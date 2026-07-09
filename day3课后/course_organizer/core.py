from pathlib import Path
import shutil
from datetime import datetime
from .rules import get_file_category

class Organizer:
    def __init__(self, source: str, target: str, dry_run: bool = False, mode: str = "copy"):
        self.source = Path(source).resolve()
        self.target = Path(target).resolve()
        self.dry_run = dry_run
        self.mode = mode  # copy / move
        self.plan = []    # 整理计划列表，每条：(源文件Path, 目标文件Path, 分类目录名)
        self.category_count = {}  # 统计每类文件数量

    def scan_files(self):
        """扫描源目录所有文件，生成整理计划（核心：先计划再执行）"""
        self.plan.clear()
        self.category_count.clear()
        # 遍历源目录，仅处理文件，跳过子文件夹
        for file in self.source.iterdir():
            if not file.is_file():
                continue
            cat_name = get_file_category(file)
            # 目标分类子目录
            cat_dir = self.target / cat_name
            target_file = self._get_safe_target_path(cat_dir, file.name)
            self.plan.append((file, target_file, cat_name))
            self.category_count[cat_name] = self.category_count.get(cat_name, 0) + 1

    def _get_safe_target_path(self, cat_dir: Path, filename: str) -> Path:
        """处理同名冲突，自动生成 文件名_1.后缀 避免覆盖"""
        target_path = cat_dir / filename
        if not target_path.exists():
            return target_path
        stem, suffix = filename.rsplit(".", 1) if "." in filename else (filename, "")
        counter = 1
        while True:
            new_name = f"{stem}_{counter}.{suffix}" if suffix else f"{stem}_{counter}"
            target_path = cat_dir / new_name
            if not target_path.exists():
                return target_path
            counter += 1

    def execute_plan(self):
        """执行整理计划，dry-run时仅打印不操作"""
        if self.dry_run:
            print("===== 【DRY-RUN 预览模式】仅展示计划，不修改文件 =====")
            for src, dst, cat in self.plan:
                print(f"[{cat}] {src.name} --> {dst}")
            print(f"\n总计待整理文件：{len(self.plan)}")
            print("各类文件数量统计：")
            for cat, cnt in self.category_count.items():
                print(f"  {cat}: {cnt} 个")
            return

        # 真实执行：创建目录、复制/移动文件
        for src, dst, cat in self.plan:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if self.mode == "copy":
                shutil.copy2(src, dst)
            elif self.mode == "move":
                shutil.move(src, dst)
        # 生成整理报告
        self.generate_report()
        print(f"整理完成！共处理 {len(self.plan)} 个文件，报告已生成：{self.target / '整理报告.txt'}")

    def generate_report(self):
        """在目标目录生成整理报告.txt"""
        report_path = self.target / "整理报告.txt"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = [
            "=" * 50,
            f"课程资料整理报告 | 执行时间：{now}",
            f"操作模式：{self.mode}（copy=复制原文件保留，move=移动原文件）",
            f"本次整理总文件数：{len(self.plan)}",
            "=" * 50,
            "\n【文件流转明细】",
        ]
        for src, dst, cat in self.plan:
            lines.append(f"[{cat}] 源：{src}  -->  目标：{dst}")
        lines.extend([
            "\n【各类文件数量统计】",
        ])
        for cat, cnt in self.category_count.items():
            lines.append(f"  {cat}：{cnt} 个")
        lines.append("=" * 50)
        report_path.write_text("\n".join(lines), encoding="utf-8")
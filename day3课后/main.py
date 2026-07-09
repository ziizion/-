import argparse
from course_organizer import Organizer

def main():
    parser = argparse.ArgumentParser(description="课程资料自动整理工具")
    # 必选参数
    parser.add_argument("--source", required=True, help="原始资料文件夹路径")
    parser.add_argument("--target", required=True, help="整理后输出文件夹路径")
    # 可选参数
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际复制/移动文件")
    parser.add_argument("--mode", choices=["copy", "move"], default="copy", help="文件操作模式：copy复制(默认) / move移动")

    args = parser.parse_args()
    # 初始化整理器
    organizer = Organizer(
        source=args.source,
        target=args.target,
        dry_run=args.dry_run,
        mode=args.mode
    )
    # 1. 先扫描生成整理计划
    organizer.scan_files()
    # 2. 执行计划（预览/真实操作）
    organizer.execute_plan()

if __name__ == "__main__":
    main()

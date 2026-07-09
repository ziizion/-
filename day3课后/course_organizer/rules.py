# 优先级关键字：命中则直接归入 homework
KEYWORD_PRIORITY_LIST = ["作业", "练习", "实验", "任务"]

# 后缀 -> 分类目录映射
EXT_CATEGORY_MAP = {
    ".ppt": "slides",
    ".pptx": "slides",
    ".key": "slides",

    ".py": "code",
    ".ipynb": "code",
    ".c": "code",
    ".cpp": "code",
    ".java": "code",

    ".csv": "data",
    ".xlsx": "data",
    ".json": "data",

    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".txt": "documents",
    ".md": "documents",

    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
}

def get_file_category(file_path):
    """
    根据文件路径判断分类，关键字优先级高于后缀
    :param file_path: Path对象
    :return: 分类文件夹名
    """
    filename = file_path.name
    # 优先匹配关键字
    for keyword in KEYWORD_PRIORITY_LIST:
        if keyword in filename:
            return "homework"
    # 再匹配后缀
    ext = file_path.suffix.lower()
    return EXT_CATEGORY_MAP.get(ext, "others")
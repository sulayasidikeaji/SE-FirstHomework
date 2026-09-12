import sys

def get_ngram(text: str, n: int = 2) -> set:
    """
    2-gram算法：把文本切分为连续双字符片段集合
    预处理：去除换行、空格，保留标点
    """
    text = text.replace("\n", "").replace(" ", "")
    gram_set = set()
    if len(text) < n:
        return gram_set
    for i in range(len(text) - n + 1):
        gram_set.add(text[i:i+n])
    return gram_set

def calc_repeat_rate(orig_text: str, copy_text: str) -> float:
    """计算重复率：交集字符片段数量 / 原文片段总数，保留两位小数"""
    orig_grams = get_ngram(orig_text, 2)
    copy_grams = get_ngram(copy_text, 2)
    if len(orig_grams) == 0:
        return 0.00
    intersection = orig_grams.intersection(copy_grams)
    rate = len(intersection) / len(orig_grams)
    return round(rate, 2)

def main():
    # 命令行参数数量校验
    if len(sys.argv) != 4:
        print("参数错误！使用方法 python main.py orig.txt copy.txt output.txt")
        sys.exit(1)
    orig_path = sys.argv[1]
    copy_path = sys.argv[2]
    out_path = sys.argv[3]

    try:
        # 读取原文
        with open(orig_path, "r", encoding="utf-8") as f:
            orig_content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到原文文件 {orig_path}")
        sys.exit(2)
    except Exception as e:
        print(f"读取原文失败: {e}")
        sys.exit(3)

    try:
        # 读取抄袭文本
        with open(copy_path, "r", encoding="utf-8") as f:
            copy_content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到抄袭文件 {copy_path}")
        sys.exit(4)
    except Exception as e:
        print(f"读取抄袭文件失败: {e}")
        sys.exit(5)

    repeat_rate = calc_repeat_rate(orig_content, copy_content)

    try:
        # 写入结果文件，保留两位小数
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{repeat_rate:.2f}")
    except Exception as e:
        print(f"写入结果文件失败: {e}")
        sys.exit(6)

if __name__ == "__main__":
    main()

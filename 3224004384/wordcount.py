# 简单单词统计程序
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

if __name__ == "__main__":
    content = "Hello Git and GitHub"
    print("单词数量：", count_words(content))
    print("字符数量：", count_chars(content))

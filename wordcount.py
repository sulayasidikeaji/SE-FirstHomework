# 简单单词统计程序
def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    content = "Hello Git and GitHub"
    print(count_words(content))

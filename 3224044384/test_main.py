import unittest
from main import get_ngram, calc_repeat_rate

class TestPaperCheck(unittest.TestCase):
    # 测试1：原文抄袭完全相同，重复率=1.00
    def test_all_same(self):
        orig = "今天是星期天，天气晴"
        copy = "今天是星期天，天气晴"
        self.assertEqual(calc_repeat_rate(orig, copy), 1.00)

    # 测试2：完全无重合文本，重复率=0.00
    def test_no_overlap(self):
        orig = "苹果香蕉"
        copy = "桌子椅子"
        self.assertEqual(calc_repeat_rate(orig, copy), 0.00)

    # 测试3：空原文
    def test_empty_orig(self):
        orig = ""
        copy = "随便文字"
        self.assertEqual(calc_repeat_rate(orig, copy), 0.00)

    # 测试4：空抄袭文本
    def test_empty_copy(self):
        orig = "测试文字"
        copy = ""
        self.assertEqual(calc_repeat_rate(orig, copy), 0.00)

    # 测试5：题目样例
    def test_sample_case(self):
        orig = "今天是星期天，天气晴，今天晚上我要去看电影。"
        copy = "今天是周天，天气晴朗，我晚上要去看电影。"
        res = calc_repeat_rate(orig, copy)
        self.assertTrue(0 < res < 1)

    # 测试6：原文只有1个字符，无法生成2gram
    def test_single_char_orig(self):
        orig = "a"
        copy = "a"
        self.assertEqual(calc_repeat_rate(orig, copy),0.00)

    # 测试7：带换行空格，预处理生效
    def test_blank_newline(self):
        orig = "今 天\n是周日"
        copy = "今天是周日"
        self.assertEqual(calc_repeat_rate(orig, copy),1.00)

    # 测试8：部分文字修改
    def test_part_modify(self):
        orig = "软件工程作业"
        copy = "软件工程实验"
        res = calc_repeat_rate(orig, copy)
        self.assertTrue(0 < res < 1)

    # 测试9：抄袭文本比原文长
    def test_copy_longer(self):
        orig = "软件工程"
        copy = "软件工程论文查重"
        res = calc_repeat_rate(orig, copy)
        self.assertEqual(res,1.00)

    # 测试10：抄袭文本比原文短
    def test_copy_shorter(self):
        orig = "软件工程论文查重"
        copy = "软件工程"
        res = calc_repeat_rate(orig, copy)
        self.assertTrue(0 < res <1)

    # 测试11：全标点
    def test_punctuation(self):
        orig = "，。！？；"
        copy = "，。！？；"
        self.assertEqual(calc_repeat_rate(orig, copy),1.00)

if __name__ == '__main__':
    unittest.main()

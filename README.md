# SE-FirstHomework
## 文本相似度查重工具
软件工程第一次作业
本项目基于Python实现，采用余弦相似度算法完成中文文本相似度计算，实现简单论文查重功能。

## 项目文件结构
- main.py：主程序，负责读取文本、分词、余弦相似度计算、结果写入文件
- test_main.py：单元测试脚本，共11组测试用例，验证程序核心逻辑
- orig.txt：原始参考文本
- orig_add.txt：待对比改写文本
- result.txt：程序运行输出，保存最终相似度结果
- htmlcov/：coverage自动生成的代码测试覆盖率报告文件夹

## 程序运行方法
```bash
python main.py orig.txt orig_add.txt result.txt

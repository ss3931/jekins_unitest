import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('.', pattern='test*.py')

# runner = unittest.TextTestRunner()
#
# runner.run(suite)
# 在控制台展示,下面的是在html中演示


# 使用HTML TestRunner去生成测试报告

# 1.生成测试报告的文件
test_report = 'test_report.html'

# 2.打开上面的文件,将运行的结果写道文件中

with open(test_report,'wb') as f:
    # w : 写  b : 二进制  a : 追加  r : 读
    # 创建一个HTMLTextRunner的运行器
    runner = HTMLTestRunner(f,title='测试报告',description='当前版本:v1.0')
    runner.run(suite)

# 点击test_report.html >  Open in Brower  > 用任意游览器打开, 查看html测试报告
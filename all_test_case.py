import unittest
import HTMLTestRunner
import time


# 路径
test_dir="F:\\maoguoying\\test_case"
test_dir1="F:\\maoguoying\\report"
# discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py",top_level_dir=None)
def creatsuitel():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py",top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
alltestnames = creatsuitel()
# 定义带有当前测试时间的报告，防止前一次报告被覆盖
now=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
filename=test_dir1+"\\"+now+"result.html"
print(filename)

# 二进制打开，准备写入文件
fp =open(filename,"wb")
# with open(filename,"wb")as fp:
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例执行情况")
runner.run(alltestnames)

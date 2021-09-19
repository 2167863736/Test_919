import unittest,HTMLTestRunner_cn
suit = unittest.defaultTestLoader.discover(start_dir='./',pattern='Test_case.py')
you = HTMLTestRunner_cn.HTMLTestRunner(open("suning.html","wb"),
                                       title='苏宁的测试报告',
                                       description="以下是二个业务的结果描述：")
you.run(suit)
import unittest
from selenium import webdriver
from time import sleep
from Second_week.Business import Business
from Second_week.Business2 import Business2
class case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
    def tearDown(self) -> None:
        pass
    def test_01(self):
        po = Business(self.driver)
        po.yewu1()
    def test_02(self):
        po = Business2(self.driver)
        po.yewu2()
        sleep(2)
        dy = self.driver.find_element_by_xpath('/html/body/div[38]/div/div[1]').text
        self.assertIn('温馨提示', dy)
if __name__ == '__main__':
    unittest.main()
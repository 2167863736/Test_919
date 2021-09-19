from time import sleep
from Second_week.Business import Business
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Business2(Business):
    gwc = (By.ID,"searchKeywords")
    gwc1 = (By.XPATH,'/html/body/div[10]/div/ul/li[9]/div/div/div[1]/div/a/img')
    gwc2 = (By.PARTIAL_LINK_TEXT,"加入购物车")
    def huad(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
    def sousuo(self):
        self.find_element(*self.gwc).send_keys("芭比",Keys.ENTER)  # 输入框
        sleep(2)
        self.find_element(*self.gwc).send_keys(Keys.ENTER)  # 回车事件
    def djss(self):
        self.driver.execute_script("window.scrollTo(0,1200)")  # 下滑
    def djsp(self):
        self.find_element(*self.gwc1).click()  # 点击商品
    def qie(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换页面
    def jiaru(self):
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        self.find_element(*self.gwc2).click()  # 点击加入购物车
    def yewu2(self):
        self.open_url("https://www.suning.com/")
        self.yewu1()
        sleep(2)
        self.huad()
        self.driver.implicitly_wait(5)
        self.sousuo()
        sleep(2)
        self.djss()
        sleep(2)
        self.djsp()
        sleep(2)
        self.qie()
        sleep(5)
        self.jiaru()

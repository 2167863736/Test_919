from time import sleep
from Second_week.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 登录业务
class Business(Base):
    dl = (By.NAME,"public0_none_denglu_denglu")
    dl1 = (By.CLASS_NAME,"qq")
    dl2 = (By.ID,"ptlogin_iframe")
    dl3 = (By.LINK_TEXT,"帐号密码登录")
    dl4 = (By.XPATH,'//*[@id="u"]')
    dl5 = (By.CSS_SELECTOR,"#p")
    dl6 = (By.ID,"login_button")
    def dnegl(self):
        # self.driver.execute_script("window_handles(0,document.body.scrollHeght)")  # 下滑到底部
        # sleep(1)
        # self.driver.execute_script("window_handles(0,0)")  # 顶部
        # sleep(2)
        a = self.find_element(*self.dl)  # 点击登录
        ActionChains(self.driver).click(a).perform()
    def djqq(self):
        self.find_element(*self.dl1).click()  # 点击QQ登录
    def idname(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
        self.driver.maximize_window()  # 最大化
        kj = self.find_element(*self.dl2)  # ifname框架
        self.driver.switch_to.frame(kj)
    def zhmm(self):
        self.find_element(*self.dl3).click()  # 点击账号密码登录
    def shuruzh(self):
        self.find_element(*self.dl4).send_keys("2167863736")
    def shurmm(self):
        self.find_element(*self.dl5).send_keys("ji20020812")
    def dengl(self):
        WebDriverWait(self.driver,10,10).until(EC.presence_of_element_located((By.ID,"login_button"))).click()  # 显示等待
    def yewu1(self):
        self.open_url("https://www.suning.com/")
        self.dnegl()
        sleep(2)
        self.djqq()
        sleep(2)
        self.idname()
        sleep(2)
        self.zhmm()
        sleep(2)
        self.shuruzh()
        sleep(2)
        self.shurmm()
        sleep(2)
        self.dengl()



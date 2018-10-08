# encoding:utf8

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('')
        self.timeout = 5
        self.poll_frequency = 0.3

    def tearDown(self):
        self.dr.quit() #关闭浏览器

    def explicit_wait_element(self,locator):
        WebDriverWait(self.dr,self.timeout,self.poll_frequency).until(EC.visibility_of_element_located(locator))

    # 封装定位方法CSS
    def by_css(self,css):
        # pass
        locator = (By.CSS_SELECTOR,css)
        #加一个显式等待
        self.explicit_wait_element(locator)
        return self.dr.find_element_by_css_selector(css)

    # 定位用户名输入框
    def username_input(self):
        return self.by_css('#usernam')

    # 定位密码输入框
    def password_input(self):
        return self.by_css('#password')

    # 定位验证码输入框
    def code_input(self):
        return self.by_css('#verificationCode')

    # 定位登陆按钮
    def login_button(self):
        return self.by_css('#accountsLoginBtn')


    def login(self,username,password,code=):
        #第一步 定位 用户名输入框 输入值
        self.username_input().clear()
        self.username_input().send_keys(username)
        #第二步 定位 密码输入框 输入值
        self.password_input().clear()
        self.password_input().send_keys(password)
        #第三部 定位 验证码 输入值
        self.code_input().clear()
        self.code_input().send_keys(code)
        #第四部 定位 点击
        self.login_button().click()

    def test_login_success(self):
        username = ''
        password = ''
        self.login(username,password)
        sleep(5)

if __name__ == '__main__':
    unittest.main()

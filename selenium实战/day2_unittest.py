#encoding:utf8

import unittest
from selenium import webdriver
from time import sleep

class SendMsgCase(unittest.TestCase):

    def setUp(self):
        # 1、打开浏览器
        self.dr = webdriver.Chrome()
        # 2、导航到我们要测试的网页
        self.dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
        self.dr.implicitly_wait(10)

    def test_send_msg_button(self):
        mobile_phone = '13145580588'
        self.send_msg(mobile_phone)
        # 5、验证button 不可点击
        self.assertFalse(self.send_msg_button().is_enabled())

        sleep(3)

        # 6、验证 发送验证码的按钮文本信息改变 为 已发送
        self.assertTrue('已发送' in self.send_msg_button().text)


    def send_msg(self,mobile_phone):
        # 3、定位到手机号码输入框，输入11位大陆手机号
        self.mobile_phone_input().send_keys(mobile_phone)

        # 验证button 可以点击
        self.assertTrue(self.send_msg_button().is_enabled())
        # 4、定位到发送验证码的button ，点击操作
        self.send_msg_button().click()



    # 定位方法
    def by_css(self,css):
        return self.dr.find_element_by_css_selector(css)

    # 手机号码输入框的定位
    def mobile_phone_input(self):
        return self.by_css('[type = "tel"]')

    # 发送验证码的按钮 定位
    def send_msg_button(self):
        return self.by_css('.CountButton-3e-kd')



    def tearDown(self):
        self.dr.quit()




if __name__ =='__main__':
    unittest.main()
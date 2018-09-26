# encoding:utf8

# 元素显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

'''
元素定位成功，不代表能操作，因为元素可能是不可见的
'''
'''
这个是最初学习的水平
'''
time_out = 10
poll = 0.5

dr = webdriver.Chrome()
dr.get('http://test-www.tianhangbox.net/view/login.shtml')
username_locator = (By.CSS_SELECTOR,'#username')
WebDriverWait(driver=dr, timeout=time_out, poll_frequency=poll).until(EC.visibility_of_element_located(locator=username_locator))   #ctrl+shift 加上下
dr.find_element_by_css_selector('#username').send_keys('13286993500')



password_locator = (By.CSS_SELECTOR,'#password')
WebDriverWait(driver=dr, timeout=time_out, poll_frequency=poll).until(EC.visibility_of_element_located(locator=username_locator))   #ctrl+shift 加上下
dr.find_element_by_css_selector('#password').send_keys('123456')
dr.find_element_by_css_selector('#verificationCode').send_keys('123456')
dr.find_element_by_css_selector('#accountsLoginBtn').click()

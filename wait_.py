#encoding:utf8

#元素显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ECt
from selenium.webdriver.common.by import By
dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
locator = (By.CSS_SELECTOR,'#kw')
WebDriverWait(driver=dr,timeout=3,poll_frequency=0.3).until(EC.visibility_of_element_located(locator))
dr.find_element(By.CSS_SELECTOR,'#kw').send_keys('杨芳振')

'''
敲高亮的代码，同时放到github上面  ctrl + K 提交到本地代码库   然后push到github
'''
# dr.find_element_by_css_selector('#kw').send_keys('杨芳振')

'''
1、翻译expected_conditions里面的所有类方法
2、都使用一遍
3、如何加快代码执行速度、如何增加脚本稳定性
做好了提交到github

'''



# print(dr.title)
# WebDriverWait(driver=dr,timeout=3,poll_frequency=0.3).until(EC.visibility_of_element_located())
#
# EC.visibility_of_element_located() 这个是一个条件，返回真或假
#
# print('---2---')

# 因为 dr.find_element_by_css_selector('#kw') 这行代码返回的是一个WebElement对象
#
# class title_is(object):
#     """An expectation for checking the title of a page.
#     title is the expected title, which must be an exact match
#     returns True if the title matches, false otherwise."""
#     def __init__(self, title):
#         #self.title = ’百度一下‘
#         self.title = title
#
#     #类方法，执行类就是执行方法
#     def __call__(self, driver):
#         # return '百度一下' 等于 driver.title
#         return self.title == driver.title
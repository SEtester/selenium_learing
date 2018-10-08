from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.implicitly_wait(10)

# 导航到 饿了么 注册页面
dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')

# 定位并输入手机号
dr.find_element_by_css_selector('[type = "tel"]').send_keys('13148850552')


# 打印 定位【获取验证码】按钮 ，is_enabled()返回结果
print('is_enabled()_1 点击发送验证码button 之前 返回结果:', dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled())


# 点击【获取验证码】按钮
dr.find_element_by_css_selector('.CountButton-3e-kd').click()

# 打印 定位【获取验证码】按钮 ，is_enabled()返回结果
print('is_enabled()_2 点击发送验证码button 之后 返回结果:', dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled())

# 验证【获取验证码】按钮不可点击
assert dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled() == False
sleep(2)

# 获取 “验证码发送成功” 文本信息
actual_result = dr.find_element_by_css_selector('.CountButton-3e-kd').text
print('actual_result:', actual_result)

# 验证 【获取验证码】 文本信息 变更 【已发送】
assert '已发送' in actual_result


# 验证【获取验证码】按钮不可点击
assert dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled() == True
sleep(2)

# 点击【获取验证码】按钮
dr.find_element_by_css_selector('.CountButton-3e-kd').click()

# 验证【获取验证码】按钮不可点击
assert dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled() == False

# 如何判断 发送验证码的间隔 30s
# 杨芳振的思路：不断地点, 循环30次，

dr.find_element_by_css_selector().is_enabled()
dr.find_element_by_css_selector().is_displayed()
dr.find_element_by_css_selector().is_selected()

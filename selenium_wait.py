#encoding:utf8

#元素显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
poll = 1
end_time = time.time() + 10
dr = webdriver.Chrome()
# wait = WebDriverWait(dr,timeout=10,)
dr.get('https://www.baidu.com')
flag = 1
while True:
    try :
        flag = flag +1
        print('flag:',flag)
        dr.find_element_by_css_selector('#kw').is_displayed()
    except Exception:
        print('----')
    time.sleep(poll)
    print(time.ctime())
    if time.time() > end_time:
        break


'''
def until(self, method, message=''):
    """Calls the method provided with the driver as an argument until the \
    return value is not False."""
    screen = None
    stacktrace = None

    设置了超时时间  end_time = 当前时间 + 10
    end_time = time.time() + self._timeout
    while True:
        try:
            这句话意思 value 指向 一个方法，这个方法必须传入 driver实例才能使用
            value = method(self._driver)
            如果 value 指向的这个方法返回真  那么 返回 value,如果是假就异常处理
            if value:
                return value
        except self._ignored_exceptions as exc:
            screen = getattr(exc, 'screen', None)
            stacktrace = getattr(exc, 'stacktrace', None)
        强制等待
        time.sleep(self._poll)
        if time.time() > end_time:
            break
    raise TimeoutException(message, screen, stacktrace)
'''

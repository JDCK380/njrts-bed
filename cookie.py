from selenium import webdriver
import json
import time

# 初始化 WebDriver
driver = webdriver.Chrome()  # 你也可以使用其他浏览器的 WebDriver

# 打开目标网站
driver.get('https://yx.njrts.edu.cn/swms/')  # 替换为你想访问的网站

# 等待页面加载
time.sleep(30)  # 根据需要调整等待时间

# 获取 cookies
cookies = driver.get_cookies()

# 将 cookies 存储到本地文件
with open('cookies.json', 'w') as f:
    json.dump(cookies, f)

# 关闭 WebDriver
driver.quit()

print("Cookies 已成功保存到 cookies.json")

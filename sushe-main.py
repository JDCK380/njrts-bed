from selenium import webdriver
import datetime
import time
import winsound
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument("--window-size=414,896")  # iPhone 14 Pro Max 的分辨率
chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1")

# 初始化 WebDriver
service = Service('chromedriver.exe')  # 替换为你的 ChromeDriver 路径
WebDriver = webdriver.Chrome(service=service, options=chrome_options)

TargetTime = "2024-09-10 11:30:00.00000000"  # 设置抢购时间

WebDriver.get(
    "https://yx.njrts.edu.cn/swms/mobile2024052316/yxfw/dormitory/optionalDormitory.html")  # 输入目标购买页面
  time.sleep(3)
# 等待页面加载完成
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

for cookie in cookies:
    WebDriver.add_cookie(cookie)

WebDriver.refresh()

print("进入抢宿舍页面成功")

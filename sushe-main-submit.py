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
# time.sleep(0)
# 等待页面加载完成
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

for cookie in cookies:
    WebDriver.add_cookie(cookie)
    

WebDriver.refresh()

print("进入抢宿舍页面成功")

# 找到所有 bed-item status-2 元素
bed_items = WebDriver.find_elements(By.XPATH, '//div[@class="bed-item status-2"]')

'''
# 检查是否找到元素并点击特定的一个
if len(bed_items) > 1:  # 例如，点击第二个元素
    bed_items[1].click()  # 索引从 0 开始，所以 1 是第二个
    print("成功点击110-2")
else:
    print("没有找到")
'''

yes = WebDriver.find_elements(By.XPATH, '//div[@id="button_submit"]')

time.sleep(5)

try:
    # 显示被隐藏的元素
    WebDriver.execute_script("document.getElementById('button_submit').style.display = 'block';")
    
    # 直接点击元素
    WebDriver.execute_script("document.getElementById('button_submit').click();")
    
    print("成功点击元素")
except Exception as e:
    print(f"点击失败: {e}")


'''
while True:
    try:
        WebDriver.find_element(By.CLASS_NAME, "nav-header-register")
    except:
        break



while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now + "     " + TargetTime)
    if now >= TargetTime:
        WebDriver.refresh()
        break

while True:
    try:
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[1]')))
        element.click()
        # 等待抢票按钮出现并可点击
        element = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'product-buy.enable')))
        # 点击抢票按钮
        element.click()
        # time.sleep(5)
        print("进入购买页面成功")
    except BaseException as e:
        WebDriver.refresh()
        continue

    try:
        WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active").click()
        print("订单创建完成，请在一分钟内付款")

        duration = 10000  # 持续时间为 10 秒钟，单位为毫秒
        freq = 440  # 播放频率为 440 Hz
        winsound.Beep(freq, duration)  # 播放系统嗡嗡声

        time.sleep(60)
    except:
        print("无法点击创建订单")
'''

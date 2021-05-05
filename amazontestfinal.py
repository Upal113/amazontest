from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

urls = ['https://www.amazon.com/Lenovo-Processor-Graphics-Included-81X20005US/dp/B086226DDB/ref=lp_16225007011_1_8', 
        'https://www.amazon.com/Roku-Streaming-Stick-HDR-Streaming-Long-range/dp/B075XLWML4/ref=lp_16225007011_1_3',
        'https://www.amazon.com/Oculus-Quest-Advanced-All-One-2/dp/B08F7PTF53/ref=lp_16225016011_1_1',
        'https://www.amazon.com/Lenovo-Processor-Graphics-Included-81X20005US/dp/B086226DDB/ref=lp_16225007011_1_10']
excel_sheet = []
for url in urls:
    option = webdriver.ChromeOptions()
    option.headless = True
    driver = webdriver.Chrome('D://chromedriver.exe', options=option)
    driver.get(url)
    driver.implicitly_wait(5)
    price = driver.find_element_by_id('priceblock_ourprice').text
    title = driver.find_element_by_id('productTitle').text
    excel_item = {
        'title' : title,
        'price':price
    }
    excel_sheet.append(excel_item)
df = pd.DataFrame(excel_sheet)
file = pd.ExcelWriter('amazon1.xlsx')
df.to_excel(file)
file.save()
print(df)

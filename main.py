import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import emoji


rent591_url = "https://www.591.com.tw/"
google_form = "https://docs.google.com/forms/d/1RNGGWQ6fpzb6booYXEx0QQgHrZWr53N4xiFJM-bP1xY/edit"
driver = uc.Chrome()
driver.get(rent591_url)

city = driver.find_element(By.XPATH, '//*[@id="area-box-body"]/dl[1]/dd[4]')
city.click()
time.sleep(2)

ad_close = driver.find_element(By.CLASS_NAME, "for-love-close")
ad_close.click()
search = driver.find_element(By.CLASS_NAME, "auto-search-btn")
search.click()

rent_price = driver.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/div[2]/section[3]/ul/li[8]/div/input[2]')
rent_price.send_keys("12000")
confirm = driver.find_element(By.CLASS_NAME, "filter-custom-submit")
confirm.click()
time.sleep(2)

check = driver.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/div[2]/section[5]/ul/li[4]/i')
check.click()
time.sleep(2)

all_rent = driver.find_elements(By.CLASS_NAME, "vue-list-rent-item")
titles = [i.find_element(By.CLASS_NAME, "item-title").text for i in all_rent]
addresses = [i.find_element(By.CSS_SELECTOR, "div.item-area span").text for i in all_rent]
links = [i.find_element(By.CSS_SELECTOR, "a").get_attribute("href") for i in all_rent]
prices = [i.find_element(By.CLASS_NAME, "item-price").text for i in all_rent]

driver.close()

for num in range(len(titles)):
    driver = webdriver.Chrome()
    driver.get(google_form)
    time.sleep(1)
    answer = driver.find_elements(By.CLASS_NAME, "whsOnd")
    for i in answer:
        if answer.index(i) == 0:
            title = emoji.demojize(titles[num])
            i.send_keys(title)
        elif answer.index(i) == 1:
            i.send_keys(links[num])
        elif answer.index(i) == 2:
            i.send_keys(prices[num])
        else:
            i.send_keys(addresses[num])

    apply = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    apply.click()

    driver.close()

driver.get("https://docs.google.com/forms/d/1RNGGWQ6fpzb6booYXEx0QQgHrZWr53N4xiFJM-bP1xY/edit#responses")
sheet = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/'
                                      'div[1]/div/span/span[2]')
sheet.click()
name = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[11]/div/div[2]/span/div/div/span/div[1]/div/'
                                     'div/div[1]/div/div[1]/input')
name.send_keys("renting search")
ok = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[11]/div/div[2]/div[3]/div[2]/span/span')
ok.click()

driver.close()

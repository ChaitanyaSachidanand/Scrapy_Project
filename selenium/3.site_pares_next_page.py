from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

'''refered this site for code : https://reflect.run/articles/installing-chromedriver-and-python-selenium/'''
browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(10)

# query = "Python"

# <div class="UpdateCityModal__cancel-btn___2jWwS UpdateCityModal__btn___oMW5n" data-auto-updatecity-cancel="true">Cancel</div>
# <div class="UpdateCityModal__cancel-btn___2jWwS UpdateCityModal__btn___oMW5n" data-auto-updatecity-cancel="true">Cancel</div>
# //*[@id="container"]/div/div/div[2]/a[2]
browser.get("https://www.1mg.com/drugs-all-medicines")
# browser.implicitly_wait(30)
browser.find_element(By.XPATH,'//*[@id="update-city-modal"]/div/div[3]/div[1]').click()
print("done")

for i in range(1,4):
    browser.find_element(By.XPATH,'//*[@id="container"]/div/div/div[2]/a['+str(i)+']').click()
    for j in range(1,4):
        med_link=browser.find_element(By.XPATH,"(//div[@class='style__product-card___1gbex style__card___3eL67 style__raised___3MFEA style__white-bg___10nDR style__overflow-hidden___2maTX'])["+str(j)+"]")
        # med_link=browser.find_element(By.XPATH,"(//div[@class='style__product-card___1gbex style__card___3eL67 style__raised___3MFEA style__white-bg___10nDR style__overflow-hidden___2maTX'])[1]")
        med_link.click()
        
        browser.switch_to.window(browser.window_handles[1])
        element = browser.find_element(By.XPATH,"//h1[@class='DrugHeader__title-content___2ZaPo']")
        print(element.text)
        element = browser.find_element(By.XPATH,"//span[normalize-space()='Prescription Required']")
        print(element.text)
        element = browser.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/div')
        print(element.text)
        element = browser.find_element(By.XPATH,'//*[@id="uses_and_benefits"]/div/div/div[1]/div')
        print(element.text)
        # //div[normalize-space()='Avastin 100mg Injection']
        # //*[@id="container"]/div/div/div[4]
        # //*[@id="container"]/div/div/div[4]/div[1]/div
        
        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         EC.visibility_of_any_elements_located((By.ID, "myDynamicElement")) # didint test it yet
        #     )
        # finally:
        #     browser.close()
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    # time.sleep(3)
    # browser.switch_to.window(browser.window_handles[3])
    # browser.close()
    # time.sleep(3)
    # browser.switch_to.window(browser.window_handles[2])
    # browser.close()
    # time.sleep(3)
    # browser.switch_to.window(browser.window_handles[1])
    # browser.close()
    # time.sleep(3)
    # browser.switch_to.window(browser.window_handles[0])
    # browser.close()
    # print(med_links)
    print("doing ",i)
# a  = browser.find_elements(By.CLASS_NAME,"style__chips___2T95q")
# search_input = browser.find_element(By.ID, "searchInput")
# search_input.send_keys(query)

# suggestions = browser.find_elements(By.CLASS_NAME, 'suggestion-link')
# assert len(suggestions) > 0

# for suggestion in suggestions:
#     title_element = suggestion.find_element(
#         By.CLASS_NAME, 'suggestion-highlight')
#     assert re.search(query, title_element.text)

# suggestions[0].click()
# assert re.search(query, browser.current_url)

# page_heading = browser.find_element(By.ID, "firstHeading")
# assert re.search(query, page_heading.text)

print("tests passed")
browser.quit()
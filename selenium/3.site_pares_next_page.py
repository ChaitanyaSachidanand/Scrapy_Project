from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
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
med_data={}
for i in range(1,27):
    med_data["Med_Character"]=i
    browser.find_element(By.XPATH,'//*[@id="container"]/div/div/div[2]/a['+str(i)+']').click()
    lnks=browser.find_elements(By.TAG_NAME,"a")
    print(len(lnks))
    print(len(lnks[337:-36])+1)
# traverse list
    # for lnk in lnks[337:-36]:

   # get_attribute() to get all href
        # print(lnk.get_attribute("href"))
    count=0
    while(True):
        count+=1
        print("The count of the current page: ",count)
        med_data["page_count"]=count
        for j in range(1,len(lnks[337:-36])+1,20):
             
            # browser.refresh()   
            med_link=browser.find_element(By.XPATH,"(//div[@class='style__product-card___1gbex style__card___3eL67 style__raised___3MFEA style__white-bg___10nDR style__overflow-hidden___2maTX'])["+str(j)+"]")
            # med_link=browser.find_element(By.XPATH,"(//div[@class='style__product-card___1gbex style__card___3eL67 style__raised___3MFEA style__white-bg___10nDR style__overflow-hidden___2maTX'])[1]")
            
            med_link.click()
            
            browser.switch_to.window(browser.window_handles[1])

            element = browser.find_element(By.XPATH,"//h1[@class='DrugHeader__title-content___2ZaPo']") or None

            med_data["Name"]=element.text
            print(element.text)
            # try:
            
            element = browser.find_element(By.XPATH,"//*[@id='atc-content']/div")
                                                    
            med_data["Price"]=element.text
            print(element.text)                             
            # except NoSuchElementException:
            #     element = browser.find_element(By.XPATH,"//*[@id='atc-content']/div/div[2]/div[1]/div")
            #     med_data["Price"]=element.text
            #     print(element.text)
            try:
                element = browser.find_element(By.XPATH,"//div[@class='DrugHeader__prescription-req___34WVy']") or None
                med_data["Prescription"]=element.text
                print(element.text)
            except NoSuchElementException:
                med_data["Prescription"]=None
                # print(e)

            try:
                element = browser.find_element(By.XPATH,"//div[@class='DrugHeader__left___19WY-']//div//div[2]//div[2]") 
            
                print(element.text)
                med_data["COMPOSITION"]=element.text
            except NoSuchElementException:
                med_data["COMPOSITION"]=None
            try:
                element = browser.find_element(By.XPATH,"//*[@id='drug_header']/div/div/div[3]/div[1]/div[2]/div[3]/div[2]") or None
                print(element.text)
                med_data["Storage"]=element.text
            except NoSuchElementException:
                med_data["Storage"]=None
                
            try:
                element = browser.find_element(By.XPATH,'//*[@id="overview"]/div/div/div/div') or None
                med_data["overview"]=element.text
                print(element.text)
            except NoSuchElementException:
                med_data["overview"]=None
            try:    
                element = browser.find_element(By.XPATH,'//*[@id="uses_and_benefits"]/div/div/div[1]/div') or None
                print(element.text)
                med_data["uses_and_benefits"]=element.text
            except NoSuchElementException:
                med_data["uses_and_benefits"]=None
                
            try:    
                element = browser.find_element(By.XPATH,"//div[@class='DrugOverview__list-container___2eAr6 DrugOverview__content___22ZBX']") or None
                print(element.text)
                med_data["SIDE_EFFECTS"]=element.text
            except NoSuchElementException:
                med_data["SIDE_EFFECTS"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='how_to_use']/div/div/div/div") or None
                print(element.text)
                med_data["how_to_use"]=element.text
            except NoSuchElementException:
                med_data["how_to_use"]=None

            try:    
                element = browser.find_element(By.XPATH,"//*[@id='how_drug_works']/div/div/div/div") or None
                print(element.text)
                med_data["how_drug_works"]=element.text
            except NoSuchElementException:
                med_data["how_drug_works"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='safety_advice']/div/div/div/div") or None
                print(element.text)
                med_data["safety_advice"]=element.text
            except NoSuchElementException:
                med_data["safety_advice"]=None
            
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='safety_advice']/div/div/div/div") or None
                print(element.text)
                med_data["safety_advice"]=element.text
            except NoSuchElementException:
                med_data["safety_advice"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='expert_advice']/div[2]/div/div[2]") or None
                print(element.text)
                med_data["expert_advice_Q_TIPS"]=element.text
            except NoSuchElementException:
                med_data["expert_advice_Q_TIPS"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='missed_dose']/div/div/div/div") or None
                print(element.text)
                med_data["missed_dose"]=element.text
            except NoSuchElementException:
                med_data["missed_dose"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='substitutes']/div[2]/div/div[2]") or None
                print(element.text)
                med_data["substitutes_med"]=element.text
            except NoSuchElementException:
                med_data["substitutes_med"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='user_feedback']/div[2]/div[1]") or None
                print(element.text)
                med_data["user_feedback"]=element.text
            except NoSuchElementException:
                med_data["user_feedback"]=None
            
            try:
                element = browser.find_element(By.XPATH,"//*[@id='fact_box']/div[2]/div/div/div[1]/div[2]") or None
                print(element.text)
                med_data["Chemical_Class"]=element.text
            except NoSuchElementException:
                med_data["Chemical_Class"]=None
            try:
                element = browser.find_element(By.XPATH,"//*[@id='fact_box']/div[2]/div/div/div[2]/div[2]") or None
                print(element.text)
                med_data["Habit_Forming"]=element.text 
            except NoSuchElementException:
                med_data["Habit_Forming"]=None
            try:
                element = browser.find_element(By.XPATH,"//*[@id='fact_box']/div[2]/div/div/div[3]/div[2]") or None
                print(element.text)
                med_data["Therapeutic_Class"]=element.text
            except NoSuchElementException:
                med_data["Therapeutic_Class"]=None
            try:
                element = browser.find_element(By.XPATH,"//*[@id='fact_box']/div[2]/div/div/div[4]/div[2]") or None
                print(element.text)
                med_data["Action_Class"]=element.text
            except NoSuchElementException:
                med_data["Action_Class"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='drug-main-header']/div[18]/div[2]") or None
                print(element.text)
                med_data["Related_lab_tests"]=element.text
            except NoSuchElementException:
                med_data["Related_lab_tests"]=None
            try:    
                element = browser.find_element(By.XPATH,"//*[@id='drug-main-header']/div[20]") or None
                print(element.text)
                med_data["Related_Ayurvedic_Ingredients"]=element.text
            except NoSuchElementException:
                med_data["Related_Ayurvedic_Ingredients"]=None

            print("data featched",j)
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
        try:    
           element = browser.find_element(By.CSS_SELECTOR,".next.link-disabled")
        #    element.click()
           break

        except NoSuchElementException:
            element = browser.find_element(By.CSS_SELECTOR,".next")
            # next link-disabled
            # //*[@id="container"]/div/div/div[5]/ul/li[8]
            
        #     element = browser.find_element(By.XPATH,"//*[@id='container']/div/div/div[5]/ul/li[9]/a")
            element.click()
            
      
        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         EC.visibility_of_any_elements_located((By.ID, "myDynamicElement")) # didint test it yet
        #     )
        # finally:
        #     browser.close()
        
    browser.refresh()
    
    print("doing ",i)
    

print("tests passed")
browser.quit()
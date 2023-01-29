from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.
driver = webdriver.Chrome(r"./driver/chromedriver")
  
# get https://www.geeksforgeeks.org/
driver.get("https://www.harrisvotes.com/Voter/Registration/Voter-Precinct-Data")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(10)
  
# Obtain button by link text and click.
iframe = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
selector = Select(driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/form/p/select'))
button = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/form/p/input')
for opt in selector.options:
    # for example
    selector.select_by_value(opt.text)
    print(opt.text)
    button.click()
time.sleep(5)
driver.close()
#<select name="Precinct" id="Download1" class="pc form-control input-sm">
#<iframe src="https://app.harrisvotes.com/VoterRegistration/PrecinctData" scrolling="off"></iframe>
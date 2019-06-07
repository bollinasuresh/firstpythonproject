from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\sbollina\\Desktop\\jars\\chromedriver.exe")
driver.get("http://www.liveupindia.com/")
address_button = driver.find_element_by_xpath("//*[@class='btn btn-link btn-md dropdown-toggle search-location-btn']/span[2]")
#print(address_button.is_enabled())
#print(address_button.is_displayed())
address_button.click()
#print("====================================")
city_list = driver.find_elements_by_xpath("//*[@class='dropdown-menu applyfilter project-type search-location']/li")
#print(len(city_list))
for city in city_list:
    city_to_select = city.text.strip()
    if city_to_select == "Pune":
        print(city.text.strip(), " is selected")
        city.click()
        break
    print("selected")
driver.quit()

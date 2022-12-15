#imports

#all imports to help selenium run
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#imports for other functions
import time
import json
import re
import random

#set up webdriver:
#open up chrome webdriver
options = webdriver.ChromeOptions()
#open up inspect (necessary to access the menu webpage in a way where I can scrape it efficiently)
options.add_argument("--auto-open-devtools-for-tabs")

#assembly of selenium packages
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
DRIVER_PATH = '/path/to/chromedriver'
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


#open up nutrislice webpage (picks a random of 2 working links to help minimize chance of captcha)
rand = random.randint(0, 1)
if rand == 0:
    driver.get("https://menus.flikisdining.com/en/")
else:
    driver.get("https://lookup.nutrislice.com/en/")


#first page

#finds input field
search = driver.find_element(By.TAG_NAME, "input")

#sends keys to the input slowly to prevent captcha detection
search.send_keys("Ca")
time.sleep(5)
search.send_keys("nnon")
time.sleep(.5)
search.send_keys(" Sch")
time.sleep(1)
search.send_keys("ool")
search.send_keys(Keys.RETURN)
time.sleep(2)

#finds button to click on Cannon School and clicks on it
cannon_button = driver.find_element(By.ID, "cdk-overlay-0")
action = ActionChains(driver)
action.click(on_element = cannon_button)
action.perform()
time.sleep(2)


#second page

#find button for menus and click on it
menus_button = driver.find_element(By.CLASS_NAME, "primary")
action2 = ActionChains(driver)
action2.click(on_element = menus_button)
action2.perform()
time.sleep(2)


#third page

#find button for grades and click on it
grades_button = driver.find_element(By.LINK_TEXT, "2nd Grade- Upper School")
action3 = ActionChains(driver)
action3.click(on_element = grades_button)
action3.perform()
time.sleep(5)


#scrape the text data from the webpage
html = driver.find_element(By.ID, "content")



#open up the json file
with open("flik.json", "r") as f:
    data = json.load(f)

#empty the json file (must create each variable first in case it does not exist)
data['Raw String'] = ""
del data['Raw String']

data["Soup"] = ""
del data['Soup']

data["Entrees/Sides"] = ""
del data['Entrees/Sides']

data["Innovations"] = ""
del data['Innovations']

data['Vegetarian'] = ""
del data['Vegetarian']

data['Gluten Free'] = ''
del data['Gluten Free']





#edge case to check if there is no food on the menu that day
menu = re.search("There is currently nothing on the menu today", html.text)
if menu is not None:
    data['Raw String'] = "No Food Today :)"

#if there is food on the menu
else: 
    #use RegEx to split the strings into the different meal types
    data['Raw String'] = html.text

    #each split creates an array with everything to the left of the string in array[0], and everything to the right array[1]
    str = re.split('\nSoup\n', html.text)
    entree_split = re.split('\nEntree/Sides\n', str[1])
    innovation_split = re.split('\nInnovation\n', entree_split[1])
    veg = re.search("\nVegetarian\n", innovation_split[1])


    #edge case because somedays there is not a vegetarian option
    if veg is not None:
        vegetarian_split = re.split("\nVegetarian\n", innovation_split[1])
        
    gluten_split = re.split("\nMade Without Gluten Containing Ingredients - Hot Lunch Combo\n", innovation_split[1])





    #creates json string for the soup
    data['Soup'] = entree_split[0]

    #creates json array for entrees
    all_entrees = re.split("\n", innovation_split[0])
    data["Entrees/Sides"] = all_entrees

    #creates json array for innovation (works with vegetarian edge case)
    if veg is not None:
        all_innovation = re.split("\n", vegetarian_split[0])
    else:
        all_innovation = re.split("\n", gluten_split[0])
    data["Innovations"] = all_innovation

    #creates json array for vegetarian (if it exsits)
    if veg is not None:
        all_vegetarian = re.split("\n", gluten_split[0])
        data['Vegetarian'] = all_vegetarian

    #creates json array for gluten
    all_gluten = re.split("\n", gluten_split[1])
    all_gluten.pop(0)
    data['Gluten Free'] = all_gluten

#dumps the json into the file
with open('flik.json', 'w') as f:
        json.dump(data, f, indent=2)




driver.quit()
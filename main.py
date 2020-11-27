from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import sys

browser = webdriver.Chrome()

browser.maximize_window()

browser.get('https://web.whatsapp.com/')

try :
    if sys.argv[1]:

        with open('groups.txt', 'r', encoding='utf8') as f:
            groups = [group.strip() for group in f.readlines()]
except IndexError:
    print('Please provide the group name as the first argument.')

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()

for g in groups:

    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(1)

    #using pyperclip inorder to use the emojies 
    pyperclip.copy(g)

    search_box.send_keys(Keys.CONTROL + "v")  # Keys.CONTROL + "v"

    time.sleep(2)

    #setting tile for the span tag to fetch the user name in the search bar
    #group_xpath = f'//span[@title="{g}"]'
    group_xpath = '//span[@dir="ltr"][@class="_1hI5g _1XH7x _1VzZY"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)

    #typing the text bar to send message
    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.CONTROL + 'v')  # Keys.CONTROL + "v"
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)

    try:
        if sys.argv[2]:
            attachment_box = browser.find_element_by_xpath('//div[@title="Attach"]')
            attachment_box.click()
            time.sleep(1)

            image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            path = sys.argv[2]
            print(sys.argv[2])
            
            #C:\Users\USER\Desktop\whatsapp_automaton\python.png

            image_box.send_keys(path)
           
            time.sleep(2)

            send_btn = browser.find_element_by_xpath('//span[@data-icon="send"]')
            send_btn.click()
            time.sleep(2)


    except IndexError:
        pass
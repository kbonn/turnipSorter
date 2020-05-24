from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import sys

min_bells = sys.argv[1]
max_queue = sys.argv[2]

d = webdriver.Chrome(executable_path='./chromedriver')
d.get('https://turnip.exchange/islands')

time.sleep(1)
d.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[3]/div/button[2]').click()
time.sleep(1)

island_list = []
good_islands = False

islands = d.find_elements_by_css_selector('div.note')

for island in islands:
    island_name = island.find_element_by_css_selector('h2 p.text-center').text
    bells, text = island.find_element_by_css_selector('p.ml-2').text.split(' ')
    queue_text, queue = island.find_element_by_css_selector('p.mr-1').text.split(' ')
    queue_waiting, total_queue = queue.split('/')

    if (int(bells) > int(min_bells) and int(queue_waiting) < int(max_queue)):
        good_islands = True
        island_url = "https://turnip.exchange/island/" + island.get_attribute('data-turnip-code')
        island_info = [island_name, bells, queue, island_url]
        island_list.append(island_info)
        # island.click()

if (good_islands == True):
    sorted_island_list = sorted(island_list, key = lambda x: int(x[1]))
    for list in sorted_island_list:
        d.execute_script('window.open("' + list[3] + '","_blank");')
        print(list)
else:
    print("No good islands :(")
import json
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config
import time
import pandas as pd

from abc import ABC, abstractmethod

class WebScrapper(ABC):

    @abstractmethod
    def get_data_url(self):
        pass


class Olympic(WebScrapper):

    def __init__(self, driver_path):
        options = Options()
        for arg in config['seleniumConfig']['chromeOptions']:
            options.add_argument(arg)
        self.driver = Chrome(
            executable_path=driver_path,
            options=options
        )
    

    def get_data_url(self, url):
        self.driver.get(url)
        
        #sports = [opl.get_attribute('title') for opl in options_list if opl.get_attribute('title') != '']
        #print(sports)
        #sports_json = []
        #for sport in sports:
        #    sports_json.append({
        #        "name": sport,
        #        "shortname": ""
        #    })
        #with open("./Sports.json", "w") as out_json:
        #    json.dump(sports_json, out_json)

        #special_ul = self.driver.find_element_by_id('document-event')
        #special_div = special_ul.find_element_by_class_name('form-group')
        #lis = special_div.find_elements_by_tag_name('li')
        #events = [li for li in lis]
        #events_json = []
        #for event in events:
        #    events_json.append({
        #        "name": event.find_element_by_class_name('dropdown-link').get_attribute('textContent').replace("\n", ""),
        #        "sportShortname": event.get_attribute('discipline')
        #    });
        #with open("./Events.json", "w", encoding='utf8') as out_json:
        #    json.dump(events_json, out_json, ensure_ascii=False)

        #special_div = self.driver.find_element_by_id('medallist-country')
        #lis = special_div.find_elements_by_tag_name('li')[1:]
        #noc = [li for li in lis]
        #noc_json = []
        #for nc in noc:
        #    noc_json.append({
        #        "name": nc.find_element_by_class_name('d-md-table-cell').get_attribute('textContent'),
        #        "countryShortname": nc.get_attribute('name'),
        #        "flagUrl": nc.find_elements_by_tag_name('img')[0].get_attribute('src')
        #    });
        #with open("./Countries.json", "w", encoding='utf8') as out_json:
        #    json.dump(noc_json, out_json, ensure_ascii=False)

        sports_json = []
        ul = self.driver.find_element_by_class_name('tk-disciplines__sequence')
        lis = ul.find_elements_by_tag_name('li')
        a = []
        for li in lis:
            print(li.get_attribute('innerHTML'))
            try:
                a.appends(li.find_elements_by_tag_name('a'))
            except Exception:
                print(Exception)
        print(a)

        
        #medals_json = []
        #WebDriverWait(self.driver, 10000)
        #self.driver.find_element_by_id('onetrust-accept-btn-handler').click()
        #WebDriverWait(self.driver, 10000)
#
#
        #for x in range(0,64):
        #    special_table = self.driver.find_element_by_id('medals-table')
        #    trs = special_table.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[1:]
        #    for tr in trs:
        #        tds = tr.find_elements_by_class_name('invisible')
        #        medals_json.append({
        #            "rank": tr.find_element_by_class_name('sorting_1').find_element_by_tag_name('img').get_attribute('alt'),
        #            "countryShortname": tds[0].get_attribute('textContent')[1:-1],
        #            "sportShortname": tds[1].get_attribute('textContent')[1:-1],
        #            "event": tr.find_elements_by_tag_name('td')[3].text
        #        })
        #    time.sleep(1)
        #    WebDriverWait(self.driver, 1000)
        #    self.driver.find_element_by_link_text("Next").click()
        #with open("./Medals.json", "w", encoding='utf8') as out_json:
        #    json.dump(medals_json, out_json, ensure_ascii=False)

        self.driver.quit()
        return None

url = config['url']
#"url": "https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medalists.htm"
selenium_config = config['seleniumConfig']
olympic = Olympic(selenium_config['driverPath'])
olympic.get_data_url(url)
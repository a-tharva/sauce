"""Web search with selenium

This module opens new chrome window for image search and retuns result to file
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import time


inc = webdriver.ChromeOptions()
inc.add_argument("--incognito")

def search_that(url, filename):
    """To search url image
    
    Keywords:
    url -- image url for google images
    filename -- to create file and store search results
    """
    try:
        f = open(filename,'w')
        
        # location of chrome driver
        driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options= inc)
        driver.implicitly_wait(0.5)
        
        # open google image search
        driver.get('https://images.google.com/')
        
        # find cam button
        cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()
        
        # input url 
        paste_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[1]/input")
        paste_url.send_keys(url)
        
        # click search button
        img_searc = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[2]/input")
        img_searc.click()
        
        #just in case
        time.sleep(2) 
        
        # return websites result
        elems = driver.find_elements_by_class_name('yuRUbf')
        for i in elems:
            a = i.find_elements_by_tag_name("a")
            for _ in a:
                n = _.get_attribute('href')
                f.write(n+"\n\n")
                print(n)
    except Exception as Error:
        print(Error)

        
def wiki(search_term):
    import wikipedia
    
    wikipage = wikipedia.summary(search_term, sentences=50)
    print(f'{wikipage}\n\n')
    
    
def duckduckgo(search_for):
    response = requests.get(f'http://api.duckduckgo.com/?q={search_for}&format=json')
    response = response.json()
    # Print data
    print('Heading:',response['Heading'])
    print('Abstract:',response['Abstract'])
    print('Abstract source:',response['AbstractSource'])
    print('Abstract text:',response['AbstractText'])
    print('Definition:',response['Definition'])
    # No of related topics from result
    related_no = 2
    print('Related Topic:')
    for i in response['RelatedTopics']:
        if related_no <= 0:
            break
        print(i['Text'])
        related_no-=1

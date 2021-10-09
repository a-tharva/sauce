"""Web search with selenium

This module opens new chrome window for image search and retuns result to file
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        #location of chrome driver
        driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options= inc)
        driver.implicitly_wait(0.5)

        #open google image search
        driver.get('https://images.google.com/')

        #find cam button
        cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()
        
        #input url 
        paste_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[1]/input")
        paste_url.send_keys(url)
        
        #click search button
        img_searc = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[2]/input")
        img_searc.click()

        time.sleep(2) #just in case
        
        #return websites result
        elems = driver.find_elements_by_class_name('yuRUbf')
        for i in elems:
            a = i.find_elements_by_tag_name("a")
            for _ in a:
                n = _.get_attribute('href')
                f.write(n+"\n\n")
                print(n)

    except Exception as e:
        print(error)




def wiki_that(search_term):
    
    import wikipedia
    
    wikipage = wikipedia.summary(search_term, sentences=50)
    print(f'{wikipage}\n\n')

































'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle

inc = webdriver.ChromeOptions()
inc.add_argument("--incognito")

url = input("Input the url for img search:")

driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options= inc)
driver.implicitly_wait(0.5)


with open('PrnList.data','rb') as _:
    Prn_list = pickle.load(_)

crnt_list = []

try:
    #open google image
    driver.get('https://images.google.com/')

    #find cam button
    cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
    cam_button.click()

    paste_url = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[1]/input")
    paste_url.send_keys(url)

    img_searc = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr/td[2]/input")
    img_searc.click()

    time.sleep(5)
    #print sites
    
    elems = driver.find_elements_by_tag_name('cite')
    for i in elems:
        print(i.text)
        
    elems = driver.find_elements_by_class_name('yuRUbf')
    for i in elems:
        a = i.find_elements_by_tag_name("a")
        for _ in a:
            print(_.get_attribute('href'))
    
    #save every link on page in new_list
    elems = driver.find_elements_by_tag_name("a")
    for i in elems:
        crnt_list.append((i.get_attribute('href')))
    
    #does not work for dynamic web pages 
    elems = driver.find_elements_by_class_name("yuRUbf")
    for i in elems:
        print(i.get_attribute('href'))
    print(list(set(crnt_list).intersection(Prn_list)))

except Exception as e:
    print(error)

'''
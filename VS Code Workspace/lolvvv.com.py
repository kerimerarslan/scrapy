from selenium import webdriver
import time

browser = webdriver.Chrome("D:\dev\chromedriver_win32\chromedriver.exe")

browser.get("https://www.youtube.com/watch?v=rFBeqxBGj4g")
browser.set_window_size(800,600)
browser.fullscreen_window()
browser.save_screenshot("D:\run\aliriza.png")

time.sleep(2)


#for link in range(0,200):
    #//*[@id="__next"]/div/main/div/table/tbody/tr[1]/td[2]/a/div[2]/div
    #browser.find_elements_by_css_selector("a[class='flex items-center space-x-1 justify-center sm:justify-start hover:text-primary']")[link].click()
   # time.sleep(1)
   # fileName = browser.find_element_by_class_name("flex flex-wrap divide-y sm:divide-y-0 sm:divide-x divide-white divide-opacity-10 bg-ground rounded-b border-b border-white border-opacity-10 mb-4")
    #runs = browser.find_element_by_css_selector("table[class='ui fixed unstackable very basic table']")
    #browser.save_screenshot("image.png")
    #runs = browser.find_element_by_xpath("//*[@id='root']/div/div[1]/div[7]")
    #with open("d:/run/"+fileName.text,"w", encoding="UTF-8") as file:
    #    file.write(str(runs))
    #browser.back()
    #time.sleep(1)
    


#browser.quit()
from selenium import webdriver
import time
from PIL import Image

#driver ı belirttik
browser = webdriver.Chrome("D:\dev\chromedriver_win32\chromedriver.exe")

#gideceğimiz sayfayı verdik 
browser.get("https://www.lolvvv.com/tr/champion")

#kaynak kodu aldık
#print(browser.page_source)
#print(browser.title)

#tam ekran yapma

#browser.get("https://www.lolvvv.com/tr/champion/Aatrox/rün?positions=TOP")

#pencere boyutu belirleme
#browser.set_window_size(600,400)
#time.sleep(2)
#screenshot alma
browser.save_screenshot("C:/Users/kerim/OneDrive/Masaüstü/image.png")

#browser.back()
for link in range(0,200):
    #//*[@id="__next"]/div/main/div/table/tbody/tr[1]/td[2]/a/div[2]/div
    browser.find_elements_by_css_selector("a[class='flex items-center space-x-1 justify-center sm:justify-start hover:text-primary']")[link].click()
    adi = browser.find_element_by_xpath("//*[@id='__next']/div/main/div/div[1]/div[3]/div/div[1]/h1")
    print("AGAGAGAGAGAAGAGAGGAGAGAGAGAGAGAAGAGAGAGAGAGAGAGA")
    
    print(adi.text)
    browser.set_window_size(3000,3000)
    #browser.execute_script('window.scrollTo(0,108)')
    fileName = browser.find_element_by_xpath("//*[@id='__next']/div/main/div/div[5]")
    #runs = browser.find_element_by_css_selector("table[class='ui fixed unstackable very basic table']")
    #deger = browser.find_element_by_xpath("//*[@id='__next']/div/main/div/div[5]/div[1]/div/div[5]/div[1]/div[1]/img")
   # print(str(deger))
    location = fileName.location
    size = fileName.size
    print(size)
    time.sleep(3)
    browser.save_screenshot("C:/Users/kerim/OneDrive/Masaüstü/kabiliyet/"+adi.text+".png")
   
    x = location['x']
    y = location['y']
    print("LOKASYONNNNNNNNNNNNNNNNNNNNNNNNN")
    print(location)
    width = location['x']+size['width']
    height = location['y']+size['height']
    
    im = Image.open("C:/Users/kerim/OneDrive/Masaüstü/kabiliyet/"+adi.text+".png")
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save("C:/Users/kerim/OneDrive/Masaüstü/kabiliyet/"+adi.text+".png")
    #fileName.screenshot('C:/Users/kerim/OneDrive/Masaüstü/image3.png')
    #runs = browser.find_element_by_xpath("//*[@id='root']/div/div[1]/div[7]")
   # with open("d:/run/"+"deger2","w", encoding="UTF-8") as file:
       # file.write(str(deger))
    browser.back()
    #time.sleep(1)

browser.quit()

import requests
from bs4 import BeautifulSoup

#tarayıcımızı girmemiz gerekiyor.(My user agent)
headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173"}

#alacağımız sitenin linkini ve tarayızımı parametre olarak veriyoruz.
glassdoor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm",headers=headers_param)

#siteye erişebiliyor muyuz ona bakmak için, 200 gelirse OK.
#print(glassdoor.status_code)sc

#sitenin içeriğini alıyoruz.
#print(glassdoor.content)

jobs = glassdoor.content

#parçalama yöntemini belirtiyoruz beautifulsoup un sitesinde diğerleride var
soup = BeautifulSoup(jobs,"html.parser")

#örn başlık çektik
#print(soup.title)

#örn h1 etiketleri arasındaki başıkları aradık "find" ile
#.text eklediğimiz zaman sadece yazıyı alıyoruz
#find_all dersek örn tüm h1 etiketlerini getiriyor
#print(soup.find("h1").text)

#bir parametre daha ekleyip mesela p etiketli, classı aşağıdaki olanları aldık.
all_jobs = soup.find_all("p",{"class":"h2 m-0 entryWinner pb-std pb-md-0"})

#bir döngü açarak tüm a etiketlerini aldık
#for job in all_jobs:
#    print(job.a.text)

all_data = soup.find_all("div",{"class":"col-6 col-lg-4 dataPoint"})

for data in all_data:
    print(data.text)


#author : Dr. JIMMY




import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest


linkslist = []
titleslist = []
summerylist = []
artcleslist = []
page_num = int(1)

while True:


    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    r =  requests.get(f"https://mobizil.com/news/page/{page_num}" , headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')
    page_limit = int(3)

    if (page_num > page_limit):
        print('pages ended')
        break


    div_container = soup.find('div', class_="col-sm-8 content-column")
    titles = div_container.find_all('h2' , class_='title')
    summury = div_container.find_all('div', class_='post-summary')



    for i in range(len(titles)):
        titleslist.append(titles[i].text.strip())
        summerylist.append(summury[i].text.strip())
        linkslist.append(titles[i].find('a').attrs['href'])

    page_num += 1
    print('page swithced')




for link in linkslist:
    r =  requests.get(link , headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')
    div_container2 = soup.find("div" , class_='col-sm-8 content-column')
    article = div_container2.find("div", class_='entry-content clearfix single-post-content')
    artcleslist.append(article.text.strip())



file_list = [titleslist , linkslist , summerylist , artcleslist]
exported = zip_longest(*file_list)



with open("mobizil.csv" , 'w', encoding='utf-8-sig') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["title" , "link" , 'summery' , "artice"])
    wr.writerows(exported)



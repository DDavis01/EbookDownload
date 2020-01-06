from bs4 import BeautifulSoup
import requests
import os
import wget

#LibGenURL = 'http://gen.lib.rus.ec/'
#Example URL = http://gen.lib.rus.ec/search.php?req=0133594149&open=0&res=25&view=simple&phrase=1&column=def


def search(BookInfo,InfoType):
    InfoType = 1
    ISBN = BookInfo[0]
    Name = BookInfo[1]
    Author = BookInfo[2]
    Year = BookInfo[3]
    if InfoType == 1:
        URL = 'http://gen.lib.rus.ec/search.php?req='+ISBN+'&open=0&res=25&view=simple&phrase=1&column=identifier'

    response = requests.get(URL)
    #print(response.text)
    html_soup = BeautifulSoup(response.text, 'lxml')
    links = []
    for a in html_soup.find_all('a', id=True):
        links.append(a['href'])
    #print(links)
    selectResponse = requests.get('http://gen.lib.rus.ec/'+links[0])
    select_html_soup = BeautifulSoup(selectResponse.text, 'lxml')
    select_links=[]
    for a in select_html_soup.find_all('a', title='Gen.lib.rus.ec'):
        select_links.append(a['href'])
    #print(select_links[0])
    return select_links[0]

def downloadBook(BookInfo,link):
    ip = link.split('/')
    response = requests.get(link)
    html_soup = BeautifulSoup(response.text, 'lxml')
    dl_link = html_soup.find('a',string='GET')
    bookLoc=dl_link['href']
    URL = 'http://'+ip[2]+bookLoc
    fileName = BookInfo[1]+".pdf"
    print(URL)
    filename = wget.download(URL)
    
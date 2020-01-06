from bs4 import BeautifulSoup
import requests
import wget
import csv
#LibGenURL = 'http://gen.lib.rus.ec/'
#Example URL = http://gen.lib.rus.ec/search.php?req=0133594149&open=0&res=25&view=simple&phrase=1&column=def


def search(BookInfo,InfoType):    #Function to parse a list "BookInfo" and extract from Lib Gen the download link of the top selection based off of ISBN
    ISBN = BookInfo[0]
    Name = BookInfo[1]
    Author = BookInfo[2]
    Year = BookInfo[3]
    if InfoType == 1:
        URL = 'http://gen.lib.rus.ec/search.php?req='+ISBN+'&open=0&res=25&view=simple&phrase=1&column=identifier'
    response = requests.get(URL)
    html_soup = BeautifulSoup(response.text, 'lxml')
    links = []
    for a in html_soup.find_all('a', id=True):
        links.append(a['href'])
    selectResponse = requests.get('http://gen.lib.rus.ec/'+links[0])
    select_html_soup = BeautifulSoup(selectResponse.text, 'lxml')
    select_links=[]
    for a in select_html_soup.find_all('a', title='Gen.lib.rus.ec'):
        select_links.append(a['href'])
    return select_links[0]

def downloadBook(BookInfo,link):    #Function to download book given BookInfo list and the designated link
    ip = link.split('/')
    response = requests.get(link)
    html_soup = BeautifulSoup(response.text, 'lxml')
    dl_link = html_soup.find('a',string='GET')
    bookLoc=dl_link['href']
    URL = 'http://'+ip[2]+bookLoc
    fileName = BookInfo[1]+".pdf"
    filename = wget.download(URL,out=fileName)
    
def parseBookInfo(CSV):
    with open(CSV, 'r') as f:
        reader = csv.reader(f)
        bookList = list(reader)
    #print(bookList)
    return(bookList)

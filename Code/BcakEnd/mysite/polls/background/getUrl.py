import requests
from bs4 import BeautifulSoup


def getUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text ,"lxml")
    pattern = soup.find(name='link', attrs={'itemprop': {'embedURL'}})
    ans = pattern['href']
    return ans

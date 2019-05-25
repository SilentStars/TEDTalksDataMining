import urllib
from bs4 import BeautifulSoup


def getImgURL(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')

    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all(itemprop="thumbnailUrl")
    imgURL = divs.pop(0)['content']

    return imgURL


from bs4 import BeautifulSoup as bs
import requests

def getInfo(main_page, num):
    info = []
    divs = main_page.find_all('div', class_='post-block__content', limit = num)

    for div in divs:
        info.append(div.text.strip())
    return info

def getHeadlines(article_box, num):
    sub_headers = []
    links = []
    
    main_page = getPage()
    divs = main_page.find('div', class_='river')
    headers = divs.find_all('a', class_='post-block__title__link', limit = num)
    
    for header in headers:
        sub_headers.append(header.text.strip())
        links.append(header.get('href'))

    return sub_headers, links

def getPage():
    url = 'https://techcrunch.com/'
    main_page = bs(requests.get(url).text, 'lxml-xml')
    return main_page

def tech_get_news(num):
    page = getPage()
    titles, links = getHeadlines(page, num)
    info = getInfo(page, num)

    return titles, links, info


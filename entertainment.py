from bs4 import BeautifulSoup as bs
import requests


def get_headlines(main_page):
    news_headlines = []
    headlines = main_page.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=5)
    for headline in headlines:
        news_headlines.append(headline.text.strip())
    return news_headlines

def get_links(main_page):
    news_links = []
    hrefs = main_page.find_all('a', class_='VDXfz', limit=5)
    for href in hrefs:
        news_links.append(href.get('href'))
    return news_links

def get_news():
    main_url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
    page = requests.get(main_url)
    main_page = bs(page.text, 'html.parser')
    headlines = get_headlines(main_page)
    links = get_links(main_page)

    return headlines, links

print(get_news())


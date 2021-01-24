from bs4 import BeautifulSoup as bs
import requests


def get_headlines(main_page, num):
    news_headlines = []
    headlines = main_page.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=num)
    for headline in headlines:
        news_headlines.append(headline.text.strip())
    return news_headlines

def get_links(main_page, num):
    news_links = []
    hrefs = main_page.find_all('a', class_='VDXfz', limit=num)
    for href in hrefs:
        news_links.append(href.get('href'))
    return news_links

def entertainment_get_news(num):
    main_url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
    page = requests.get(main_url)
    main_page = bs(page.text, 'html.parser')
    headlines = get_headlines(main_page, num)
    links = get_links(main_page, num)

    return headlines, links
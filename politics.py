from bs4 import BeautifulSoup as bs
import requests

#News headlines
def get_headlines(search_results):
    headlines = []
    news_headlines = search_results.find_all('h3', limit=5)
    for headline in news_headlines:
        headlines.append(headline.text.strip())
    return headlines

#News subheadlines
def get_subheadlines(search_results):
    subheadlines = []
    news_subheadlines = search_results.find_all('a', class_='text-link styles-text', limit=5)
    for subheadline in news_subheadlines:
        subheadlines.append(subheadline.text.strip())
    return subheadlines

#News links
def get_links(search_results):
    links = []
    news_links = search_results.find_all('a', class_=None, limit=5)
    for link in news_links:
        links.append(link.get('href'))
    return links

def get_news(place):
    url = 'https://www.worldpoliticsreview.com/search?query='
    search_query = place.lower()
    result_page = requests.get(url + search_query)
    news_page = bs(result_page.text, 'html.parser')
    search_results = news_page.find('div', id='search-results')
    headlines = get_headlines(search_results)
    subheadlines = get_subheadlines(search_results)
    links = get_links(search_results)

    return headlines, subheadlines, links


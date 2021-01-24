from bs4 import BeautifulSoup as bs
import requests

#News headlines
def get_headlines(search_results, num):
    headlines = []
    news_headlines = search_results.find_all('h3', limit=num)
    for headline in news_headlines:
        headlines.append(headline.text.strip())
    return headlines

#News subheadlines
def get_subheadlines(search_results, num):
    subheadlines = []
    news_subheadlines = search_results.find_all('a', class_='text-link styles-text', limit=num)
    for subheadline in news_subheadlines:
        subheadlines.append(subheadline.text.strip())
    return subheadlines

#News links
def get_links(search_results, num):
    links = []
    news_links = search_results.find_all('a', class_=None, limit=num)
    for link in news_links:
        links.append("https://www.worldpoliticsreview.com/" + link.get('href'))
    return links

#make a function to scrape from homepage without query

def politics_get_news(place, num):
    url = 'https://www.worldpoliticsreview.com/search?query='
    search_query = place.lower()
    result_page = requests.get(url + search_query)
    news_page = bs(result_page.text, 'html.parser')
    search_results = news_page.find('div', id='search-results')
    headlines = get_headlines(search_results, num)
    subheadlines = get_subheadlines(search_results, num)
    links = get_links(search_results, num)

    return headlines, subheadlines, links
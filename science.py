from bs4 import BeautifulSoup as bs
import requests

#Main article 
def main_news(news_page):
    main_image = news_page.find('img', class_='qa-srcset-image')
    main_image_link = main_image.get('src')
    main_headlines = news_page.find('h3', class_='gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text').text.strip()
    main_subheadlines = news_page.find('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary').text.strip()
    return main_image_link, main_headlines, main_subheadlines

#Sub-articles
#sub_images = news_page.find_all('img', class_='lazyloaded', limit=4)

def sub_headlines(news_page, num):
    side_titles = []
    sub_headlines = news_page.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text', limit=num)
    for subheadline in sub_headlines:
        side_titles.append(subheadline.text.strip())
    return side_titles

def sub_subheadlines(news_page, num):
    side_info = []
    sub_subheadlines = news_page.find_all('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@l', limit=num)
    for sub_subheadline in sub_subheadlines:
        side_info.append(sub_subheadline.text.strip())
    return side_info
    
    
def sub_links(news_page, num):
    href = []   
    sub_link = news_page.find_all('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor', limit=num)
    for link in sub_link:
        href.append("https://www.bbc.com/" + link.get('href'))
    return href

def science_daily_get_news(num):
    url = 'https://www.bbc.com/news/science_and_environment'
    page = requests.get(url)
    news_page = bs(page.text, 'html.parser')
    if num == 1:   
        main_image_link, main_headlines, main_subheadlines = main_news(news_page) 
        return main_image_link, main_headlines, main_subheadlines, [], [], []
        
    main_image_link, main_headlines, main_subheadlines = main_news(news_page)    
    side_titles = sub_headlines(news_page, num - 1)
    side_info = sub_subheadlines(news_page, num - 1)
    href = sub_links(news_page, num - 1)

    return main_image_link, main_headlines, main_subheadlines, side_titles, side_info, href

def science_get_news(keyword, num):
    #get news from a search page with a keyword query
    #get article name, subhead if applicable, possible image link. and link to article
    pass
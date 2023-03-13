# in this file we take a key word and return the list of all the urls in that pageimport requests
import requests
import urllib
import sys
from requests_html import HTML
from requests_html import HTMLSession


def main():
    listed = scraping("hello")
    for item in listed:
        print(item)


def scraping(keyword):
    keyword = urllib.parse.quote_plus(keyword)
    try:
        session = HTMLSession()
        responce = session.get("https://www.google.com/search?q=" + keyword)
    except:
        print("Something went wrong")
        sys.exit()

    links = list(responce.html.absolute_links)

    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links


if __name__ == "__main__":
    main()

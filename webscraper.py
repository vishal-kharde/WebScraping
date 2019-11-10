import requests
from readability import Document  #pip install readability-lxml     Given a html document, it gives main body text.
from bs4 import BeautifulSoup
import urllib

#gives the news article body text
def get_article_content(str):
    response = requests.get(str)
    doc = Document(response.text)
    soup = BeautifulSoup(doc.summary(), "lxml")
    text = soup.get_text()
    return text

print (get_article_content("https://www.livemint.com/money/personal-finance/sbi-new-fd-rates-from-today-check-out-the-latest-rates-here-11573196043178.html"))

# following code is for google search, need some tweaking though
query = "'fake news'"
query = urllib.parse.quote_plus(query) # Format into URL encoding
number_result = 10
#url = 'https://google.com/search?q=' + searchstring
google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)

response = requests.get(google_url)

soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify())
for g in soup.find_all("div",class_="kCrYT"):
    aa= g.find('a')
    if aa is not None and 'href' in aa.attrs:
        l = aa.get('href')
        print(l)

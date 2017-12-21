# import libraries
import urllib2
from bs4 import BeautifulSoup
# url to visit
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
# use urllib2 to open the quote_page
page = urllib2.urlopen(quote_page)
# use beautiful soup to parse the html and store to variable soup
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip()

print name

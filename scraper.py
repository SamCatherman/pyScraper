# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# url to visit
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
# use urllib2 to open the quote_page
page = urllib2.urlopen(quote_page)
# use beautiful soup to parse the html and store to variable soup
soup = BeautifulSoup(page, 'html.parser')
# find all h1 tags in the element with the class 'name'
name_box = soup.find('h1', attrs={'class': 'name'})
# use strip() method to remove starting and trailing tags
name = name_box.text.strip()
#variable to hold the ticker
ticker_box = soup.find('div', attrs={'class': 'ticker'})
ticker = ticker_box.text.strip()

price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text


#print variables
print name
print ticker
print price

#open csv file with append, keeping old data
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, ticker, price, datetime.now()])

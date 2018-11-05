import requests
import bs4

res = requests.get('http://www.mypinoyblogger.com')
scrap = bs4.BeautifulSoup(res.text, 'lxml')
get_title = scrap.select('title')[0].getText()

print('Site Title', get_title)

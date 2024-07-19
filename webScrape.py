from bs4 import BeautifulSoup
import requests

sourceCode = requests.get('https://www.rmit.edu.au/').text
htmlCode = BeautifulSoup(sourceCode, 'lxml')
article = htmlCode.find('p', class_ = 'short-desc-gen').text
# print(article.find('div', class_ = 'row cmp-list'))
print(article)


from bs4 import BeautifulSoup
import requests

sourceCode = requests.get('https://www.rmit.edu.au/').text
htmlCode = BeautifulSoup(sourceCode, 'lxml')
article = htmlCode.find('article')
print(article.div.a)


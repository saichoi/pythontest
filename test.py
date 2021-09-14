import requests
from bs4 import BeautifulSoup
    
uri = '''
https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=0&acr=1&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8
'''

response = requests.get(uri)
soup = BeautifulSoup(response.text, 'html.parser')
temp = soup.select_one('.todaytemp')
tempDict = dict(zip(*temp))

#print(temp.text)
print(tempDict)
import requests, json
from bs4 import BeautifulSoup 

class SearchOffer:

    def __init__(self,keyword , language ='fa'):
        self.keyword = keyword
        self.headers = {'User-agent':'Mozilla/5.0'} 
        self.offer_keyword = []
        self.language = language
    def soup(self,url):
        req = requests.get(url, headers = self.headers)
        soup = BeautifulSoup(req.content,'html.parser')
        return soup

    def offer(self):
        URL = f"http://suggestqueries.google.com/complete/search?output=toolbar&hl={slef.language}&q={self.keyword}"   
        soup = self.soup(URL).find_all('suggestion')
        data = [data['data'] for data in soup]
        return data
    def google(self):
        return self.offer()


    
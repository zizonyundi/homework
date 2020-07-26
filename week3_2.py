import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#regularTeamRecordList_table > tr')
# 아래 빈 칸('')을 채워보세요
for tr in trs:
    name = tr.select_one('td.tm > div').text.strip()
    scores = tr.select_one('td:nth-child(7)').text.strip()

    def get_score(tr, trs) :
        for score in scores :
            if score < 0.5
                return score
    print (get_score())

#regularTeamRecordList_table > tr:nth-child(1) > td.tm > div
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(4)
#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(7)
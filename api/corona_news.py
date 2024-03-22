from flask_restful import Resource
from flask import make_response
from Backend.model.corona_news_crawling import corona_news
import json

class Corona(Resource):
    def get(self):
        articles = corona_news()
        news_dict=[]
        for link,imageUrl,title,summary,date in articles:
            news_dict.append({'link':link,'imageUrl':imageUrl,'title':title,'summary':summary[:150]+'...','date':date})

        return make_response(json.dumps(news_dict,ensure_ascii=False))
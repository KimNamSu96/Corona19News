from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#네이버 속보 뉴스 서비스
from api.corona_news import Corona

#플라스크 앱 생성
app = Flask(__name__)
#CORS에러 처리
CORS(app)
api = Api(app)

api.add_resource(Corona, '/corona')

if __name__ == '__main__':
    app.run(debug=True)
# flask : html 응답을 동적으로 생성 및 전달하기 위한 프레임워크
# Routing : 요청을 함수와 연결해주는 기술

from flask import Flask

app = Flask(__name__)

# 일반적인 Web Framework에서 데이터는 Data Base에 저장함
topics = [
    {'id': 1, 'title': 'html', 'body': 'html body'},
    {'id': 2, 'title': 'css', 'body': 'css body'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript body'}
]

def templete(contents, content):
    return f'''<doctype html>
    <html>
        <head>
        </head>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {contents}
        </ol>
        {content}
        </body>
    </html>
    '''

# 기본 페이지 라우팅
# return값이 화면에 표시됨
@app.route('/')
def index():
    liTags = ''
    # 동적으로 url 생성
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return templete(liTags, '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')   # 같은 이름(id)의 파라미터로 값 전달
def read(id):
    liTags = ''
    title = ''
    body = ''
    # 동적으로 url 생성
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    for topic in topics:
        if topic["id"] == id:
            title = topic['title']
            body = topic['body']
            break
    return templete(liTags, f'<h2>{title}</h2>{body}')

# 생성 페이지 라우팅
@app.route('/create/')
def create():
    return 'Create'

if __name__ == '__main__':
    app.run(port=5001, debug=True)
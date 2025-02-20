# flask : html 응답을 동적으로 생성 및 전달하기 위한 프레임워크
# Routing : 요청을 함수와 연결해주는 기술

from flask import Flask, request, redirect


app = Flask(__name__)

nextId = 4
# 일반적인 Web Framework에서 데이터는 Data Base에 저장함
topics = [
    {'id': 1, 'title': 'html', 'body': 'html body'},
    {'id': 2, 'title': 'css', 'body': 'css body'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript body'}
]

def templete(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
        '''
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
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    # 동적으로 url 생성
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

# 기본 페이지 라우팅
# return값이 화면에 표시됨
@app.route('/')
def index():
    getContents()
    return templete(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/read/<int:id>/')   # 같은 이름(id)의 파라미터로 값 전달
def read(id):
    title = ''
    body = ''
    getContents()

    for topic in topics:
        if topic["id"] == id:
            title = topic['title']
            body = topic['body']
            break
    return templete(getContents(), f'<h2>{title}</h2>{body}', id)

# 생성 페이지 라우팅
@app.route('/create/', methods=['GET', 'POST'])
def create():
    # print('request.method', request.method)
    if request.method == 'GET':  
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p> 
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return templete(getContents(), content)

    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId += 1
        return redirect(url)

# 수정 페이지 라우팅
# 직전 create 항목 update 가능
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if topic["id"] == id:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p> 
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return templete(getContents(), content)

    elif request.method == 'POST':
        # global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if topic['id'] == id:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
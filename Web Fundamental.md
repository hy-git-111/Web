# Web
## 정적 웹, 동적 웹
* 브라우저  
: HTML 문서나 파일을 출력하는 SW

* 정적 웹  
: html 변동시 서버에서 html 업데이트 필요(새로고침)  
사용자 정보 초기화됨

* 동적 웹  
: html 변동이 있을때 Javascript로 변동된 부분에 대한 데이터만 업데이트(랜더링, 새로고침 불필요)    
사용자 정보 유지됨

* SPA, Single Page Application  
여러 페이지가 있지만, 연동 등의 기술을 이용하여 하나의 페이지만 존재하는것처럼 동작하는 프레임워크
    > <span style="color:darkgray">**SPA가 동적 웹을 만들어줌 > js로 html을 구현함**</span>

    > <span style="color:darkgray">**Front End  
    : SPA를 이용해서 화면단을 개발하는 사람**</span>

<br/>

## 웹 주소
* URI(Uniform Resource Identifier, 통합 자원 식별자)  
    * URL의 상위 버전  
    * 서버에서 특정 리소스를 구별하기 위한 식별자

* URN(Uniform Resource Name)
    * 이름으로 리소스를 특정하는 URI

* URL(Uniform Resource Locator)
    * 웹 페이지를 고유하게 식별할 수 있는 주소
    * 구조 : 프로토콜 + 도메인 + url 경로 + 쿼리 
     
[URI/URL/URN 참고자료] https://velog.io/@younoah/uri-url-urn

<br/>

## 웹 프로토콜(Protocol, 통신 규약)
* Json : 데이터 전송 시 주로 사용
* XML : 데이터 저장, 전달, 교환 시 사용
* HTML : HTTP에 응답하는 방식, 웹 프로토콜
* HTTP

    * http(Hyper Text Transform Protocol)
        * http 1.1 : 1요청 1응답의 원칙을 가진다.
        * http 메소드(행위)
            * GET : 페이지 정보, 데이터 조회 요청
            * POST : 저장할 정보 전달 > 정보 "생성" 요청, 보안사항이 있는 데이터의 전달
            * PUT, PATCH : 기존에 저장된 정보 수정 요청
            * DELETE : 저장된 정보 삭제

    * https(Hyper Text Transform Protocol Secure)
        * 기기, 운영체제, 브라우저에 상관없이 통신할 수 있는 방식

        > <span style="color:darkgray">**http를 꼭 알아야 하는 이유!  
        통신방식을 알면 응답값에 대한 파악 가능(4xx, 5xx..)  
        개발자 도구를 통해 http 통신 기록 확인 가능  
        결함 공유 시 오류코드 전달 가능**</span>

<br/>

## Web 통신 구조
* 클라이언트(FE) : 서버 기능과 무관하게 단독적인 기능들의 집합
    * UI/UX 구성
    * 서버에 요청하기 위한 통신 기능 탑재

* WAS, Web Application Server : 클라이언트와 BE 사이에서 통신을 돕는 서버

* Backend : 동작코드, 기능의 동작인 비즈니스 로직을 처리하는 부분
    * 비즈니스 로직 : 입력된 데이터를 저장하기 위해 가공하는 것

* DB : 데이터의 집합

<br/>

## web 구성
* HTML, HyperText Markup Language  
    * 웹페이지의 구조화를 위한 마크업 언어(텍스트를 붙이는 언어)
    * 태그를 이용하여 요소를 표시하고 구성함

        > <span style="color:darkgray">**http : html 전송을 위한 프로토콜  
        HyperText : 웹사이트에서 링크를 통해 다른 사이트로 즉시 이동하는 기능  
        Markup : 태그를 사용해 문서에 의미를 표시하는 것**
        </span>

* CSS, Cascading Style Sheet  
: 웹 페이지 디자인을 위한 언어  
    > <span style="color:darkgray">**Selenium에서 요소를 식별할 떄 CSS Selector 사용**</span>

    * Bootstrap  
    : CSS 라이브러리

* JS, JavaScript
: 웹페이지의 동적 요소 추가를 위한 언어

<br/>

# HTML
## HTML 구조
* DOCTYPE
* html
* head
* body

예시 코드
```html
<!DOCTYPE html> // html5 문서임을 선언
<html lang="en">
    <head>
        <meta charset="UTF-8">  // 인코딩 형식
        <title>Document</title> // 웹페이지 제목
    </head>
    <body>
    // 웹 페이지의 실제 내용 작성
    </body>
</html>
```

<br/>

## HTML 태그
### 기본 문법
```html  
<태그 속성="속성값">콘텐츠</태그>
```

* self-closing tags  
: 닫는 태그가 필요하지 않은 태그

    self-closing tags 예시
    ````html
    <br/> : 줄바꿈
    <input/> : 입력창
    <img/> : 이미지 삽입
    ````
    <!-- img태그 사용 예시
    ```html
    <img src="url또는 파일 경로" alt="대체텍스트"/>
    ``` -->

* 컨테이너  
: 요소를 묶어서 레이아웃 구조화

    * Block 수준의 컨테이너 요소  
    : 줄바꿈을 통해 행 단위로 스타일 적용 가능  

        Block element 예시  
        ````html
        <div></div> : 행바꿈
        ````

    * Inline 수준의 컨테이너 요소  
    : 줄바꿈 없이 일부 텍스트만 스타일 적용 가능  

        Inline element 예시 
        ````html
        <span></span>
        ````    

<br/>

### 자주 사용하는 태그
* h 태그  
    ````html
    <h1></h1>
    ````
    예제
    ````
    <h1>제목 태그</h1>
    <h2>제목 태그</h2>
    <h3>제목 태그</h3>
    <h4>제목 태그</h4>
    <h5>제목 태그</h5>
    <h6>제목 태그</h6>
    ````
    출력
    <h1>제목 태그</h1>
    <h2>제목 태그</h2>
    <h3>제목 태그</h3>
    <h4>제목 태그</h4>
    <h5>제목 태그</h5>
    <h6>제목 태그</h6>

<br/>

* p 태그  
    ````html
    <p></p>
    ````
    예제
    ````html
    <p>내용1</p>
    <p>내용2</p>
    ````
    출력  
    <p>내용1</p>
    <p>내용2</p>

<br/>

* a 태그  
    ````html
    <a href="url" target="속성값에 따라 현재 탭/새 탭에서 실행">텍스트</a>
    ````
    * target 속성값  
    _blank : 새로운 탭에서 열기  
    _self : 현재 탭에서 열기(default)

    예제
    ````html
    <a href="https://www.naver.com/" target="">현재 탭에서 네이버 열기</a>  
    <a href="https://www.naver.com/" target="_blank_">새 탭에서 네이버 열기</a>
    ````
    출력  
    <a href="https://www.naver.com/" target="">현재 탭에서 네이버 열기</a>  
    <a href="https://www.naver.com/" target="_blank_">새 탭에서 네이버 열기</a>

<br/>

* 목록 태그와 요소  
    ````html
    <ul></ul> : Unoldered List
    <ol></ol> : Oldered List
    <li></li> : List
    ````
    예제
    ````html
    <ul>
    <li>item</li>
    <li>item</li>
    </ul>

    <ol>
    <li>item</li>
    <li>item</li>
    </ol>

    ````
    출력
    <ul>
    <li>item</li>
    <li>item</li>
    </ul>
    
    <ol>
    <li>item</li>
    <li>item</li>
    </ol>

<br/>

* table 태그와 요소
    ````
    <table></table> : Table 생성
        * 속성
        border : 테두리 선 굵기

    <tr></tr> : Table Row
    <th></th> : Table Header
    <td></td> : Table Data
    ````
    > <span style="color:darkgray">**테이블 생성 : CSS를 이용하는 것보다 간단함  
    테두리 등 속성 설정 : 주로 CSS 이용**</span>

    예제
    ````html
    <table border="1">
        <tr>
            <th>속성1</th>
            <th>속성2</th>
        </tr>
        <tr>
            <td>값1</td>
            <td>값2</td>
        </tr>
    </table>
    ````
    출력
    <table border="1">
        <tr>
            <th>속성1</th>
            <th>속성2</th>
        </tr>
        <tr>
            <td>값1</td>
            <td>값2</td>
        </tr>
    </table>

<br/>

* form 태그와 요소
    ````html
    <form></form> : form 생성
        * 속성
            method : 서버로 데이터를 전송하기 위한 메소드  
                GET : 주소 표시줄에 사용자 입력 데이터 노출
                POST : 주소 표시줄에 사용자 입력 데이터 비노출
            name : 한 문서 내에 form 태그가 여러개 사용될 수 있음.
                이를 위해 form 구분을 위한 키(key)로 사용됨.
            action : 데이터를 전송할 서버와 연결되는 주소(URL, script 파일명 등)

    <label></label> : 요소에 레이블(라벨) 지정
        * 속성
        for : 입력 요소의 id값

    <input/> : 한 줄 입력 가능한 입력필드
        * 속성
            type : text, url, radio, submit 등
            name : input 구분을 위한 Key
            placeholder : 입력값 예시            

    <textarea></textarea> : 여러 줄 입력 가능한 입력필드
        * 속성
        name : textarea 구분을 위한 Key
        placeholder : 입력값 예시
        clos : 행 크기 제어
        rows : 열 크기 제어
    ````

    > <span style="color:darkgray">**form 태그는 다른 언어와 연동하여 사용(js, React SPL)  
    label 태그가 입력 요소와 연결될 경우 입력 요소 활성화됨**</span>

    예제
    ````html
    <form>
        <label for="inputId">input:</label>
        <input
        type="text"
        id="inputId"
        name="text1"
        placeholder="텍스트를 입력해 주세요."
        />
        <br/><br/>
        <label>textarea:</label>
        <textarea
            name="content"
            placeholder="텍스트를 입력해 주세요."
            cols="20"
            rows="5"
        ></textarea>
    </form>
    ````
    출력
    <form>
        <label for="inputId">input:</label>
        <input
        type="text"
        id="inputId"
        name="text1"
        placeholder="텍스트를 입력해 주세요."
        />
        <br/><br/>
        <label>textarea:</label>
        <textarea
            name="content"
            placeholder="텍스트를 입력해 주세요."
            cols="20"
            rows="5"
        ></textarea>
    </form>

<br/>

* Semantic 태그  
: 컨테이너 태그이지만 각 요소의 역할과 의미를 예측 가능하도록 하는 태그  
SW 완성도와 관련됨  
검색엔진 최적화(SEO, Search Engine Potimization)를 위해 사용

    ````html
    <header></header>
    <nav></nav> : 내비게이션 링크
    <section></section> : 구역 분할
    <main></main>
    <aside></aside>
    <article></article> : 문서 내 독립적인 콘텐츠
    <footer></footer>
    ````

    > <span style="color:darkgray">**semantic을 사용하지 않으면 div 태그로 레이아웃 구현 가능**</span>

<br/>

# 선택자(Selector)
* 전역 속성   
: 모든 html에서 사용할 수 있는 공통 속성

* 선택자  
: CSS로 속성을 부여할 대상을 뜻함
    * id
    : 고유 식별자로 요소 식별을 위해 사용

    * class
    : 여러 요소에 동일한 스타일 적용을 위해 동일한 클래스 할당  
    다중 할당 시 공백으로 구분 

* 선택자 이름 입력 규칙
    * 대소문자 구분
    * 공백, 특수문자 포함 불가
    * 숫자나 문자로 시작, 숫자로만 이루어질 수 없음 

    사용 예시
    ```html
    <head>
        <style>
            /* class 선택자 */
            .class1{    

            }
            /* class 선택자 */
            .class2{

            }
            /* id 선택자 */
            #id1{

            }
        </style>
    </head>
    <body>
        <div class="class1 class2">요소 1</div>
        <div class="class1">요소 2</div>
        <div id="id1">요소 3</div>
    </body>
    ```



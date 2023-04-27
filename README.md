# 삼쩜삼 과제 제출용 레퍼지토리

## 환경설정(https://rswm-ju.tistory.com/2 참고)
1. 파이썬 설치
- www.python.org
2. 비쥬얼 스튜디오(VS) code 를 설치
- https://code.visualstudio.com/ 
3. 사각형 모양의 확장 기능 아이콘을 클릭(Extensions)
- python 검색 후 install
- Python Extension Pack 검색 후 install
4. 터미널에서 하단의 "엑셀 데이터 크롤링을 하기 위해 필요한 라이브러리" 차례대로 설치 
- pip install requests
- pip install BeautifulSoup4
- pip install openpyxl

## 엑셀 데이터 크롤링을 하기 위해 필요한 라이브러리(설치 필요)
- Requests : 웹사이트 url을 인식시킴으로써 데이터를 요청하고, 요청한 데이터를 받아 활용할 수 있도록 함 
(pip install requests)

- BeautifulSoup : Requests를 이용해 데이터를 요청한 후, HTML 소스 코드를 가져올 수 있다. HTML코드를 인식시켜 원하는 데이터를 선택하고 수집할 수 있는 파싱을 할 수 있도록 함
(pip install BeautifulSoup)

- Openpyxl : 파이썬에서 엑셀을 다를 수 있음 
(pip install openpyxl)

## 실행 매뉴얼
1. 삼쩜삼_네이버뉴스_과제.py 클릭
2. GitHub 화면에서 [Raw] 버튼을 마우스 오른쪽 버튼으로 클릭
3. '다른 이름으로 링크 저장' 선택
4. VSCODE 실행 후 터미널에서 저장된 위치로 이동 후 "python 삼쩜삼_네이버뉴스_과제.py" 입력 후 엔터
5. 검색어를 입력해달라는 text가 나타나면 "삼쩜삼" 입력 후 엔터
6. py파일과 같은 위치에 csv 형태의 파일이 생성

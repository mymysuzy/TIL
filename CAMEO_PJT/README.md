# 🙋🏻‍♀️ Briefing

[카카오맵](https://map.kakao.com/)을 사용하여 카페의 `이름`, `주소`, `전화번호` 등을 가져오는 `Scraping작업`을 진행했습니다.



`CafeInfoScraping.py`는 보편적으로 사용한 스크래핑 파일이며

`CafeInfoScraping_AfterErrorOccurred.py`는 `CafeInfoScraping.py`를 사용해서 스크래핑을 하던 도중 Error로 인해 스크래핑이 멈추게 되어 다시 시작할 경우에 사용한 파일입니다.

<br>

# 👩🏻‍💻💻 Before a start

>  스크래핑을 진행하기 위해선 **아래의 작업**이 선행되어야 합니다.

<br>

### 1. Chrome 버전 확인
   
   <br>
   
   <img src="https://user-images.githubusercontent.com/74548646/129755322-993ce996-28ab-4330-a6e6-95a3fa2fdb4c.png" alt="다운로드" width="70%" height="70%" />
   
   <br>
   
### 2. [Chrome Drivers](https://chromedriver.chromium.org/downloads) 웹페이지에 접속해 Chrome 버전과 같은 드라이버로 다운로드한다.
<td>
   &nbsp; &nbsp; 이때, Selenium을 돌릴 파일과 같은 경로에 다운로드하여야 한다.
   
   <br>
   <br>

   <img src="https://user-images.githubusercontent.com/74548646/129755543-3c5a7ece-6cac-4bb5-889a-7c97902b405d.png" alt="다운로드"  width="70%" height="70%" />
   
   <br>
   
### 3. CafeInfoScraping.py를 켜고 **원하는 검색어**를 71번째 줄의 `elem.send_keys`에 넣어준다.
   
   <br>
   
### 4. 그리고 **몇 페이지까지 스크래핑** 해주고 싶은지 471번째 줄의 `final`에 지정해준다.


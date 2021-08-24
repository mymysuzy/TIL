import pymysql
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 각 PC마다 상이한 user_agent값을 넣어주자.
# http://m.avalon.co.kr/check.html 사이트에 들어가면 알 수 있다.
# -------------------------------------------------------------
# 각 국가별로 보여지는 웹페이지 HTML이 조금씩 다를 수 있다. 디폴트는 보통 미국용 웹페이지가된다.
# 따라서 사전에 정확히 하기 위해 한국에서 크롬을 쓰고 있다는 것을 명시해주어야 개발자모드로 보았을 때의 엘리먼트를 그대로 사용할 수 있다.
# 이럴 때 사용할 수 있는 속성은 user_agent!
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"

franchise = [
    '스타벅스',
    '투썸플레이스',
    '메가커피',
    '이디야',
    '빽다방',
    '할리스',
    '파스쿠찌',
    '폴바셋',
    '엔제리너스',
    '커피빈',
    '커피나무',
    '달콤커피',
    '탐앤탐스',
    '커피베이',
    '더착한커피',
    '카페베네',
    '커피에반하다',
    '커피명가',
    '만랩커피',
    '셀렉토커피',
    '매머드커피',
    '드롭탑',
    '커피스미스',
    '커피마마',
    '토프레소',
    '더카페',
    '전광수커피',
    '빈스빈스',
    '그라찌에',
    '카페보니또',
    '공차',
    '데이하우스',
    '컴포즈커피',
    '청자다방',
    '벌크커피',
    '카페코지',
    '케냐에스프레소',
    '니나에스프레소',
    '허니밀브런치카페',
    '에쏠로지',
    '카페온화',
    '카페굴리엘모커피',
]

# "User-Agent": user_agent : 위에서 정의해준 user_agent값을 headers에 지정해주자.
# "Accept-Language": "ko-KR,ko": 만약 한국어로된 웹페이지라면 그걸로 줘! 아님 말고
headers = {
    "User-Agent": user_agent,
    "Accept-Language": "ko=KR,ko"
}

# 사전에 설치해준 Chrome Driver
options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

# 스크래핑에 사용하고 싶은 페이지
browser.get("https://map.kakao.com/")

# "검색창"의 HTML상 id값은 search.keyword.query
# 따라서 find_element_by_id를 사용하여 해당 id값을 찾아준다.
elem = browser.find_element_by_id("search.keyword.query")

# 검색창에 넣고 싶은 검색어를 지정해준다.
elem.send_keys("광주광역시 북구 카페")

# 검색을 시작할 수 있도록 Enter 쳐준다.
elem.send_keys(Keys.ENTER)

# BeautifulSoup 실행
soup = BeautifulSoup(browser.page_source, "html.parser")
time.sleep(5)

# 검색결과의 아래쪽에 보면 보이는 "더보기" 버튼 찾고, 클릭
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.ID, "info.search.place.more")))
elem.send_keys('\n')
time.sleep(5)

# 더보기 버튼을 클릭하여 다음 페이지로 넘어가면 1, 2, 3, 4, 5의 Page Nation이 보인다.
# 현재는 1, 2, 3, 4, 5의 Page Nation이 보이는 중.
# 내가 스크래핑을 시작하고 싶은 페이지는 25페이지 부터 34페이지기 때문에 다음의 Page Nation이 보이도록 넘어가자.
# 6, 7, 8, 9 , 10 페이지로 이동
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "info.search.page.next")))
elem.send_keys('\n')

time.sleep(3)

# 현재는 6, 7, 8, 9 , 10의 Page Nation이 보이는 중.
# 11, 12 ,13, 14, 15 페이지로 이동
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "info.search.page.next")))
elem.send_keys('\n')
time.sleep(3)

# 현재는 11, 12 ,13, 14, 15의 Page Nation이 보이는 중.
# 16, 17, 18, 19, 20 페이지로 이동
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "info.search.page.next")))
elem.send_keys('\n')
time.sleep(3)

# 현재는 16, 17, 18, 19, 20의 Page Nation이 보이는 중.
# 21, 22, 23, 24, 25 페이지로 이동
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "info.search.page.next")))
elem.send_keys('\n')
time.sleep(3)

# 현재는 21, 22, 23, 24, 25의 Page Nation이 보이는 중. 내가 스크래핑을 원하는 25페이지가 보인다!
# info.search.page.no5를 통해 25페이지를 선택.

# no5의 의미는 총 5개의 페이지 번호로 나눈 것 중 5번째라는 의미
# 즉, 22페이지는 no2
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.ID, "info.search.page.no5")))
elem.send_keys('\n')


# 이전 까지의 페이지
final = 24
# 이제 스크래핑을 시작 하고 싶은 시작 페이지
Page = 25


def scrap():
    global Page, final
    final += 1

    if 5 <= Page:
        # 브라우저 안에서 5초동안 기다린다.
        # info.search.page.next를 가진 id 태그를 찾을 때 까지 기다린다.
        # 찾으면 elem으로 가져온다.
        elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, f"info.search.page.next")))
        Page = 1

    else:
        Page += 1
        elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, f"info.search.page.no{Page}")))

    elem.send_keys('\n')
    time.sleep(3)

    # BeautifulSoup가 현재 브라우저가 가지고 있는 source를 가지고와서 html로 파싱
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # "상세보기" 버튼의 elem를 전부 가져오기
    elems = browser.find_elements_by_class_name("moreview")

    for elem in elems:
        # 상세보기 링크 존재하면 클릭
        if elem.get_attribute("href"):

            browser2 = webdriver.Chrome(options=options)

            # selenium이 해당 링크로 이동
            browser2.get(elem.get_attribute("href"))
            time.sleep(3)

            # BeautifulSoup가 현재 브라우저가 가지고 있는 source를 가지고와서 html로 파싱(가져오기)
            soup = BeautifulSoup(browser2.page_source, "html.parser")

            # 우리가 받아오려는 총 7개의 데이터 중 6개 받아오기
            Form = [None] * 6
            # 그 중 나머지 1개인 url은 아래와 같이 받아옴.
            Form.append(elem.get_attribute("href"))

            # flag가 0이면 프랜차이즈
            # flag가 1이면 동네카페
            flag = 0
            try:
                # 애견카페, PC 카페, 스터디 카페, 키즈카페는 제외시키려고 "카페", "디저트 카페", "커피전문점"만 받아온다.
                cls = soup.find("span", attrs={"class": "txt_location"}).text
                if cls == "분류: 카페" or cls == "분류: 디저트카페" or cls == "분류: 커피전문점":
                    flag = 1
            except:
                pass
            # 상세보기에서 없는 경우도 있어서 계속 try, except로 처리 중
            try:
                # 카페의 이름을 가져와서 name에 저장
                name = soup.find(
                    "h2", attrs={"class": "tit_location"}).get_text()
                # 프랜차이즈 리스트를 하나씩 뽑아서 카페 이름에 프랜차이즈 이름이 포함된 가게면 flag를 다시 0으로 만들어 준다.
                for i in franchise:
                    if i in name:
                        flag = 0
                        break
            except:
                browser2.close()
                continue
            # 프랜차이즈거나 우리가 원하는"카페"가 아닐 경우 브라우저 종료
            if flag == 0:
                browser2.close()
                continue

            # 0번째 form에 name 추가
            Form[0] = name

            try:
                updated_date = soup.find(
                    "span", attrs={"class": "date_revise"})
                # 1번째 form에 updated_date 추가
                Form[1] = updated_date.get_text()
            except:
                pass
            try:
                address_origin = soup.find(
                    "span", attrs={"class": "txt_address"}).get_text()
                address = ""
                # \n, \t 와 같은 요소들 제거해주고 다시 문자열 합체
                for i in address_origin.split():
                    address += (i + ' ')
                Form[2] = address
            except:
                pass
            try:
                homepage = soup.find(
                    "a", attrs={"class": "link_homepage"})["href"]
                Form[3] = homepage
            except:
                pass

            try:
                telephone = soup.find(
                    "span", attrs={"class": "txt_contact"}).get_text()
                Form[4] = telephone
            except:
                pass

            try:
                # frame_g를 가지고 오기 전 까지 브라우저에서 대기
                # frame_g는 해당 카페이름을 클릭했을 때 보이는 첫 번째 대문 사진.
                # 찾으면 click
                WebDriverWait(browser2, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
                time.sleep(3)

                # image 하나만 넣으려고 1로 설정
                image_len = 1
                temp = ''
                # frame_g를 클릭하면 보이는 이미지들의 링크(link_item)를 가지고 온다.
                image_list = browser2.find_elements_by_class_name("link_item")

                # 많은 이미지들 중 첫 번째 이미지만 저장해주자.
                for image in image_list:
                    image.click()
                    elem = WebDriverWait(browser2, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
                    # 첫 번째 image의 src를 get
                    temp = elem.get_attribute("src")

                    # 만약 이미지의 이름 길이가 300을 넘어가면 받아오지 말자.
                    # DB에 image varchar(300)으로 지정되어있기 때문에 넘어가면 에러 내뱉으며 스크래핑 종료되기 때문.
                    if len(temp) >= 300:
                        temp = None

                    # 이미지 1개 저장했으니 break
                    if image_len == 1:
                        break

                # 받아온 image를 5번째 form에 저장
                Form[5] = temp

            except:
                pass

            # 어떤 데이터를 스크래핑에 성공했는지 cmd창에서 보여주려고 print함
            print(Form)

            # 사전에 정의해두었던 store_list 리스트에 방금 스크래핑한 Form 리스트를 저장.
            # DB에 넣기 알맞은 형태로 만들어 졌다!
            store_list.append(Form)

        # 브라우저 종료
        browser2.close()


store_list = []

while True:

    # scrap 메서드 실행!
    scrap()

    # scrap 메서드가 종료된 후 얻은 데이터를 DB와 연결해 넣자.
    # EC2의 DB와 연결
    connect = pymysql.connect(host='i5c202.p.ssafy.io', user='root',
                              password='ssafy', db='CAMEO', charset='utf8mb4')
    cursor = connect.cursor()

    for r in store_list:
        cafe_name = str(r[0])
        updated_date = str(r[1])
        address = str(r[2])
        homepage = str(r[3])
        telephone = str(r[4])
        image = str(r[5])
        url = str(r[6])

        sql = """insert into cafe
        (cafe_name, updated_date, address, homepage, telephone, image, url)
        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """ % (cafe_name, updated_date, address, homepage, telephone, image, url)

        cursor.execute(sql)
        connect.commit()

    connect.close()
    store_list = []

    print(f'{final} 페이지의 크롤링이 끝났습니다.')

    # 내가 몇 페이지까지 스크래핑을 진행하고 싶은지 지정해줘야한다.
    # 제대로 지정 안해주면 에러남! 예를 들어 34페이지가 없는데 34페이지라고 넣었으면..
    if final == 34:
        print('모든 페이지의 크롤링이 끝났습니다. 종료합니다.')
        break

# 브라우저를 종료
browser.quit()

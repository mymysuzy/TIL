import csv
import pymysql
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# cafe.py :: 일반적인 스크래핑
# cafe2.py :: 스크래핑 하다 중간에 뻑나서 중간에서 부터 다시 스크래핑 해야할 때

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

headers = {
    "User-Agent": user_agent,
    "Accept-Language": "ko=KR,ko"
}
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=options)
browser.get("https://map.kakao.com/")
elem = browser.find_element_by_id("search.keyword.query")
elem.send_keys("광주광역시 북구 카페")
elem.send_keys(Keys.ENTER)


store_list = []

soup = BeautifulSoup(browser.page_source, "html.parser")
elems = browser.find_elements_by_class_name("moreview")
for elem in elems:
    if elem.get_attribute("href"):
        browser2 = webdriver.Chrome(options=options)
        browser2.get(elem.get_attribute("href"))
        time.sleep(3)
        soup = BeautifulSoup(browser2.page_source, "html.parser")
        Form = [None] * 6
        flag = 0
        Form.append(elem.get_attribute("href"))
        try:
            cls = soup.find("span", attrs={"class": "txt_location"}).text
            if cls == "분류: 카페" or cls == "분류: 디저트카페" or cls == "분류: 커피전문점":
                flag = 1
        except:
            pass
        try:
            name = soup.find("h2", attrs={"class": "tit_location"}).get_text()

            for i in franchise:
                if i in name:
                    flag = 0
                    break
        except:
            browser2.close()
            continue

        if flag == 0:
            browser2.close()
            continue

        Form[0] = name
        try:
            updated_date = soup.find("span", attrs={"class": "date_revise"})
            Form[1] = updated_date.get_text()
        except:
            pass
        try:
            address_origin = soup.find(
                "span", attrs={"class": "txt_address"}).get_text()
            address = ""
            for i in address_origin.split():
                address += (i + ' ')
            Form[2] = address
        except:
            pass
        try:
            homepage = soup.find("a", attrs={"class": "link_homepage"})["href"]
            Form[3] = homepage
        except:
            pass

        try:
            telephone = soup.find(
                "span", attrs={"class": "txt_contact"}).get_text()
            Form[4] = telephone
        except:
            pass

        # try:
        #     tags_origin = soup.find_all("a", attrs={"class" : "link_tag"})
        #     tags = []
        #     for tag in tags_origin:
        #         if tag["href"] != "#none":
        #             tag = tag.get_text()
        #             tag = re.sub(r'\n, \r', '', tag)
        #             tag= tag.strip()
        #             tags.append(tag)
        #     Form[5] = tags
        # except:
        #     pass

        # try:
        #     menus_origin = soup.find_all("div", attrs={"class" : "info_menu"})
        #     menus = []
        #     for menu in menus_origin:
        #         name = menu.find("span", attrs={"class" : "loss_word"}).get_text()
        #         price = menu.find("em", attrs={"class" : "price_menu"}).get_text()
        #         menus.append([name, price])
        #     Form[6] = menus
        # except:
        #     pass
        # try:
        #     reviews_origin = soup.find_all("p",attrs={"class" : "txt_comment"})
        #     star_rates = soup.find_all("em", attrs={})
        #     reviews = []
        #     for review in reviews_origin:
        #         reviews.append(review.find("span").get_text())
        #     Form[7] = reviews
        # except:
        #     pass

        # try:
        #     WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
        #     time.sleep(5)
        #     images=[]
        #     i = 0
        #     image_list = browser2.find_elements_by_class_name("link_item")
        #     for image in image_list[0]:
        #         image.click()
        #         elem = WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
        #         images.append(elem.get_attribute("src"))
        #     Form[5] = images
        # except:
        #     pass
        try:
            WebDriverWait(browser2, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
            time.sleep(3)
            image_len = 1
            temp = ''
            image_list = browser2.find_elements_by_class_name("link_item")
            for image in image_list:
                image.click()
                elem = WebDriverWait(browser2, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
                temp = elem.get_attribute("src")
                if image_len == 1:
                    break
            Form[5] = temp
        except:
            pass
        print(Form)
        store_list.append(Form)
    browser2.close()

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
print('1 페이지의 크롤링이 끝났습니다.')

elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "info.search.place.more")))
elem.send_keys('\n')
soup = BeautifulSoup(browser.page_source, "html.parser")
elems = browser.find_elements_by_class_name("moreview")


for elem in elems:
    if elem.get_attribute("href"):
        browser2 = webdriver.Chrome(options=options)
        browser2.get(elem.get_attribute("href"))
        time.sleep(3)
        soup = BeautifulSoup(browser2.page_source, "html.parser")
        Form = [None] * 6
        flag = 0
        Form.append(elem.get_attribute("href"))
        try:
            cls = soup.find("span", attrs={"class": "txt_location"}).text
            if cls == "분류: 카페" or cls == "분류: 디저트카페" or cls == "분류: 커피전문점":
                flag = 1
        except:
            pass
        try:
            name = soup.find("h2", attrs={"class": "tit_location"}).get_text()

            for i in franchise:
                if i in name:
                    flag = 0
                    break
        except:
            browser2.close()
            continue

        if flag == 0:
            browser2.close()
            continue

        Form[0] = name
        try:
            updated_date = soup.find("span", attrs={"class": "date_revise"})
            Form[1] = updated_date.get_text()
        except:
            pass
        try:
            address_origin = soup.find(
                "span", attrs={"class": "txt_address"}).get_text()
            address = ""
            for i in address_origin.split():
                address += (i + ' ')
            Form[2] = address
        except:
            pass
        try:
            homepage = soup.find("a", attrs={"class": "link_homepage"})["href"]
            Form[3] = homepage
        except:
            pass
        try:
            telephone = soup.find(
                "span", attrs={"class": "txt_contact"}).get_text()
            Form[4] = telephone
        except:
            pass
        # try:
        #     tags_origin = soup.find_all("a", attrs={"class" : "link_tag"})
        #     tags = []
        #     for tag in tags_origin:
        #         if tag["href"] != "#none":
        #             tag = tag.get_text()
        #             tag = re.sub(r'\n, \r', '', tag)
        #             tag= tag.strip()
        #             tags.append(tag)
        #     Form[5] = tags
        # except:
        #     pass

        # try:
        #     menus_origin = soup.find_all("div", attrs={"class" : "info_menu"})
        #     menus = []
        #     for menu in menus_origin:
        #         name = menu.find("span", attrs={"class" : "loss_word"}).get_text()
        #         price = menu.find("em", attrs={"class" : "price_menu"}).get_text()
        #         menus.append([name, price])
        #     Form[6] = menus
        # except:
        #     pass
        # try:
        #     reviews_origin = soup.find_all("p",attrs={"class" : "txt_comment"})
        #     star_rates = soup.find_all("em", attrs={})
        #     reviews = []
        #     for review in reviews_origin:
        #         reviews.append(review.find("span").get_text())
        #     Form[7] = reviews
        # except:
        #     pass
        try:
            WebDriverWait(browser2, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
            time.sleep(3)
            image_len = 1
            temp = ''
            image_list = browser2.find_elements_by_class_name("link_item")
            for image in image_list:
                image.click()
                elem = WebDriverWait(browser2, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
                temp = elem.get_attribute("src")
                if image_len == 1:
                    break
            Form[5] = temp
        except:
            pass
        # try:
        #     WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
        #     time.sleep(5)
        #     images=[]
        #     i = 0
        #     image_list = browser2.find_elements_by_class_name("link_item")
        #     for image in image_list[0]:
        #         image.click()
        #         elem = WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
        #         images.append(elem.get_attribute("src"))
        #     Form[8] = images
        # except:
        #     pass

        # try:
        #     WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
        #     time.sleep(3)
        #     images = []
        #     image_list = browser2.find_elements_by_class_name("link_item")
        #     for image in image_list:
        #         image.click()
        #         elem = WebDriverWait(browser2, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
        #         images.append(elem.get_attribute("src"))
        #     Form[5] = images[:]
        # except:
        #     pass
        print(Form)

        store_list.append(Form)
    browser2.close()

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
print('2 페이지의 크롤링이 끝났습니다.')


Page = 2
final = Page


def scrap():
    global Page, final
    final += 1

    if 5 <= Page:
        elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, f"info.search.page.next")))
        Page = 1

    else:
        Page += 1
        elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, f"info.search.page.no{Page}")))

    elem.send_keys('\n')
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    elems = browser.find_elements_by_class_name("moreview")

    for elem in elems:
        if elem.get_attribute("href"):
            browser2 = webdriver.Chrome(options=options)
            browser2.get(elem.get_attribute("href"))
            time.sleep(3)
            soup = BeautifulSoup(browser2.page_source, "html.parser")
            Form = [None] * 6
            Form.append(elem.get_attribute("href"))
            flag = 0
            try:
                cls = soup.find("span", attrs={"class": "txt_location"}).text
                if cls == "분류: 카페" or cls == "분류: 디저트카페" or cls == "분류: 커피전문점":
                    flag = 1
            except:
                pass
            try:
                name = soup.find(
                    "h2", attrs={"class": "tit_location"}).get_text()

                for i in franchise:
                    if i in name:
                        flag = 0
                        break
            except:
                browser2.close()
                continue

            if flag == 0:
                browser2.close()
                continue

            Form[0] = name
            try:
                updated_date = soup.find(
                    "span", attrs={"class": "date_revise"})
                Form[1] = updated_date.get_text()
            except:
                pass
            try:
                address_origin = soup.find(
                    "span", attrs={"class": "txt_address"}).get_text()
                address = ""
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
            # try:
            #     tags_origin = soup.find_all("a", attrs={"class" : "link_tag"})
            #     tags = []
            #     for tag in tags_origin:
            #         if tag["href"] != "#none":
            #             tag = tag.get_text()
            #             tag = re.sub(r'\n, \r', '', tag)
            #             tag= tag.strip()
            #             tags.append(tag)
            #     Form[5] = tags
            # except:
            #     pass

            # try:
            #     menus_origin = soup.find_all("div", attrs={"class" : "info_menu"})
            #     menus = []
            #     for menu in menus_origin:
            #         name = menu.find("span", attrs={"class" : "loss_word"}).get_text()
            #         price = menu.find("em", attrs={"class" : "price_menu"}).get_text()
            #         menus.append([name, price])
            #     Form[6] = menus
            # except:
            #     pass
            # try:
            #     reviews_origin = soup.find_all("p",attrs={"class" : "txt_comment"})
            #     star_rates = soup.find_all("em", attrs={})
            #     reviews = []
            #     for review in reviews_origin:
            #         reviews.append(review.find("span").get_text())
            #     Form[7] = reviews
            # except:
            #     pass

            try:
                WebDriverWait(browser2, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "frame_g"))).click()
                time.sleep(3)
                image_len = 1
                temp = ''
                image_list = browser2.find_elements_by_class_name("link_item")
                for image in image_list:
                    image.click()
                    elem = WebDriverWait(browser2, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "img_photo")))
                    temp = elem.get_attribute("src")
                    if image_len == 1:
                        break
                Form[5] = temp
            except:
                pass

            print(Form)
            store_list.append(Form)
        browser2.close()


while True:
    scrap()
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
    if final == 34:
        print('모든 페이지의 크롤링이 끝났습니다. 종료합니다.')
        break

browser.quit()


with open('북구.txt', 'w', newline='', encoding='utf8') as f:
    f.write(str(store_list))

# with open('남구.csv', 'w',newline='', encoding='cp949') as f:
#     write = csv.writer(f)
#     write.writerows(store_list)

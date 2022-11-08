# 📌 XML

> eXtensible Markup Language

<br>

* Android에서 `UI를 그리기 위해서 채택한 언어`
  
  즉, DSL(Domain Specific Language)이다.
  
  * 도메인 특화 언어
  
  * 특수한 목적을 달성하기 위한 언어

<br>

```
[참고] HTML과 XML의 차이점

* 둘 다 마크업 언어이다. 

  * 계산을 수행하지 않으므로 프로그래밍 언어가 아니다.  

* HTML은 페이지의 구조를 개발하는데 사용되는 하이퍼 텍스트 마크업 언어이다.

* XML은 플랫폼간 데이터를 교환하는데 사용되는 확장 가능한 마크업 언어이다.
```

<br>

<br>

---

# 📌단위

<br>

### Dp

> Density-Independent Pixels) 

<br>

- 화면의 크기와 해상도가 달라도 동일한 비율의 UI를 보여주기 위해 Android에서 정의한 단위  
  - -> 휴대폰 기기마다 다른 크기로 보일 수 있는 픽셀의 단점을 보완
- 비율로 크기를 정한다

<br>

<br>

---

# 📌 View 컴포넌트

> 화면을 그릴 때 기본적으로 제공이 되는 xml파일들

<img title="" src="file:///C:/Users/sohyun/AppData/Roaming/marktext/images/2022-11-08-16-40-28-image.png" alt="" width="239" data-align="center">

<br>

```
위젯(Widget), 뷰 클래스(View class), 컴포넌트(Component), 레이아웃이라 부르기도 한다
```

<br>

### 종류

- 부모 뷰(= 루트 뷰, 컨테이너 뷰)  
  - 다른 뷰를 가질수 있는 뷰  
- 자식 뷰  
  - 다른 뷰를 가질수 없는 뷰

<br>

### 특수한 뷰

- 레이아웃 뷰  
  - 자식뷰의 배치(위치)를 설정하는 뷰
  - ConstraintLayout, LinearLayout...

<br>

<br>

---

# 📌LinearLayout

- 부모가 될 수 있는 뷰 (컨테이너 뷰)  

- 자식의 위치를 설정하는 뷰  
  
  - 가로, 세로로 설정 할 수 있다  

- 속성  
  
  - orientation : 자식의 뷰의 방향을 설정  
  - weight : 자식이 자치하는 크기의 비율을 설정  

<br>

<br>

---

# 📌 RelativeLayout

- 부모가 될 수 있는 뷰 (컨테이너 뷰)
- 자식의 위치를 설정하는 뷰
  - 기준점을 중심으로 자식뷰를 배치  
    - 기준점 : 부모, 자식뷰 
      - 부모를 기준으로 : alignParentBottom 등
      - 자식을 기준으로 : toRightOf 등
  - 기준점을 표시하는 방법  
    - id속성을 사용 

<br>

<br>

---

# 📌 ConstraintLayout

<br>

-생략-

<br>

<br>

---

# 📌 Frame Layout

> 액자에 View를 넣는다 생각하자

<br>

* 부모가 될 수 있는 뷰 (컨테이너 뷰)

* 먼저 적힌(xml)자식뷰가 맨아래(뒤) 깔린다  
- 중첩이 필요할 때 사용한다

<img title="" src="file:///C:/Users/sohyun/AppData/Roaming/marktext/images/2022-11-08-17-46-48-image.png" alt="" width="131" data-align="center">

<br>

<br>

---

# 📌 Gravity

> 속성 중 하나이다

> gravity속성이 부여된 뷰를 어떠한 방향으로 끌어당긴다

<br>

- 종류  
    gravity -> Padding  
  
  - 속성을 부여하는 뷰와 그 안에 있는 뷰의 관계  
    layout_gravity -> Margin  
  - 속성을 부여하는 뷰와 그 외부에 있는 뷰의 관계  
    - 예) layout_gravity="bottom|right"

<br>

<br>

---

# 📌 ScrollView

> 채팅화면과 같은 것들을 구현 가능

<br>

* 자식을 오직 하나만 가질 수 있는 컨테이너 뷰
  
  * 자식뷰가 LinearLayout이면 여러개를 넣을 수 있다

* 특이한 속성
  
  * fillViewPort
    
    * 여백이 있다면 여백을 자식뷰로 채워준다

<br>

<br>

---

# 📌 Resource

> 반복되는 UI들을 효과적으로 관리할 수 있는 방법

<br>

* `drawable`
  
  * 실제 이미지 파일(jpg, png), 도형으로 만들어진 xml파일

* `layout`
  
  * 화면을 구성하는 xml

* `mipmap`
  
  * 앱의 아이콘이 온다

* `values`
  
  * `colors`
    
    * 색
  
  * `string`
    
    * 문자열
  
  * `themes`
    
    * 기본 색깔이 지정되어있음

<br>

<br>

---



































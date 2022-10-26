# TIL_Week 2

> 2022.10.20 ~2022.10.27

<br>

### 📌 2022.10.20

## [동기와 비동기](https://pythontoomuchinformation.tistory.com/661)

<br>

### 동기

> 요청과 결과가 동시에 일어난다

> 설계가 매우 간단하고 직관적

> 하지만 결과가 주어질 때 까지 다른작업을 하지 못하고 대기해야 한다

**[참고] 블록 상태**

결과가 주어질 때 까지 다른작업을 하지 못하고 대기해야하는 상태

<br>

```
예시) 
카페의 바리스타가 한 손님의 주문을 받고 해당 손님의 커피가 완성될 때 까지 
손님은 그 자리에 서서 아무것도 하지 않고 대기해야한다고 한다고 함. 

그렇지 않으면 커피를 주지 않겠다고 하는 인성 논란의 바리스타... 😲
```

<br>

### 비동기

> 요청과 결과가 동시에 일어나지 않는다

> 동기보단 설계가 복잡

> 하지만 결과가 주어질 때 까지 다른작업을 할 수 있어 자원을 효율적으로 사용 가능

**[참고] 논블록 상태**

결과가 주어질 때 까지 다른작업을 할 수 있는 상태

<br>

```
예시) 

카페의 바리스타가 한꺼번에 모든 손님의 주문을 받은 뒤 커피를 다 만들면면 진동벨로 알려준다. 

이 때 손님은 커피를 기다리는 동안 휴대폰을 보거나 화장실을 이용할 수 있다. 🤗
```

<br>

또한 동기와 비동기는 작업을 처리하고자 하는 `시각의 차이`가 있기도 하다.

* 동기 : 같은 목적을 추구하는 행위가 동시에 이루어진다.

* 비동기 : 같을 수도 다를 수도 있는 목적을 동시에 처리할 수도 동시에 처리하지 않을 수도 있다.

<br>

**REFERENCE**

https://private.tistory.com/24

<br>

<br> 

## RxJava

RxJava는 이벤트 처리와 같은 비동기 처리에 최적화 되었다. 

<br>

#### 리액티브 프로그래밍

데이터가 통지될 때 마다 관련 프로그램이 반응하여 데이터를 처리하는 프로그래밍 방식.

데이터를 생산하는 측은 데이터를 전달하는 것 까지만을 책임진다. 데이터를 소비하는 측에서 데이터로 무엇을 하는지 몰라도 된다. 

따라서 데이터를 소비하는 측에서 데이터를 처리하는 도중이라도 데이터를 생산하는 측은 바로 다음 데이터를 처리할 수 있다. 

이처럼 리액티브 프로그래밍은 비동기 처리를 쉽게 구현할 수 있다.

<br>

#### 리액티브 스트림

데이터 스트림을 비동기로 다룰 수 있는 메커니즘을 편히 사용할 수 있는 인터페이스를 제공.

데이터를 만들어서 통지하는 `Publisher`와 통지된 데이터를 처리하는 `Subscriber`로 구성된다. 

* **Publisher** : 데이터를 전송하는 생산자로서의 인터페이스

* **Subscriber** : 데이터를 수신하는 소비자로서의 인터페이스

<br>

[참고]

* **Subscription** : 데이터 갯수를 요청하고 구독을 해지하는 인터페이스

* **Processor** : Publisher와 Subscriber의 기능이 모두 있는 인터페이스

<br>

Subscriber가 Publisher를 구독하면 Publisher가 통지한 데이터를 Subscriber가 받을 수 있다.

<br>

![image](https://user-images.githubusercontent.com/74548646/197479018-b58bf2a2-99d9-4c71-850e-99754b78b39a.png)

* Publisher는 통지 준비가 끝나면 Subscriber에 통지(`onSubscribe`)한다.

* 통지를 받은 Subscriber는 받고자 하는 데이터 갯수를 요청
  
  * 만약 Subscriber가 데이터 갯수를 요청하지 않으면 Publisher는 통지를 시작할 수 없다.

* Publisher는 데이터를 생성해 Subscriber에 통지(`onNext`) 및 Subscriber로 부터 다음 요청이 올 때 까지 데이터 통지를 중단
  
  * 데이터 통지 도중 에러가 발생하면 Subscriber에 발생한 에러객체와 에러를 함께 통지(`onError`)

* Subscriber는 받은 데이터로 작업을 수행

* Publisher는 마지막으로 데이터 전송이 완료되 정상 종료되었다고 통지(`onComplete`)

<br>

이를 정리해보면 다음과 같다.

* onSubscribe : 데이터 통지가 준비되었음을 알림

* onNext : 데이터를 통지

* onError : 에러를 통지

* onComplete : 완료 통지

<br>

**REFERENCE**

https://velog.io/@seokzoo/1.-RxJava%EC%9D%98-%EA%B8%B0%EB%B3%B81

---

<br>

### 📌 2022.10.21

## RxJava의 기본구조

RxJava에서 생산자와 소비자는 크게 두 가지로 나눌 수 있다.

* Reactive Stream을 지원하는 `Flowable(생산자)`와 `Subscriber(소비자)`
  
  * Flowable은 Publisher를 구현한 클래스
  
  * Subscriber는 Reactive Streams의 클래스

* Reactive Stream을 지원하지 않고 배압기능이 없는 `Observable(생산자)`와 `Observer(소비자)`
  
  * Observable은 Reactive Streams를 구현하지 않지만 기본적인 메커니즘과 구성은 Flowable과 거의 같다. 다만 Observable과 Observer구성은 통지하는 데이터 개수를 제어하는 배압기능이 없기 때문에 데이터 개수를 요청하지 않는다.
  
  * 따라서 Subscription 대신 `Disposable`이라는 구독 해지 메소드가 있는 인터페이스를 이용한다. Disposable은 onSubscribe()메소드의 인자로 Observer에 전달되며 구독 해지를 위한 메소드 dispose()와 isDisposed()가 있다. 따라서 Observable과 Observer간에 데이터 교환 시에는 Flowable과 Subscriber처럼 데이터 개수 요청은 하지 않고 데이터가 생성되자마자 Observer에 통지된다.

---

<br>

### 📌 2022.10.24

## 1️⃣ Tablayout, Pager

### Tablayout

> 탭을 담당하는 역할

### Pager

> 종이를 넘기듯이 화면을 전환시켜 준다

### Adapter

> Pager와 Tablayout을 연결시켜주는 역할

<br>

## 2️⃣ DB

#### Android에서의 DB

1. 계층형 데이터베이스
   
   > 파일 트리구조 방식으로 데이터 저장

2. 관계형 데이터베이스
   
   > 행과 열을 가지는 테이블 형식으로 데이터 저장
   
   > 가장 보편적인 방식
   
   > SQL로 DB를 조작
   
   > 예) Oracle, PostgreSQL. SQLite

3. 객체형 데이터베이스
   
   > 객체를 저장하는 방식

4. 키-벨류 방식
   
   > 키와 벨류를 쌍으로 저장하는 방식
   
   > NoSQL

<br>

#### SQL(관계형 데이터 베이스)

> 데이터베이스를 조작하기 위한 언어

<br>

#### RDBMS

> 관계형 데이터베이스를 관리하기 위한 소프트웨어

> (Relational Database Management System)

<br>

## 3️⃣ Sharedpreference

* 키-벨류 방식으로 데이터 저장가능

* 휴대폰에 데이터를 저장

* 데이터는 앱 밑에 있다 -> 앱을 삭제하면 데이터도 삭제된다

* 사용자의 기호와 같은 간단한 데이터를 저장해야 한다

* CRUD

<br>

## 4️⃣ Room

> 데이터베이스를 쉽게 사용하기 위한 API

-> Room을 이용해서 SQLite를 조작

<br>

#### Android 데이터 저장방식

* 키-벨류 : SharedPreference(내장)

* 관계형 방식 : SQLite(내장)

<br>

#### Android의 내장된 관계형 데이터베이스를 사용시 장점

Android가 데이터를 서버와 주고받을 때, 서버를 통해 받는 데이터베이스는 관계형 데이터베이스로 이뤄져있다. Android의 관계형 데이터베이스를 사용할 시 서버의 관계형 데이터베이스로부터 받은 데이터를 저장하기에 편하다. 

<br>

# 💌오늘의 한마디

```
내 특유의 꼼꼼한 성격이 한동안 말썽이었다😥 

FastCampus의 강의 하나하나를 거의 외울듯이 수강하는 바람에
성취감 부족, 자신감 하락, 의욕 하락의 부정적 영향이 생겼다

그래서 다시금 마음을 다잡고 일단은 모든 진도를 빠르게 빼기로 했다

다시 화이팅!
```

---

<br>

### 📌 2022.10.25

## Network

>  두대 이상의 컴퓨터를 연결하는 것

<br>

#### 네트워크가 필요한 이유

1) 클라이언트(앱) -> 인터넷 -> 서버 : **요청**
   -> 내가 지금 화면을 그리려고 하는데 데이터좀 줘

2) 서버 -> 인터넷 -> 클라이언트(앱) : **응답**
   
   -> 화면을 그릴 수 있는 데이터 여기있어

<br>

### 네트워킹

> 서버와 클라이언트의 의사소통

> 네트워크 약속(프로토콜)이 존재

<br>

```
대부분의 앱들이 정보를 서버로 부터 받아서 화면을 구성한다
```

<br>

**문제점**

매번 똑같은 화면을 그릴 때 매번 똑같은 데이터를 전달받아야 한다

-> 낭비다

<br>

**해결책**

`캐싱`

> 한번 받은 데이터를 클라이언트가 로컬 데이터베이스에 저장

> 다시 필요하면 서버에 요청할 필요없이 로컬 데이터베이스를 이용

<br>

**단점**

캐싱 구현 난이도 높음

<br>

#### 프로토콜의 종류

* FTP : 파일 전송 규약

* SMTP : 메일 전송 규약

* `HTTP` : 인터넷 서비스 규약  -> 우리가 배워야할 규약

<br>

### Request

> 클라이언트가 서버에게 보내는 요청

> 이때 HTTP 규약을 따라야 한다

<br>

#### Request Header

* 요청에 대한 추가정보를 기입하는 곳

* 서버 개발자들이 특정한 값을 `header에 실어 보내달라 요청`할 때 있다

![image](https://user-images.githubusercontent.com/74548646/197688070-43ee0e72-4574-463e-a10c-4f98a9081485.png)

<br> 

#### Request Body

* 추가적인 요청이 있을 때 추가적인 정보를 기재하는 곳
  
  * 예) 모든 학생들의 정보가 아닌 id가 1인 학생의 정보만 가져와달라는 요청

* `JSON형태`로 보낸다

![image](https://user-images.githubusercontent.com/74548646/197688030-1aab7e92-5c16-4b90-8f7d-42bfe66bf1aa.png)

<br>

#### Request Method

* GET, POST, DELETE, PUT, HEAD, CONNECT ...등

![image](https://user-images.githubusercontent.com/74548646/197688001-26ce0d4d-46c6-4fc0-86f8-180fbdcc4ac7.png)

<br>

### Response

> 서버가 클라이언트에 보내는 응답

<br>

#### Response Code

* `Status 코드`
  
  * 200(성공)
  
  * 201(너가 요청한 요구사항 잘 처리 되었음)
  
  * 401(너는 요청에 대한 결과를 볼 권한이 없다)
  
  * 404(not found, 너가 보낸 요청은 잘못되었다)

![image](https://user-images.githubusercontent.com/74548646/197687967-d3f6c535-b37d-48ec-95d9-55726278d7f6.png)

<br>

**[참고] HTTP 응답코드에 대한 분류**

![image](https://user-images.githubusercontent.com/74548646/197687941-03341a02-7728-467f-a08d-1c86b9beb8dc.png)

<br>

#### JSON

> 키-벨류 방식

* {} : 객체 표현

* [] : 배열 표현

![](C:\Users\sohyun\AppData\Roaming\marktext\images\2022-10-25-14-33-20-image.png)

<br>

# 💌오늘의 한마디

```
오늘 배운 Network부분은 ssafy에서 Web개발을 배울 때 배웠던 부분이라 쉬웠다

ssafy에서 정말 어렵다고 느껴던 부분이었는데


이제와서 보니 이렇게 쉬울 수가 없다...

역시 여러번 봐야 익숙해지는구나 다시금 느꼈고


나도 여러번의 반복을 거듭하면 잘 해내는 사람이구나 느꼈다!


화이팅~~~
```

---

<br>

### 📌 2022.10.26

-> applicatin클래스가 있는게 구지 single ton이 필요하냐?는 논쟁이 있다

<br>

## 테스트를 위한 iOS 어플리케이션 배포 방식

```
iOS개발을 완료하였다! 이제 여러 기기에서 테스트 해보고 싶다.

이럴 때 Android의 경우 단순하게 apk를 빌드해서 다른사람에게 파일로 전송해주면된다.

하지만 iOS의 경우엔 조금 다르다. ipa 자체로 설치가 불가능하기 때문이다.
```

<br>

### 방법 1️⃣ 개발용 테스트

> 가내수공업 빌드

그냥 컴퓨터와 휴대폰 기기를 선으로 직접적으로 연결해주고 빌드하면 된다.

<br>

일일이 기기 하나하나 꼽아가며 빌드해주어야하기 때문에 수고로움이 크다.

<br>

### 방법 2️⃣ 애드혹(adhoc)

애드혹 방식(over the air)은 단순하다
테스트기기의 uuid를 등록 및 배포하고 해당기기에서 테스트 하는 방식

<br>

* 개발완료
* 테스트기기의 uuid 수집
* 해당 uuid를 개발자 센터에 등록
* 빌드 후 export하여 드랍박스 등의 서버에 업로드
* 해당 기기에 받아서 테스트

<br>

**[참고] over the air**
펌웨어 업데이트 방식 중 하나
컴퓨터에 연결하지 않고 Wi-Fi등을 사용해 무선으로 펌웨어를 업데이트 하는 기술

<br>

### 방법 3️⃣ 테스트 플라이트(베타테스트)

앱설치 등 통계치를 관리하고 모니터링 할 수 있다.
그야말로 베타 테스트로 제격!

<br>

내부 배포와 외부 배포 방식이 있다.

<br>

* `내부 배포` : 이메일(애플id)을 받아 초대하는 방식

* `외부 배포` : 이메일 필요없이 설치 링크를 전달하는 방식

<br>

하지만 앱심사를 통과해야 한다

<br>

### 방법 4️⃣ 엔터프라이즈

uuid등록이나 이메일이 필요하거나 하지 않다

배포하면 테스트를 원하는 모두에게 설치가 가능하다

iOS를 배포할 수 있는 방법 중 가장 편하고, 앱스토어가 아닌 곳에서 불특정 다수에게 배포하기 위해선 엔터프라이즈가 적격이긴 하지만!

<br>

연간 비용이 한화 약 30만원이며 신청과정도 까다롭기 때문에 현업에선 잘 사용하지 않는다

<br>

### 결론

`애드훅`이나 `테스트 플라이트`를 현업에선 많이 사용한다

<br>

**REFERENCE**
https://ithoon.tistory.com/30
https://www.blueswt.com/124
https://skytitan.tistory.com/346

<br>

## Root Activity란?

>  어플리케이션을 켰을 때 실행되는 최초의 Activity

<br>

Android 어플리케이션의 AndroidManifest.xml에서 intent-filter요소 안에 MAIN으로 선언되어 있으며 보통 LAUNCHER도 category 요소로 같이 선언되어 있다.

<br>

그런데 이러한 root activity보다 더 먼저 실행되는 것이 있다.

바로 Application 클래스!

## 

<br>

## Application 클래스란?

application 클래스는 `어느 Component(Activity, Service, Intent 등)에서나 공유할 수 있는 전역 클래스`이며 `공동으로 관리해야하는 데이터를 작성하기에 적합`하다.

<br>

Application 클래스는 root activity와 마찬가지로 AndroidManifest.xml에 정의해서 사용하는데, application요소 안에 name속성으로 지정되어있는 클래스를 말한다.

<br>

Application 클래스는 다음과 같은 기능을 한다.

* root activity를 만들기 전에 실행해야하는 특수 작업 처리

* 모든 구성요소에서 공유해야하는 전역 초기화

<br>

**REFERENCE**

[[Android] Application 클래스란?](https://onlyfor-me-blog.tistory.com/374)

[[Android]액티비티와 태스크](https://promobile.tistory.com/202#:~:text=Root%20Activity%EB%8A%94%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%EC%9D%98,%EC%B5%9C%EC%B4%88%EC%9D%98%20%EC%95%A1%ED%8B%B0%EB%B9%84%ED%8B%B0%EB%A5%BC%20%EB%A7%90%ED%95%9C%EB%8B%A4.)

<br>

## TextUtils

`isEmpty()`

> String값에 대해 null체크를 해주는 메서드 isEmpty()를 제공한다

<br>

 value값이 null값은 아닌지 그리고 String값이 들어갔는지를 체크할 수 있다

```kotlin
TextUtils.isEmpty(value)
```

<br>

String값이 들어왔다면 `true` 그렇지 않다면 `false`를 반환한다

<br>

`equals()`

> 또한 null체크를 해주고, 두 개의 값이 같은 값인지 체크해주는 메서드 equals(a, b)를 제공한다

<br>

```kotlin
TextUtils.equals(value1, value2)
```

<br>

# 💌오늘의 한마디

```
Android 개발에 대해 너무 막막히만 생각했던 것 같다

이렇게 차근차근 해나가니 점점 눈에 익혀지고 모바일개발이 재밌어진다


TIL을 다시금 적게된 만큼 매주 금요일엔 복습하는 시간을 가져야겠다!
```

# TIL_Week 1

> 2022.10.12 ~2022.10.19

<br>

### 2022.10.12

#### 1. [MVVM 패턴이란 무엇인가?]([[Android] MVVM패턴에 대해 간단히 알아보자](https://pythontoomuchinformation.tistory.com/655))

>  회사 코드를 분석하다가 **MVVM패턴을 따르고 있는 앱** 이라는 이야기를 듣고, 그동안 궁금했던 이 패턴에 대해 알아보기로 하였다.

## 

## MVVM 패턴이란?

### 

### 구성요소

`Model`, `View`, `ViewModel`로 이루어져있다.

![](C:\Users\sohyun\AppData\Roaming\marktext\images\2022-10-12-16-45-41-image.png)

#### 

#### View

> `사용자에게 보여지는 레이아웃`

> 사용자와의 상호작용으로 받은 입력을 ViewModel에 전달한다.

> View는 `UI업데이트를 위해 ViewModel과 Binding`하게 된다. 

> 즉, View가 ViewModel을 구독하여 ViewModel의 상태가 변경되면 그 이벤트를 받아 UI를 갱신한다

#### 

#### Model

> 데이터와 관련된 `비즈니스 로직을 처리하는 곳`이다.

> DB나 네트워크 등 `다양한 데이터 소스로 부터 필요한 데이터를 준비`한다.

#### 

#### ViewModel

> `Model에서 가져온 데이터를 View에 뿌려줄 수 있는 형태로 가공`한다. 

> View는 ViewModel의 reference를 가지지만
> ViewModel은 View에 대한 정보가 전혀 없어야한다.

> MVC패턴의 Controller와 다른점은 `View가 ViewModel을 관찰하는 형태`로 binding되어 있다. 
> 따라서 LiveData라이브러리를 통해 데이터 업데이트를 View가 자동으로 받을 수 있는 형태이다.

#### 

#### 기타

`각 컴포넌트(View, ViewMode, Model)는` 서로 Reference를 가지지 않고 View -> ViewModel -> Model 형태의 `단방향 Dependency`를 가진다.

---

### 2022.10.13

#### 1. [Network에서 header란?](https://pythontoomuchinformation.tistory.com/656)

## 

## Header

> 데이터 앞 부분에 `파일에 대한 정보`를 실어놓은 부분



주로 `데이터 형식` 혹은 `시간`과 `주소`에 대한 정보로 이뤄짐

### 

### 데이터를 주고 받는 과정을 확인함으로서 Header를 이해해보자

![](C:\Users\sohyun\AppData\Roaming\marktext\images\2022-10-13-13-59-04-image.png)

[장구리, Lifelog : 네이버 블로그](https://blog.naver.com/hai0416/221593312143)

![](C:\Users\sohyun\AppData\Roaming\marktext\images\2022-10-13-14-04-51-image.png)

[Network Encyclopedia](https://networkencyclopedia.com/header/)



`데이터를 전송하는 측면의 레이어`

* 상위층에서 받은 **데이터에 Header를 붙여** 하위층에 넘긴다

* 점점 더 **하위층**으로 내려갈 수록 **패킷 전체 크기는 커진다**

`데이터를 전달받는 측면의 레이어`

* 전달받은 패킷에 포함된 **Header 정보를 사용하여 필요한 프로세스를 거친 후 Header를 제거**하고 상위층으로 보낸다

* 점점 더 **상위층**으로 올라갈 수록 **패킷 전체 크기는 작아지고**

* 결국 전송측에서 보낸 **데이터만 남게된다.**



### [참고] Packet이란?

> Network에서 데이터를 주고받을 때 정해놓은 규칙

> 정보를 보낼 때 특정 형태를 맞추어 보낸다는 것

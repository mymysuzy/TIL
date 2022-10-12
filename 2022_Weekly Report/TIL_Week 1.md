# TIL_Week 1

> 2022.10.12 ~2022.10.19

<br>

### 2022.10.12

1. [MVVM 패턴이란 무엇인가?]([[Android] MVVM패턴에 대해 간단히 알아보자](https://pythontoomuchinformation.tistory.com/655))

>  회사 코드를 분석하다가 **MVVM패턴을 따르고 있는 앱** 이라는 이야기를 듣고, 그동안 궁금했던 이 패턴에 대해 알아보기로 하였다.



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

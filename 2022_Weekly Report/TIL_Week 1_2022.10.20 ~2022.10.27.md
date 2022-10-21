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

예) 카페의 바리스타가 한 손님의 주문을 받고 해당 손님의 커피가 완성될 때 까지 손님은 그 자리에 서서 아무것도 하지 않고 대기해야한다고 한다고 함. 그렇지 않으면 커피를 주지 않겠다고 하는 인성 논란의 바리스타... 😲

<br>

### 비동기

> 요청과 결과가 동시에 일어나지 않는다

> 동기보단 설계가 복잡

> 하지만 결과가 주어질 때 까지 다른작업을 할 수 있어 자원을 효율적으로 사용 가능

**[참고] 논블록 상태**

결과가 주어질 때 까지 다른작업을 할 수 있는 상태

<br>

예) 카페의 바리스타가 한꺼번에 모든 손님의 주문을 받은 뒤 커피를 만들고 진동벨로 알려준다. 이 때 손님은 커피를 기다리는 동안 휴대폰을 보거나 화장실을 이용할 수 있다. 🤗

<br>

또한 동기와 비동기는 작업을 처리하고자 하는 `시각의 차이`가 있기도 하다.

* 동기 : 같은 목적을 추구하는 행위가 동시에 이루어진다.

* 비동기 : 같을 수도 다를 수도 있는 목적을 동시에 처리할 수도 동시에 처리하지 않을 수도 있다.

<br>

REFERENCE

https://private.tistory.com/24

<br>

<br>

## 

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

![](C:\Users\sohyun\AppData\Roaming\marktext\images\2022-10-20-14-45-25-image.png)

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

REFERENCE

https://velog.io/@seokzoo/1.-RxJava%EC%9D%98-%EA%B8%B0%EB%B3%B81

### 

### 📌 2022.10.21

## RxJava의 기본구조

RxJava에서 생산자와 소비자는 크게 두 가지로 나눌 수 있다.

* Reactive Stream을 지원하는 `Flowable(생산자)`와 `Subscriber(소비자)`
  
  * Flowable은 Publisher를 구현한 클래스
  
  * Subscriber는 Reactive Streams의 클래스

* Reactive Stream을 지원하지 않고 배압기능이 없는 `Observable(생산자)`와 `Observer(소비자)`
  
  * Observable은 Reactive Streams를 구현하지 않지만 기본적인 메커니즘과 구성은 Flowable과 거의 같다. 다만 Observable과 Observer구성은 통지하는 데이터 개수를 제어하는 배압기능이 없기 때문에 데이터 개수를 요청하지 않는다.
  
  * 따라서 Subscription 대신 `Disposable`이라는 구독 해지 메소드가 있는 인터페이스를 이용한다. Disposable은 onSubscribe()메소드의 인자로 Observer에 전달되며 구독 해지를 위한 메소드 dispose()와 isDisposed()가 있다. 따라서 Observable과 Observer간에 데이터 교환 시에는 Flowable과 Subscriber처럼 데이터 개수 요청은 하지 않고 데이터가 생성되자마자 Observer에 통지된다.

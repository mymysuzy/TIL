# TIL_Week 3

> 2022.10.26 ~2022.11.01

<br>

<br>

### 📌 2022.10.26

-> applicatin클래스가 있는게 구지 single ton이 필요하냐?는 논쟁이 있다

<br>

## ✨테스트를 위한 iOS 어플리케이션 배포 방식

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

---

<br>

## ✨Root Activity란?

>  어플리케이션을 켰을 때 실행되는 최초의 Activity

<br>

Android 어플리케이션의 AndroidManifest.xml에서 intent-filter요소 안에 MAIN으로 선언되어 있으며 보통 LAUNCHER도 category 요소로 같이 선언되어 있다.

<br>

그런데 이러한 root activity보다 더 먼저 실행되는 것이 있다.

바로 Application 클래스!

## 

<br>

## ✨Application 클래스란?

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

## ✨TextUtils

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

---

<br>

### 📌 2022.10.27

<br>

## ✨ Kotlin에서의 object

### 객체 표현식 및 선언

때로는 새 하위 클래스를 명시적으로 선언하지 않고 일부 클래스를 약간 수정한 개체를 만들어야 하는 경우가 있습니다. Kotlin은 이를 객체 표현식(*Object expressions*)과 객체 선언(*object declarations*)으로 처리할 수 있습니다.

<br>

#### 객체 표현

객체 표현식(*Object expressions*)은 익명 클래스, 즉 클래스 선언으로 명시적으로 선언되지 않은 클래스의 개체를 만듭니다. 이러한 클래스는 일회성으로 유용합니다. 처음부터 정의하거나 기존 클래스에서 상속하거나 인터페이스를 구현할 수 있습니다. 익명 클래스의 인스턴스는 이름이 아닌 식으로 정의되기 때문에 익명 개체(*anonymous objects*)라고도 합니다.

<br>

**슈퍼타입에서 익명 객체 상속하기**

일부 유형(또는 유형)에서 상속하는 익명 클래스의 개체를 만들려면 개체와 콜론(:) 뒤에 이 유형을 지정합니다. 그런 다음 이 클래스에서 상속하는 것처럼 이 클래스의 멤버를 구현하거나 재정의합니다.

```kotlin
window.addMouseListener(object : MouseAdapter() {
    override fun mouseClicked(e: MouseEvent) { /*...*/ }

    override fun mouseEntered(e: MouseEvent) { /*...*/ }
})
```

<br>

상위 유형에 생성자가 있으면 적절한 생성자 매개변수를 전달하십시오. 콜론 뒤에 쉼표로 구분된 목록으로 여러 상위 유형을 지정할 수 있습니다.

```kotlin
open class A(x: Int) {
    public open val y: Int = x
}

interface B { /*...*/ }

val ab: A = object : A(1), B {
    override val y = 15
}
```

<br>

REFERENCE

https://kotlinlang.org/docs/object-declarations.html#semantic-difference-between-object-expressions-and-declarations

<br>

---



<br>

## 

## ✨ BLE와 BT

```
기술적으로 BT와 BLE는 다른 것이다. BLE는 저전력을 최우선시 하는 통신기술로서 BT의 명성을 이용해 빠르게 저변을 확대한 것이다.
```

<br>

* Classic : BT기술만 지원

* Smart : BLE기술만 지원

* Smart ready (=원칩) : BT와 BLE기술 모두 지원

<br>

### BLE 기술

2가지만 기억하자

1. Advertise(Broadcast) Mode 

2. Connection Mode

<br>

#### Advertise(Broadcast) Mode

자신의 존재에 대해 알리는 신호인 `Advertising Packet`

이 신호를 하루 종일 쏘는 것이 바로 `Beacon(비콘)`이다.

<br>

비콘은 상대가 수신하던 안하던 Advertising Packet 신호를 쏘기만 하면 되고

최대 50m거리까지 쏠 수 있으며 보통 1~2년 사용 가능하다.

<br>

물론 Advertising Packet이 한 종류만 있는것은 아니고 Scan Request와 Scan Response로 추가 정보를 주고받는 기능을 구현할 수 있다.

<br>

#### Connection Mode

>  Advertise Mode를 통해 스캔한 디바이스 중 하나와 1:1로 연결하는 것

Connection Mode로 전환되고 나서는 서로 타이밍을 맞추어 데이터를 주고받으며, Advertising과 Scan이 더이상 필요하지 않다.

<br>

이제 본격적으로 데이터를 주고받으면 된다.

<br>

데이터 전송 속도는 워낙 느리기 때문에 실제 데이터 통신은 BT Classic 혹은 Wi-Fi 기술을 이용하기도 한다.

<br>

REFERENCE

[BLE, Bluetooth Low Energy 비콘 간단 정리 :: 고마워서 만든 블로그 by 맛소금](https://blog.msalt.net/210)

<br>

<br>

# 💌오늘의 한마디

```
이어폰을 휴대폰과 연결시키지 않은 상태에서 회사 이어폰 전용 앱과 연결시켰는데
난 이렇게 하면 휴대폰과도 연결이 될 줄 알았다..

그러나 휴대폰으로 켠 음악이 하염없이 휴대폰으로만 나오게 되고..


알고보니 휴대폰과도 따로 연결시켜줘야 한다고 한다.

그 이유는 이어폰은 BLE방식 휴대폰 음악은 BT방식이기 때문이라고 한다

그래서 조금 더 서치해보게된 BT와 BLE!

난 두개가 거의 같은 기술인지 알았는데 전혀 다른 기술이라고 하니 충격받았다

이러한 불편함 때문에 앞으로 나올 이어폰은 BT방식을 적용한다고 한다

이렇게 또 하나 알아간다
```

---

<br>

### 📌 2022.10.28

<br>

## ✨

<br>

---

<br>

### 📌 2022.10.29

<br>

## ✨

<br>

---

<br>

### 📌 2022.10.30

<br>

## ✨

<br>

---

<br>

### 📌 2022.10.31

<br>

## ✨

<br>

---

<br>

### 📌 2022.11.01

<br>

## ✨

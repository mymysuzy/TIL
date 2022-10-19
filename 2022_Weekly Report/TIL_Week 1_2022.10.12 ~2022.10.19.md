# TIL_Week 1

> 2022.10.12 ~2022.10.19

<br>

### 📌 2022.10.12

#### [MVVM 패턴이란 무엇인가?](https://pythontoomuchinformation.tistory.com/655)

>  회사 코드를 분석하다가 **MVVM패턴을 따르고 있는 앱** 이라는 이야기를 듣고, 그동안 궁금했던 이 패턴에 대해 알아보기로 하였다.

<br>

## MVVM 패턴이란?

### 구성요소

`Model`, `View`, `ViewModel`로 이루어져있다.

![image](https://user-images.githubusercontent.com/74548646/196339663-d9996379-1ea7-4788-9d3a-78f86a37b469.png)

<br>

#### View

> `사용자에게 보여지는 레이아웃`

> 사용자와의 상호작용으로 받은 입력을 ViewModel에 전달한다.

> View는 `UI업데이트를 위해 ViewModel과 Binding`하게 된다. 

> 즉, View가 ViewModel을 구독하여 ViewModel의 상태가 변경되면 그 이벤트를 받아 UI를 갱신한다 

#### Model

> 데이터와 관련된 `비즈니스 로직을 처리하는 곳`이다.

> DB나 네트워크 등 `다양한 데이터 소스로 부터 필요한 데이터를 준비`한다.

#### ViewModel

> `Model에서 가져온 데이터를 View에 뿌려줄 수 있는 형태로 가공`한다. 

> View는 ViewModel의 reference를 가지지만
> ViewModel은 View에 대한 정보가 전혀 없어야한다.

> MVC패턴의 Controller와 다른점은 `View가 ViewModel을 관찰하는 형태`로 binding되어 있다. 
> 따라서 LiveData라이브러리를 통해 데이터 업데이트를 View가 자동으로 받을 수 있는 형태이다.

#### 기타

`각 컴포넌트(View, ViewMode, Model)는` 서로 Reference를 가지지 않고 View -> ViewModel -> Model 형태의 `단방향 Dependency`를 가진다.

<br>

---

### 📌 2022.10.13

#### [Network에서 header란?](https://pythontoomuchinformation.tistory.com/656)

<br>

## Header

> 데이터 앞 부분에 `파일에 대한 정보`를 실어놓은 부분

주로 `데이터 형식` 혹은 `시간`과 `주소`에 대한 정보로 이뤄짐

### 

<br>

### 데이터를 주고 받는 과정을 확인함으로서 Header를 이해해보자

![image](https://user-images.githubusercontent.com/74548646/196339755-e6a9bdbd-f2ee-43d9-9e9b-64d7fa01ac24.png)

[장구리, Lifelog : 네이버 블로그](https://blog.naver.com/hai0416/221593312143)

<br>

![image](https://user-images.githubusercontent.com/74548646/196339815-60e9b605-ee0b-48fa-a194-57875c4b490c.png)

[Network Encyclopedia](https://networkencyclopedia.com/header/)

<br>

`데이터를 전송하는 측면의 레이어`

* 상위층에서 받은 **데이터에 Header를 붙여** 하위층에 넘긴다

* 점점 더 **하위층**으로 내려갈 수록 **패킷 전체 크기는 커진다**

`데이터를 전달받는 측면의 레이어`

* 전달받은 패킷에 포함된 **Header 정보를 사용하여 필요한 프로세스를 거친 후 Header를 제거**하고 상위층으로 보낸다

* 점점 더 **상위층**으로 올라갈 수록 **패킷 전체 크기는 작아지고**

* 결국 전송측에서 보낸 **데이터만 남게된다.**

#### 

<br>

#### [참고] Packet이란?

> Network에서 데이터를 주고받을 때 정해놓은 규칙

> 정보를 보낼 때 특정 형태를 맞추어 보낸다는 것

<br>

---

### 📌2022.10.14

#### [안드로이드에서 Notification이란?](https://pythontoomuchinformation.tistory.com/manage/posts/)

<br>

## Notification

![image](https://user-images.githubusercontent.com/74548646/196339856-6090bdb8-8a41-4ffe-bc78-1002900e1744.png)

Notification이란, 위 사진과 같은 것을 이야기한다.

사진 속 Notification은 Notification 중 가장 간단한 형태이며 아이콘, 제목, 컨텐츠를 보여준다.

<br>

이러한 Notification을 만드려면 **먼저 Notification Channel을 생성해야 한다.**

다음 코드는 Channel을 생성하는 코드이다.

```kotlin
private fun createNotificationChannel(context: Context, importance: Int, showBadge: Boolean,
                                      name: String, description: String) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val channelId = "${context.packageName}-$name"
        val channel = NotificationChannel(channelId, name, importance)
        channel.description = description
        channel.setShowBadge(showBadge)

        val notificationManager = context.getSystemService(NotificationManager::class.java)
        notificationManager.createNotificationChannel(channel)
    }
}
```

<br>

NotificationManager.createNotificationChannel()로 채널을 생성할 수 있다.

채널의 아이디, 이름, 중요도로 생성한 NotificationChannel 객체를 인자로 전달한다.

* Channel Id : 앱마다 유니크한 Id를 생성해야한다.

* Channel Name : 사용자에게 보여지는 채널의 이름

* Channel Importance : 채널 중요도의 의미이며 IMPORTANCE_DEFAULT, IMPORTANCE_HIGH 등으로 설정할 수 있다.

<br>

이제 Channel이 등록되었으니, Channel Id를 사용하여 Notification을 만들어주면 된다.

만약 위와 같은 기본 Notification의 형태가 아닌 다른 style의 Notification을 사용하려면, 원하는 Style에 맞는 Notification을 선택하여 커스텀하면 된다.

<br>

### Style

> 기본적인 Notification이 아닌 커스텀된 형태로 만들고 싶을 때가 있다.

> 이럴 때 Android에선 자주 사용되는 Notification을 여러 Style로 만들어두었다.

<br>

아래는 다양한 **Notification Style**중 몇 개를 들고와보았다.

* `BigText`
  
  * 많은 양의 텍스트를 보여줄 수 있다.
  
  * 기본 Notification과 다르게 접고 펼 수 있는 기능이 있다.

![image](https://user-images.githubusercontent.com/74548646/196339890-15744e1d-ab0d-41c9-85fc-e5d535662a59.png)

* `BigPicture`
  
  * 큰 이미지를 보여준다.

![image](https://user-images.githubusercontent.com/74548646/196339934-07829fc8-7ef2-4118-a3e9-cd1d993cc940.png)

* `Head up Notification`
  
  * 전면에 Notification이 뜬다.
  
  * 사용자가 Status Bar를 내려 확인하지 않아도 바로 화면에 뜬다.
    
    * 전화와 같은 중요한 작업을 알릴 때 사용

![image](https://user-images.githubusercontent.com/74548646/196339967-0950117e-c5b6-4fd2-a200-5f03f96beb86.png)

<br>

REFERENCE

https://codechacha.com/ko/notifications-in-android/

<br>

---

### 📌2022.10.17

## Java로 만들어진 프로젝트에 Kotlin으로 코드짜기

Java로 만들어진 프로젝트에 Kotlin 언어를 사용하기 위해선 Kotlin언어에 대한 설정이 되어있어야 한다.

<br>

Android Studio의 [File] - [Settings] 로 들어간 후 검색창에 kotlin을 검색한다.

![image](https://user-images.githubusercontent.com/74548646/196340002-b48fd9fd-ca66-42cc-9d56-4883e918a965.png)

만약 plugin이 설치되어 있지 않다면 설치를 진행해주자.

설치가 되어있는 상태라면, 위 빨간 밑줄과 같이 Kotlin 버전을 확인해주자.

```bash
212-1.7.10-release-333-AS5457.46
```

여기서 버전은 1.7.10을 가리킨다.

<br>

Project `build.gradle`파일에 들어가 아래와 같이 Kotlin의 버전과 classpath가 선언되어있는지 확인해주고 그렇지 않다면 선언해주자.

```bash
// Project build.gradle file.
buildscript {
    ext.kotlin_version = '1.4.10'
    ...
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```

<br>

혹시나 해서 덧붙이는 건데, 나와 같이 build.gradle에 입력하라고 말하면 많은 build.gradle파일 중 어디에 입력하라는건지 모르는 사람들을 위해 적는다.

Project build.gradle 파일에 적으라는 말은 아래와 같이 Project라 적혀있는 build.gradle에 적으라는 것이다.

<img src="https://user-images.githubusercontent.com/74548646/196340040-36ff6936-5e7b-4b55-b20c-f269ba628a21.png" title="" alt="image" width="393">

<br>

그 외 build.gradle은 Module에 적으라는 표현을 쓴다.

<img src="https://user-images.githubusercontent.com/74548646/196340056-93bd07a5-418e-4b62-b30b-0ca32f735bde.png" title="" alt="image" width="343">

<br>

REFERENCE

https://developer.android.com/kotlin/add-kotlin

<br>

---

### 📌2022.10.18

## Kotlin 파일은 Java파일의 Lombok 라이브러리와 호환되지 않는다

재직중인 회사의 **Java와 Android Studio 기반 어플리케이션**을 Java언어에서 **Kotlin으로 컨버팅**하라는 업무 지시가 내려졌다. 컨버팅 하던 중 Java파일로 실행하였을 땐 괜찮았던 **get메서드가 인식이 되지 않았다.**

<br>

소스를 분석해보니 **Java파일에선 lombok 라이브러리를 사용**해 getter/setter를 생성해주었었다.

`즉, Kotlin 파일이 lombok라이브러리의 getter/setter을 인식하지 못하고 있는 것이었다.`

<br>

이에 대해 많은 고민을 하였지만 `결국 기존 Java코드에서 lombok 라이브러리를 제거하면서 까지 Kotlin으로 컨버팅하기로 결정하였다.`

<br>

비록 Lombok을 사용함에 따라 얻을 수 있었던 코드의 간결함이란 장점을 포기해야하지만, Kotlin으로 컨버팅 하는 과정이 더 우선시되어야 한다고 생각했다.

> 앞으로 자사 모든 Android 앱에서는 Kotlin을 적극 사용할 예정이기 때문에 차차 Kotlin 사용에 대비해야함

> Lombok에 대해 포기하지 않는다면 컨버팅 작업이 더뎌질 것임



따라서 VO를 다음과 같이 바꿔주는 작업을 진행했다.

```java
public class ResponseResult {

    private ResponseHeader header;

    // private인 header의 getter/setter 직접 만들어주었다.
    public ResponseHeader getHeader() {
        return header;
    }

    public void setHeader(ResponseHeader header) {
        this.header = header;
    }
}
```



REFERENCE

[NAVER D2](https://d2.naver.com/helloworld/6685007)



---

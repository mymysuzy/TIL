# 📌Activity

* 화면을 구성하는 가장 기본이 되는 요소

* 자동으로 activity 와 매칭되는 xml을 생성해준다 + manifest에도 등록이 된다  

* 화면을 그리는 기능 + 화면에서 발생할 수 있는 일들을 처리할 수 있는 기능이 내장

<br>

#### 특수한 Activity

- 런처 activity, main activity
  - 앱이 실행될때 최초로 실행되는 activity

<br>

#### LifeCycle(생명주기)

> 안드로이드 OS가 activity를 직접 종료시키는 일은 없다

> 다만 프로세스는 종료가능

<br>

<img title="" src="file:///C:/Users/sohyun/AppData/Roaming/marktext/images/2022-11-09-10-24-20-image.png" alt="" width="558">

<br>

* `onCreate`
  
  * **필수적으로 구현**을 해야한다
  
  * 생명주기 중에서 **단 한번만 발생**한다
    
    * 단 한번만 하면 되는 일들을 여기에서 구현한다
    
    * 화면 그리기, 데이터 준비
- `onStart`
  
  - **activity를 포그라운드로 보내 상호작용할 수 있도록 준비**
    - 포그라운드 : 사용자 눈에 보일때 또는 사용중일 때
  - 매우 빠르게 완료가 된다

- `onResume`
  
  - 앱이 사용자와 상호작용이 가능한 상태
  - **특정 이벤트가 발생하여 앱에서 포커스가 떠날 때 까지 이상태에 머무르게 된다**
    - 전화가 온다거나, 기기 화면이 꺼질때
    - 화면이 가려지지 않으면 이상태에 머문다

- `onPause`
  
  - **사용자가 activity를 떠나는 것을 나타내는 첫번째 신호**
    - 엑티비티가 **포그라운드에 있지 않다는 신호**
  - 잠시 작업을 중지해야하는 작업을 일시 중지한다
    - 영상 일시 중지, GPS 일시 중

- `onStop`
  
  - **activity가 더 이상 사용자에게 표시가 되지 않는 상태**
    - 새로운 activity가 나오는 경우
    - 화면이 가려지는 경우
  - 사용자에 보이지 않는 동안 앱은 리소스를 해제 해야한다
    - 영상 종료, GPS 종료
  - 마지막으로 해야 할일 등을 수행
    - 저장을 하는 기회

- `onDestroy`
  
  - 엑티비티가 소멸되기 전에 호출된다
    - 기기회전 또는 멀티 윈도우 모드에서 시스템이 일시적으로 activity를 소멸시는 경우
    - onStop에서 해제되지 않은 모든 리소스를 해제해야 한다

<br>

<br>

---

# 📌 View Control

> View를 컨트롤하는 방법

> 사용자와의 상호작용으로 인해 뷰를 조작하는 방법

> 뷰에 이벤트가 발생했을 때 처리하는 방법

<br>

#### Listener

- 이벤트가 발생했을 때 수신하는 역할 
  - 예) setOnClickListener 등

<br>

#### xml에 존재하는 뷰를 activity로 가져오는 방법

- `findViewById`  
  - Id -> xml에서 부여한 view의 id  
- `kotlinx`  
  - 귀찮은 findViewById과정을 생략가능 하다  
  - deprecated 되었다  
    - 가급적으면 사용을 피해야한다  
- `databinding`  
  - 뷰와 데이터를 묶는다

<br>

<br>

---

# 📌 Intent

> 의도, 의사

<br>

```
- A야 (이 데이터로) B좀 해줘

- B좀 해줘

- A야 (이 데이터로) B좀 해줘 그리고 다하면 알려줘
```

- 데이터를 같이 전달할 수 있다  

<br>

#### 명시적 인텐트 (Explicit Intent)

> 호출될 대상을 명시하는 경우 

<br>

#### 암시적 인텐트 (Implicit Intent)

> 호출될 대상을 명시하지 않는 경우 

<br>

예) 공유하기 버튼 클릭 -> 공유할 수 있는 앱 여러가지가 보여진다

<br>

- AndroidManifest.xml의 `<activity>`안에 있는  `<intent-filter>`
  
  * 공유할 수 있는 앱만이 리스트에 보여져야 할 때 사용됨
    
    즉,  인텐트가 처리할 수 있는지 확인할 때 사용 

- 인텐트 호출 대상
  
  - 앱내에서  
    - 엑티비티 끼리  
  - 외부(안드로이드 OS, 시스템), 앱 끼리(권한이 필요한다)  

```
사진 앱  
   - 우리 앱 -> 시스템 -> 사진첩  
   - 우리 앱 전화 걸기 버튼 -> 시스템 -> 전화 걸기 앱  
```

<br>
<br>

---

# 📌 Context

> 앱의 흐름

<br>

Application Context  

- 하나만 존재  
- 애플리케이션이 살아 있는 동안 유지  

Activity Context  

- Activity마다 존재  
- 액티티비가 유지되는 동안에만 유지  
- Context를 구현하고 기능을 추가한게 -> Activity

```
책(Application Context)
    - Chapter1 (Activity Context)
        - chapter1-1
        - chapter1-2
    - Chapter2 (Activity Context)
        - chapter2-1
    - Chapter3 (Activity Context)
        - chapter3-1
        - chapter3-2
        - chapter3-3
```

<br>

<br>

---

# 📌 Activity Stack

- 기본 : 후입선출(LIFO, Last In, First Out)  
- stack은 될 수 있으면 건들지 않는게 좋다  
- 만약 건드린다면 분명한 의도를 가지고 적용해야 한다  
  -> 모든종류를 다 알 수는 없다  
  -> stack을 관리할 일이 발생했을 경우에 적용 가능한 launchMode, Flag를 찾아본다  



## Stack 관리 두가지 방법

#### 1️⃣ Manifest 이용

- launchMode  
  - standard(LIFO)  
  - singleTop  
    - 이동하려는 엑티비티가 이미 스택에 존재하는 경우 새로 만들지 않는다  
  - singleTask  
    - singleTask로 런치모드가 설정된 엑티비티가 호출 되었을때 새로운 박스에 담는다  
      -> 새로운 박스에도 다른 엑티비티를 쌓을 수 있다  
  - singleInstance  
    - singleTask로 런치모드가 설정된 엑티비티가 호출 되었을때 새로운 박스에 담는다  
      -> 새로운 박스에도 다른 엑티비티를 쌓을 수 없다  

<br>

#### 2️⃣ Intent Flag 이용

- FLAG_ACTIVITY_NEW_TASK (singleTask)  

- FLAG_ACTIVITY_SINGLE_TOP (singleTop)  
  0  

- FLAG_ACTIVITY_NO_HISTORY  
  
  - 호출된 엑티비티는 스택에 쌓이지 않는다 (로딩)  

- FLAG_ACTIVITY_REORDER_TO_FRONT  
  
  - 호출된 엑티비티가 스택에 존재할 경우 최상위로 올려준다  
  - A B C -> B를 호출 -> A C B  

- FLAG_ACTIVITY_CLEAR_TOP  
  
  - A B C -> A를 호출 -> A  

- FLAG_ACTIVITY_NO_ANIMATION  
  
  - 화면전환 애니메이션 생략한다  

- Intent Flag 적용  
  
  - setFlag  
    - 기존에 적용된 flag를 삭제하고 다시 설정한다  
  - addFlag  
    - flag를 추가한다

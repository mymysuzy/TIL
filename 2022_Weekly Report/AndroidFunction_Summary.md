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

Google App Engine
================================================================================

這幾天 Google 發佈了一項服務： Google App Engine 。其目的是讓程式設計師可以容易地將網頁程式 upload 到 Google
Cluster 中，交給 Google 代為管理。程式設計師可以除去系統管理的苦差事，只要專心寫程式即可。

目前它只提供 Python 語言的程式，但將來定會增加其他語言。

這對我來說真是一項天大的好消息(當然也對其他用 Python 或不用 Python 的設計師一樣)，但壞消息是我到現在還沒拿到入場卷，心急呀!

不過，還沒拿到資格，也不代表只可用時間來期待，現在正是讀手冊的好時機，這名額過少的缺點，我倒認為是 Google 深思熟慮呀!
想想看，推一個新服務，總是有未知數，不知該用多少工程師或管理工具來維護整個 Google App Engine
系統，也不知道使用者對這系統的反應到底有多熱烈，所以先給少數人用，看看反應，收些回饋訊息，而最重要的是， Google App Engine
在使用上並不像 Gmail 一樣。使用者是不能快速上手的，須先了解系統架構、 API
介面、管理工具等等，反正現在給了名額，對程設師來說，也不是『馬上』就能生個系統出來，不如慢慢給，也給程設師時間來多讀點手冊。

Google App Engine 對 Django 使用者來說，最大的改變是使用 Model 的方法不同， App Engine 一律使用 Google
Big Table 來儲存資料庫資料。

為了讓數以千計(未來可能是億計)的 App 妥善運作，當然是讓它們跑在 Google Cluster 上來得簡單，而不是跑在 Virtual Server
Hosting 上。以後者來說，一個 App 需對應一個 http deamon, database deamon 及一個 chroot
環境，這樣雖對使用者是富有功能性的(允許使用者自行增加套件及修改系統設定)，但這樣犧牲了管理系統的簡單，OSDC.tw(2008) 中所介紹的
openfoundry 正凸顯了與 Google App Engine 使用觀念上的不同。

目前在 App Engine 中操作 Big Table 的 Model 方法還依賴 GQL ，希望將來能將它改得比較像 Django Models
，或是在 Djanog Models 上直接支援 Big Table 引擎。

.. author:: default
.. categories:: chinese
.. tags:: python, google
.. comments::
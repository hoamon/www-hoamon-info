用 PGP 作網站認證
================================================================================

剛剛在用 firegpg 為 Gmail 信件加密時，忽然靈機一動，如果使用 PGP 作網站認證豈不是方便。

我們在作 Linux
系統管理時，在遠端登入上，是使用公私錀作登入的方式，並不是用帳號/密碼，這好處是加密強度大得多，且不用打一堆不對稱的文字(我的密碼的確如此)。

那麼在網站登入上，為什麼不這麼作呢? 在註冊使用者時，就要求他把公錀上傳至網站伺服器中，以後要登入時，在登入頁面上會出現隨機字串要求用私錀來作簽署，那麼網
站伺服器以公錀驗證成功後，就可確認你是那一位使用者了，這不是非常方便，不用打帳號/密碼，安全強度又高。如果再改一下 firegpg
的行為，還可以讓它自動作簽署的動作，那又更方便了。

嗯~ 惟一的問題是 Windows 多半不會預裝 GnuPG ，而一般用戶也多半不會使用 PGP 。

哈哈~ 我一定要寫一個強迫大家用 PGP 登入的網站。

== 後記 ==
寫了一個實驗性質的網站(`https://pgpauth.hoamon.info/`_)來展現這個概念。相關程式請上 Google Code:
`http://code.google.com/p/django-pgpauth/`_ 了解。

.. _https://pgpauth.hoamon.info/: https://pgpauth.hoamon.info/
.. _http://code.google.com/p/django-pgpauth/: http://code.google.com/p
    /django-pgpauth/


Old Comments in Blogger
--------------------------------------------------------------------------------



`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-04-01T08:08:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果要求每個使用者都得用 PGP 簽署驗證，得到的反彈或是拒絕使用的可能性很高，但如果是要求 web staff 只能用 PGP
登入的話，那可行性就非常高了。像是之前 `Twitter 的 staff 帳密就被 try 到`_ ，所以在不改用其他安全措施時， PGP
就是一個密碼強度相當高的方法。

.. _Twitter 的 staff 帳密就被 try 到: http://blog.xdite.net/?p=984


`Kanru Chen <http://www.blogger.com/profile/16324198998280933607>`_ at 2009-04-11T17:31:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

好主意！

`blc <http://www.blogger.com/profile/08566577661115653189>`_ at 2009-04-19T10:50:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

讓我想到firefox 上的 Magic Password Generator

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-04-19T13:44:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

> 讓我想到firefox 上的 Magic Password Generator

但 MPG 不過是幫你把密碼變得複雜一點，除示網站能限制密碼格式必須符合 MPG 的密碼格式，要不然網站很難強迫使用者必須使用 MPG 。

採用 PGP 認證，則可強迫用戶使用。且 PGP
可以有其他附加價值，如：簽章網頁內容、以簽署認證關係建立網站用戶的社交網路、網站機密訊息以公錀加密後寄至用戶信箱…。

而且 MPG 對「非 Firefox 用戶」來說就不方便了。使用 PGP 認證方式，只要求使用者至少要安裝 GnuPG 的程式(或其他 PGP
應用程式)即可，且 GnuPG 有 Mac 、 Linux 、 Windows 版。

.. author:: default
.. categories:: chinese
.. tags:: linux, firegpg, pgp
.. comments::
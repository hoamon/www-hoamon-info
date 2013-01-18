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


.. author:: default
.. categories:: chinese
.. tags:: linux, firegpg, pgp
.. comments::
使用 PayPal Express Checkout 時，如何申請 API 簽章?
================================================================================

要使用 PayPal 作為收款工具時，除了申請它的帳戶(建議是商業帳戶)外，若使用的是 Express Checkout
收款機制，你還需為自己所寫的程式申請一組 API 簽章，包含「用戶名稱」、「密碼」、「簽名」。

申請方式很簡單，先登入 `www.paypal.com`_ ，看到個人的總覽頁面如下圖：

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TTp-
qD0OqaI/AAAAAAAAC0U/CcS8br3wnEM/s400/paypal1.png
`_

點選「我的業務設定」。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TTp-
p7ijWvI/AAAAAAAAC0M/AxzNDb9Woa8/s400/paypal2.png
`_

點選「立即開始」。

`.. image:: http://1.bp.blogspot.com/_eKM9lHjTZjs/TTp-
p_Cd43I/AAAAAAAAC0E/h1nQIx4S26s/s400/paypal3.png
`_

點選「為 PayPal 帳戶要求 API 電子簽章」。

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/TTp-
pltdyEI/AAAAAAAACz8/H9rzw8JHOXo/s400/paypal4.png
`_

選擇「申請 API 電子簽章」，並點選「同意並提交」。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TTp-
peExYaI/AAAAAAAACz0/lnM56FEpdjY/s400/paypal5.png
`_

抄下「API用戶名稱」、「API密碼」、「簽名」放到你的程式碼中，就可以呼叫 PayPal 的 Express Checkout API 了。

.. _www.paypal.com: http://www.paypal.com/
.. _ ，看到個人的總覽頁面如下圖：: http://3.bp.blogspot.com/_eKM9lHjTZjs/TTp-
    qD0OqaI/AAAAAAAAC0U/CcS8br3wnEM/s1600/paypal1.png
.. _點選「我的業務設定」。: http://3.bp.blogspot.com/_eKM9lHjTZjs/TTp-
    p7ijWvI/AAAAAAAAC0M/AxzNDb9Woa8/s1600/paypal2.png
.. _點選「立即開始」。: http://1.bp.blogspot.com/_eKM9lHjTZjs/TTp-
    p_Cd43I/AAAAAAAAC0E/h1nQIx4S26s/s1600/paypal3.png
.. _點選「為 PayPal 帳戶要求 API 電子簽章」。: http://4.bp.blogspot.com/_eKM9lHjTZjs
    /TTp-pltdyEI/AAAAAAAACz8/H9rzw8JHOXo/s1600/paypal4.png
.. _選擇「申請 API 電子簽章」，並點選「同意並提交」。: http://3.bp.blogspot.com/_eKM9lHjTZjs
    /TTp-peExYaI/AAAAAAAACz0/lnM56FEpdjY/s1600/paypal5.png


Old Comments in Blogger
--------------------------------------------------------------------------------



`玫君 <http://www.blogger.com/profile/16892506554262807852>`_ at 2011-02-23T19:54:34.080+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

請問如何成為paypal的商業用戶呢？

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2011-02-23T20:46:02.471+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

到 https://www.paypal.com/tw ，選擇「商業」那邊的註冊就行了。過程中，會要求你提供銀行帳戶或信用卡號。

`Asan is Grumpie <http://www.blogger.com/profile/12486195612703743851>`_ at 2011-06-23T15:39:44.642+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

請問一下，如果我使用的是“網站付款標準版”，這樣可以申請API certificate嗎？我在我的帳戶裡怎麼樣都找不到申請的地方，謝謝你的幫忙。

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2011-06-26T19:14:19.711+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

"網站付款標準版"是收費的工具名稱。而申請的帳戶類型，只有：「個人」、「特選」、「商業」。

是不是你用的是「個人」帳戶? 因為我用「特選」、「商業」的帳戶都可以找到「申請API certificate」的地方。

.. author:: default
.. categories:: chinese
.. tags:: paypal
.. comments::
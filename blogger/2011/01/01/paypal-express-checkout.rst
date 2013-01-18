使用 PayPal Express Checkout 作線上收款機制
================================================================================

若你不太了解什麼是金流系統，可以先去看「`簡述金流系統`_」。

消費者在線上購買商品或勞務，所謂的付款其實只牽扯到兩件事：『身份驗證』及『確認額度』。但這兩件事都是特許公司如銀行或信用卡公司才能作的事。所以我們得透過中
間人或中間人的中間人(金流公司)幫我們作到這兩件事，而我選的是 PayPal ，它是跨國的金流公司，我個人認為十分適合純網際網路公司使用。

從誰那裡匯多少錢到誰那裡? 有三個變數：『付款的人』、『付多少』及『收款人』。這『收款人』當然是我們自己的公司囉。在程式中設定收款帳戶只要設定『帳戶名稱(
USERNAME)』、『密碼(PASSWORD)』及『簽名(SIGNATURE)」就行了，如何申請這三種資料請看我的另篇`文章`_。

而『付多少』的設定變數名則為 AMT 。但在消費者刷卡時，要讓他明確地了解買的東西到底有什麼? 價錢是多少? 要刷多少錢? 我們得另外設定訂單的顯示變數。
有商品名稱(L_NAME0)、商品描述(L_DESC0)、商品編號(L_NUMBER0)、購買數量(L_QTY0)、商品單價(L_AMT0)、所有商品小計
(ITEMAMT)、運送及處理費用(SHIPPINGAMT)、稅金(TAXAMT)等。

這些變數後有帶 0 的表示它可以是多值，如果該筆訂單有第二項商品的話，就設定 L_NAME1 、 L_DESC1 、 L_NUMBER1 、 L_QTY1
、 L_AMT1 ，以此類推。

這些訂單顯示變數有幾項原則：




-   ITEMAMT 必須等於 L_AMT0 * L_QTY0 + L_AMT1 * L_QTY1 + ... + L_AMTn *
    L_QTYn


-   AMT 必須等於 ITEMAMT + SHIPPINGAMT + TAXAMT




違反這兩個原則， PayPal 會報錯的。

而『付款的人』部份就不是我們程式設計師該處理的，這部份交由 PayPal 自己與消費者確認卡號是否正確、與發卡銀行確認是否允許消費者刷該筆訂單的金額。等到
PayPal 作完『身份確認』及『額度確認』後，PayPal 會回傳一個 TOKEN ，告知我們消費者有能力消費該筆訂單，如果我們接受該筆交易，就以這個
TOKEN 回覆給 PayPal ，那它就幫我們刷下消費者的卡片了。之後就能在 PayPal 的帳務管理介面中看到消費者的付款紀錄。

上面的觀念了解了，我們這就進行程式的實作吧!

PayPal 的付款程序要經過 3 次的 API 呼叫，分別是 SetExpressCheckout,
GetExpressCheckoutDetails, DoExpressCheckoutPayment 。




-   SetExpressCheckout 是整理好一份訂單資訊供消費者瀏覽。


-   GetExpressCheckoutDetails 是抓取當次交易的詳細資訊，但不包含消費者的卡號。


-   DoExpressCheckoutPayment 要求 PayPal 對消費者進行刷卡動作，完成交易。




而消費者瀏覽網頁順序則是『我們的訂單頁面』=>『確定購買』=>『SetExpressCheckout』=>『PayPal 付款頁』=>『PayPal
確認頁』=>『GetExpressCheckoutDetails+DoExpressCheckoutPayment』=>『我們的購買成功頁面』。

我們自己所寫的『確定購買』程式中，會紀錄消費者的購買資訊，產生訂單編號，完成後執行 SetExpressCheckout API
呼叫動作。所謂的呼叫，其實不過就像是 html 中的 form submit 。很懶惰的作法是輸出一個如下的 html
表單，然後要求消費者自己手動按下送出鈕。

::
    ** 1 ****<****form**** ****method****=****"POST"****
    ****action****=****"`https://api-3t.paypal.com/nvp`_"****>**
    ** 2 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"USER"****
    ****value****=****"API_username_do_not_copy_me"****>**
    ** 3 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"PWD"**** ****value****=****"
    API_password_do_not_copy_me"****>**
    ** 4 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"SIGNATURE"****
    ****value****=****"API_signature_do_not_copy_me"****>**
    ** 5 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"L_NAME0"****
    ****value****=****"test_product_name"****>**
    ** 6 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"L_DESC0"****
    ****value****=****"test_description"****>**
    ** 7 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"L_NUMBER0"**** ****value****=****"test1"****>**
    ** 8 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"L_QTY0"**** ****value****=****"1"****>**
    ** 9 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"L_AMT0"**** ****value****=****"85"****>**
    **10 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"ITEMAMT"**** ****value****=****"85"****>**
    **11 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"SHIPPINGAMT"**** ****value****=****"10"****>**
    **12 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"TAXAMT"**** ****value****=****"5"****>**
    **13 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"AMT"**** ****value****=****"100"****>**
    **14 **    **<****input**** ****type****=****"submit"****
    ****name****=****"METHOD"****
    ****value****=****"SetExpressCheckout"****>**
    **15 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"VERSION"**** ****value****=****"63.0"****>**
    **16 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"CURRENCYCODE"**** ****value****=****"TWD"****>**
    **17 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"PAYMENTACTION"**** ****value****=****"Sale"****>**
    **18 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"CANCELURL"****
    ****value****=****"`http://www.YourCancelURL.com`_"****>**
    **19 **    **<****input**** ****type****=****"hidden"****
    ****name****=****"RETURNURL"****
    ****value****=****"`http://www.YourReturnURL.com`_"****>**
    **20 ****</****form****>**


這裡有幾個地方要注意， form method 一定是 POST ， form action 一定是 https://api-
3t.paypal.com/nvp ，input name="METHOD" 的 value 一定是 SetExpressCheckout 。

VERSION 代表你呼叫的 API 版本是多少，版本號太小的 API ，可能會有些參數不支援。不過，以我使用的經驗，上面的參數都能跑在 53 ~ 63
之間。但能設得愈大愈好。

而 CURRENCYCODE 代表收取的幣別， TWD 代表新台幣， USD 代表美金，其他貨幣請參閱`這裡`_。

PAYMENTACTION 的值有三種： Sale, Authorization, Order ， Sale 表一般銷售，消費者要買，你一定賣;
Authorization 表須確認的銷售，如消費者要買 Giant 的 TCR SL 3
車架，但貴公司沒建置庫存管理，所以消費者下單後，你得到大如足球場的倉庫去找，找得到就賣，找不到只好跟消費者 Say Sorry! Order
表須更長時間的確認銷售，像 Authorization 最多只會在帳務管理系統中等 3 天讓你按下請款鈕，但 Order 可以等到 29 天。

CANCELURL 是當消費者在 PayPal 付款頁中，反悔了，在他取消交易時， PayPal 會導引他回到你的網站。

RETURNURL 是當消費者在 PayPal 確認頁按下「立即付款」， PayPal 會導引他回到你的網站，理論上，這個網頁就是你執行
GetExpressCheckoutDetails + DoExpressCheckoutPayment 的地方。

從這個 html form 範例中，可以了解呼叫 SetExpressCheckout API 真的是非常簡單的事，只要把握正確的 name -
value pair(nvp) 即可。

不過我們是 Python 程式設計師，怎麼能用 html form 這麼簡單的東西來呼叫 API ，當然要用 urllib 囉!
把下面的程式插到『確定購買』程式的最後面，這樣就不用消費者自己手動按送出鈕了。

::
    ** 1 ****from** google.appengine.api **import** urlfetch
    ** 2 ****import** urllib
    ** 3 **
    ** 4 **string_hash = {
    ** 5 **    **"USER"**: **"API_username_do_not_copy_me"**, **"PWD"**:
    **" API_password_do_not_copy_me"**,
    ** 6 **    **"SIGNATURE"**: **"API_signature_do_not_copy_me"**,
    **"L_NAME0"**: **"test_product_name"**,
    ** 7 **    **"L_DESC0"**: **"test_description"**, **"L_NUMBER0"**:
    **"test1"**, **"L_QTY0"**: **"1"**,
    ** 8 **    **"L_AMT0"**: **"85"**, **"ITEMAMT"**: **"85"**,
    **"SHIPPINGAMT"**: **"10"**, **"TAXAMT"**: **"5"**,
    ** 9 **    **"AMT"**: **"100"**, **"METHOD"**:
    **"SetExpressCheckout"**, **"VERSION"**: **"63.0"**,
    **10 **    **"CURRENCYCODE"**: **"TWD"**, **"PAYMENTACTION"**:
    **"Sale"**,
    **11 **    **"CANCELURL"**: **"`http://www.YourCancelURL.com`_"**,
    **12 **    **"RETURNURL"**: **"`http://www.YourReturnURL.com`_"**,
    **13 **}
    **14 **form_data = urllib.urlencode(string_hash)
    **15 **result = urlfetch.fetch(url=**'`https://api-
    3t.paypal.com/nvp`_'**,
    **16 **    payload=form_data,
    **17 **    method=urlfetch.POST,
    **18 **    headers={**'Content-Type'**: **'application/x-www-form-
    urlencoded'**},
    **19 **    deadline=**10**)
    **20 **
    **21 **hash = {}
    **22 ****for** i **in** result.content.split(**'&'**):
    **23 **    k, v = i.split(**'='**)
    **24 **    hash[k] = urllib.unquote(v)
    **25 **
    **26 **redirect_url = **'`https://www.paypal.com/cgi-bin/webscr?cmd
    =_express-checkout&useraction=commit&token=%s`_'** % hash[**'TOKEN'**]
    **27 ****return** HttpResponseRedirect(redirect_url)


跑到 redirect_url 網址後，就是 PayPal 自己與消費者互動的網頁，等到消費者確定付款了，就會再轉回我們的 RETURNURL 程式。在
RETURNURL 頁面中，首先呼叫 GetExpressCheckoutDetails 得到該 token 所對應的付款資訊。然後再執行
DoExpressCheckoutPayment 即可完成信用卡刷卡動作。

::
    ** 1 ****# exec GetExpressCheckoutDetails**
    ** 2 **token = request.GET.get(**'token'**)
    ** 3 **string_hash = {
    ** 4 **    **"USER"**: **"API_username_do_not_copy_me"**, **"PWD"**:
    **" API_password_do_not_copy_me"**,
    ** 5 **    **"SIGNATURE"**: **"API_signature_do_not_copy_me"**,
    **"METHOD"**: **"GetExpressCheckoutDetails"**,
    ** 6 **    **"VERSION"**: **"63.0"**, **"TOKEN"**: token,
    ** 7 **}
    ** 8 **form_data = urllib.urlencode(string_hash)
    ** 9 **result = urlfetch.fetch(url=**'`https://api-
    3t.paypal.com/nvp`_'**,
    **10 **    payload=form_data,
    **11 **    method=urlfetch.POST,
    **12 **    headers={**'Content-Type'**: **'application/x-www-form-
    urlencoded'**},
    **13 **    deadline=**10**)
    **14 **
    **15 **hash = {}
    **16 ****for** i **in** result.content.split(**'&'**):
    **17 **    k, v = i.split(**'='**)
    **18 **    hash[k] = urllib.unquote(v)
    **19 **
    **20 ****if** hash[**'ACK'**] != **'Success'**:
    **21 **    error_messages = []
    **22 **    **for** k, v **in** hash.items():
    **23 **        error_messages.append(**'%s: %s'**%(k, v))
    **24 **    **raise**
    Exception(**';****\n****'**.join(error_messages))
    **25 **
    **26 ****# exec DoExpressCheckoutPayment**
    **27 **string_hash = {
    **28 **    **"USER"**: **"API_username_do_not_copy_me"**, **"PWD"**:
    **" API_password_do_not_copy_me"**,
    **29 **    **"SIGNATURE"**: **"API_signature_do_not_copy_me"**,
    **"METHOD"**: **"DoExpressCheckoutPayment"**,
    **30 **    **"VERSION"**: **"63.0"**, **"TOKEN"**: token,
    **31 **    **"AMT"**: **"100"**, **"CURRENCYCODE"**: **"TWD"**,
    **32 **}
    **33 **form_data = urllib.urlencode(string_hash)
    **34 **result = urlfetch.fetch(url=**'`https://api-
    3t.paypal.com/nvp`_'**,
    **35 **    payload=form_data,
    **36 **    method=urlfetch.POST,
    **37 **    headers={**'Content-Type'**: **'application/x-www-form-
    urlencoded'**},
    **38 **    deadline=**10**)
    **39 **
    **40 **hash = {}
    **41 ****for** i **in** result.content.split(**'&'**):
    **42 **    k, v = i.split(**'='**)
    **43 **    hash[k] = urllib.unquote(v)
    **44 **
    **45 ****if** hash[**'ACK'**] != **'Success'**:
    **46 **    error_messages = []
    **47 **    **for** k, v **in** hash.items():
    **48 **        error_messages.append(**'%s: %s'**%(k, v))
    **49 **    **raise**
    Exception(**';****\n****'**.join(error_messages))
    **50 **
    **51 ****return**
    HttpResponseRedirect(**'`http://www.YourThankURL.com/`_'**)


就這樣，你會在 PayPal 的帳務管理系統中，看到消費者的付款紀錄。

.. _簡述金流系統: http://hoamon.blogspot.com/2011/01/blog-post_24.html
.. _文章: http://hoamon.blogspot.com/2011/01/paypal-express-checkout-
    api.html
.. _https://api-3t.paypal.com/nvp: https://api-3t.paypal.com/nvp
.. _http://www.YourCancelURL.com: http://www.YourCancelURL.com
.. _http://www.YourReturnURL.com: http://www.YourReturnURL.com
.. _這裡: https://cms.paypal.com/us/cgi-bin/?cmd=_render-
    content&content_ID=developer/e_howto_api_nvp_currency_codes
.. _token=%s: https://www.paypal.com/cgi-bin/webscr?cmd=_express-
    checkout&useraction=commit&token=%s
.. _http://www.YourThankURL.com/: http://www.YourThankURL.com/


Old Comments in Blogger
--------------------------------------------------------------------------------



`vossler <http://www.blogger.com/profile/10599877872124155310>`_ at 2012-03-23T15:56:31.316+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hi hoamon,

如果我們使用paypal api的話，是否user在結帳時 無須登入paypal頁面，在自身網站頁面就可結帳呢?

因台灣我們的客戶群不是每家公司都會有paypal 帳號，所以要結帳時，又需要申請paypal帳號，對user端來說不是相當麻煩嗎?

`何岳峰 <http://www.blogger.com/profile/03979063804278011312>`_ at 2012-03-23T16:55:58.104+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

這裡有個範例( http://iclean.bio-enzyme.com/hmn/ )，消費者不用登入就能使用信用卡付款，但一定得到 PayPal
的網頁填寫卡號。當然 PayPal 也有讓商家自行處理卡號的付款方式，但我懷疑臺灣商家可以申請。

.. author:: default
.. categories:: chinese
.. tags:: paypal, python
.. comments::
將三個網址全托管給同一個 GAE(google app engine) 程式
================================================================================

在我還將網頁程式全部放在 Ubuntu 中以 Apache 服務時，針對不同類型的資料，我會給定不同的網址像是： www.hoamon.info,
down.hoamon.info, ssvn.hoamon.info, book.hoamon.info
…等。但是現在我的策略是把所有個人化的網站全部交給 GAE 處理。

既然如此，難道我要一個網址就開一個 GAE spot 嗎? 如果我的各項個人化網站的資料是超過 500mb 的話，在不想花錢的情況下，的確是一個網站開一個
GAE spot ，但我的個人化網站的資料量都不大，這麼作太浪費了。

這次我想整合的網址是 down.hoamon.info, ssvn.hoamon.info
，它們兩個網址原本就只是在作靜態檔案的分享，一個是鬆散無結構化集成的檔案，另一個則是有作 subversion 管理的檔案。

因為在我其他已存在的文章、網頁以及我正使用的名片上，早就標明那些檔案的下載網址，像是：
`http://ssvn.hoamon.info/OpenTrunk/hoamon.pgp.asc`_ 、
`http://down.hoamon.info/resume070403.tex`_ …等。所以我不能變更這些已存在的 url ，而是讓 GAE
能分辦那些 url 要求是要跑到原本 www.hoamon.info spot 的，那些 url 則是直接以靜態方式存取的。

我打算讓 http://down.hoamon.info/(.*) 的 url 會被 redirect 成
http://down.hoamon.info/_d/(.*); 而 http://ssvn.hoamon.info/(.*) 的 url 則被
redirect 成 http://ssvn.hoamon.info/_s/(.*) 。

這樣我就能在 app.yaml 設定如下：
::
    ...
    ...
    ...
    - url: /_s
    static_dir: ssvn_dir

    - url: /_d
    static_dir: down_dir
    ...
    ...
    ...
    - url: /.*
    script: index_views.py

那麼如何讓 down.hoamon.info 開頭的網址能 redirect 成 down.hoamon.info/_d 的呢? 我們就必須在
index_views.py 動手腳了。在 GAE 中，要讓 python 程式得取目前的 http request 是以什麼 url
作要求的，就是從這個變數 request.headers['HOST'] 下手，不過這個變數目前好像只存在於 webapp.RequestHandler
中，所以我處理的方式如下：
::
    class Index(webapp.RequestHandler):
     def get(self, args):
         # 在這裡判斷使用者要看的是那一個網站，然後再作 redirect 的動作。
         HTTP_HOST = self.request.headers['HOST']
         if 'down.hoamon.info' == HTTP_HOST:
            self.redirect('/_d/%s' % args)
         elif 'ssvn.hoamon.info' == HTTP_HOST:
            self.redirect('/_s/%s' % args)
         # end

         ...

    _DEBUG = True
    application = webapp.WSGIApplication([
         ('/(.*)', Index),
     ], debug=_DEBUG)

    def main():
     run_wsgi_app(application)

因為我只會在 webapp.RequestHandler.request.headers['HOST'] 中抓到使用者要求網址，所以就會把
dispatch 邏輯寫在 view(MTV)/controller(MVC) 中，這樣的程式能完成工作但不算漂亮。

GAE spot 的程式完成後，記得還要把 down.hoamon.info, ssvn.hoamon.info CNAME 到
ghs.google.com *，這樣就成功合併了。

PS1 額外提醒! 這個動作是要到你的 domain name 服務商的設定介面處理。不過，你也得在 GAE 的 [admin 介面]
> [Versions]
> [Add Domain]
> [填入 hoamon.info(請不要照填 hoamon.info ，這是我的托管給 google apps
的網址，你的一定不是這個。且作這一步驟，你得先有 `Google Apps 帳戶`_才行)]
> [填入密碼]
> [Add new url(像是 down.hoamon.info, ssvn.hoamon.info 等)]
才行。

.. _http://ssvn.hoamon.info/OpenTrunk/hoamon.pgp.asc:
    http://ssvn.hoamon.info/OpenTrunk/hoamon.pgp.asc
.. _http://down.hoamon.info/resume070403.tex:
    http://down.hoamon.info/resume070403.tex
.. _Google Apps 帳戶: http://hoamon.blogspot.com/2007/05/google_12.html


.. author:: default
.. categories:: chinese
.. tags:: linux, google app engine
.. comments::
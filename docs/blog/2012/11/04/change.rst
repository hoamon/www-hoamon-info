================================================================================
人生必須不停地改變 - 新部落格開站宣言
================================================================================

.. figure:: sphinx.png

    本圖( sphinx.png )非屬 hoamon 創作，引用自 http://sphinx-doc.org/

改變的好叫『祖上積德』，改變的差叫『政府無能』。\
困難的是人們往往不知道是什麼時候變及變什麼，但如果只會講：『Yes, We Can Change』，\
而不知道要變什麼、怎麼變，那就只是喊喊口號而已。

格主因為人生進入另一個階段，所以把 `個人網站 <http://www.hoamon.info/>`_
從 `Python <http://www.python.org>`_ 生成的動態網頁系統改成 `Sphinx <http://sphinx.pocoo.org/>`_
生成的靜態網頁系統。在試用一段時間之後，\
也打算把其他個人相關的網站及部落格一併轉成 Sphinx-based 的架構。\
使用同一種工具當然可降低維護成本。但為什麼是挑 Sphinx 呢?

.. more::


過去格主在寫作部落格文章時，就一直希望把版本控制的概念放進來，這也是本部落格主題的命名原因。\
在這裡寫下的文章常常是即興、電光火石，經過時間的沉澱必須再作修改的。然而在文章初發佈之際，\
若是有讀者留下意見，而我又作了修改，那麼新讀者可能會迷失在文章與留言的不對稱上。或是，\
文章發佈前，還是草稿時，我會修修改改，如果能配合版本控制器的話，那無非能大幅提升寫作效率。

這個想法，停留在我腦中有很長的一段時間，久到不用自己再創個輪子，別人已經幫我們寫好了，\
而且它還是用 Python 寫出來的工具。

Sphinx 主要是一個 ReST 文件的轉換器。我們先用 ReST 格式寫文件，\
待發佈時， Sphinx 可以幫我們生成 .tex, .html, .pub, .pdf 等格式文件，\
所以我們作者只需依 ReST 結構費心文章寫作，後端的出版編輯就交給 Sphinx 。\
而因為 ReST 文件也不過就是純文字文件，所以它非常適合躺在版本控制器中。\
我的個人網站就是開在 `Github <https://github.com/hoamon/www-hoamon-info>`_ 中控管的。

但 Sphinx 只能幫我們把 .rst 轉成 .html ， Blog 系統則還需要其他服務，像是 RSS 分享, \
時間序列文章列表等，所以我們需要裝個 `Tinkerer <http://www.tinkerer.me/>`_ 外掛來幫我們作到。

安裝方式：

::

    # easy_install -U Tinkerer

conf.py 設定範例：

::

    project = "hoamon's sandbox"
    tagline = '"sandbox" is a jargon of Version Control System.'
    author = 'hoamon'
    copyright = '2006-2012, ' + author
    website = 'http://www.hoamon.info/blog/'
    disqus_shortname = "hoamoninfo"
    html_favicon = 'favicon.ico'
    html_theme = "modern5"
    html_theme_options = { }
    rss_service = None
    posts_per_page = 10
    html_sidebars = {
        "**": ["recent.html", "searchbox.html", "categories.html", "tags.html"]
    }

使用方式：

::

    # tinker -s                 # 在本目錄建立 tinkerer-based 寫作平台
    # tinker -d "article title" # 在 ./drafts/ 下，建立一個 article_title.rst
    # tinker -p "article title" # 建立一個 ./YYYY/MM/DD/article_title.rst 的文件
    # tinker -b                 # 匯出整個 Blog 的靜態文件到 ./blog/html

這樣我們就只要專心在 .rst 文件上寫作，用 hg 作版本控制，完稿後用 tinker -b
自動發佈成一個靜態網頁的資料夾，再上傳到網站空間就行了，不只省下我們自己的寫作時間，\
也節省網站的 CPU 運算能量。

計劃把 http://blog.hoamon.info/ 文章全部轉移至 `http://www.hoamon.info/blog/ </blog/>`_ 這裡，\
而該 Blogger 站台的文章近 500 篇，我預計在 2013-12-31 前移轉完畢，\
完成後 http://blog.hoamon.info/ 將只作代轉服務，一律把舊連結如 http://blog.hoamon.info/index.html
轉成 `http://www.hoamon.info/blog/index.html </blog/index.html>`_ ，敬請舊雨新知互相走告。

最後我只有一個結語：『 Open Source is So Good 』。

.. author:: default
.. categories:: chinese
.. tags:: aboutme
.. comments::

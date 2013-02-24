================================================================================
本專案說明(正體中文版)
================================================================================

--------------------------------------------------------------------------------
授權條款
--------------------------------------------------------------------------------

為 new BSD 授權( 3-clause )。

--------------------------------------------------------------------------------
目的
--------------------------------------------------------------------------------

把創建一個軟體專案所需要的常用檔案及結構定義好，方便取用。\
主要是給 django-based 系統使用，\
同時可套用在「自架機器」或「GAE hosting」的「應用專案」上。

.. note:: 名詞定義

 1. 「本專案」指的是 ho600-django-gae-default-trunk 專案
 2. 「應用專案」指的是您把 ho600-django-gae-default-trunk 所有檔案複製成新開發專案的那個專案

本專案的檔案架構配置如下：

.. code-block:: bash

    ho600-django-gae-default-trunk/
                                    asset/
                                    bin/
                                    conf_example/
                                    docs/
                                    docs-of-ho600-django-gae-default-trunk/
                                    ho600_lib/
                                    H6_lib/
                                    trunk/
                                            depends_modules/
                                            modules/
                                            local_settings.py

asset/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

放置第三方的函式庫， ./depends_modules.conf 則紀錄應該要抓取那些專案到 asset/ 中。\
內容如下：

.. code-block:: python
    :linenos:

    # ./depends_modules.conf
    asset/django-mediagenerator:tip = ssh://hg@bitbucket.org/wkornewald/django-mediagenerator
    asset/django-tastypie:XXXYYYZZZ = git://github.com/toastdriven/django-tastypie.git

若有其他想要加入的模組，可自行加在 depends_modules.conf 中\
XXXYYYZZZ 代表特定版本的 changeset 碼，若無設定代表 tip ，\
有設定 XXXYYYZZZ 後，則該模組就只會 update 至該版本。但 pull 時還是會抓到 tip 版。

.. note::

    目前僅支援 mercurial 儲存庫。若是使用 GitHub 專案請參考 \
    `hg-git <http://hg-git.github.com/>`_ 。

預設載入 django-mediagenerator, django-tastypie, django-guardian, django-debug-toolbar 等四個 django-based 模組，\
另外載入 jstree, jQuery-URL-Parser 等二個 js 函式庫。

bin/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

執行命令有：

prepare_programming.py
................................................................................

每次在撰寫自己的應用專案前，所執行的指令。\
幫你把 depends_modules.conf 中所指定的專案程式更新到指定版本。\
並提醒你還有那些 hg repo 尚未 commit 。

更新完所需的 moduels 後，也同時把 trunk/depends_modules/ 中的 modules \
(有登記在 settings.INSTALLED_APPS 及 settings.ANOTHER_DEPENDS_MODULES ) 刪除，以確保在開發程式時，\
所載入的 module 一定是 settings.py 中有指定特別版本、特別位置的 module 。

又如果專案程式並不是使用 hg 或 git 控管，而是單用 .zip 儲存。則也用使用 [downloads] 作設定。

下載後的專案及檔案，可再利用 [copies] 設定將部份資料文件複製到其他位置中。

.. code-block:: conf

    [downloads]
    asset/Project = https://yoursite.com/yourfile.zip

    [copies]
    trunk/modules/p1/file.txt = asset/Project/file/example.conf

上面的範例是將 https://yoursite.com/yourfile.zip 下載下來，解壓縮到 asset/Project 資料夾。\
並把 asset/Project/file/example.conf 檔案複製到 trunk/modules/p1/file.txt 中。

before_deployment.py
................................................................................

要上傳至 production server 前所執行的指令，\
也是未來 jenkins 執行的指令。

這裡的行為主要是把 settings.INSTALLED_APPS 及 settings.ANOTHER_DEPENDS_MODULES 有登記的 \
modules (扣除 django 自己帶入的)，複製一份到 trunk/depends_modules/ 。\
這樣在 deployment 時，只需把 trunk/ 整包上傳即可。

symbol_to_unicode.py
................................................................................

django dumpdata 的內容，在非 ASCII 編碼下，它會顯示 \\u65b0 ，而非「新」這個字。\
執行如下指令：

.. code-block:: bash

    $ bin/symbol_to_unicode.py old.json > new.json

則 new.json 內容會是一般人看得懂的文字，而不是 \\uXXXX 。

monitor_file_and_make_html.sh
................................................................................

觀察特定資料夾內文件是否有修改，若有修改則立即執行 make html 指令( sphinx )，\
執行方式如下：

.. code-block:: bash

    $ bin/monitor_file_and_make_html.sh docs-of-ho600-django-gae-default-trunk

執行後，它會持續等待，當 docs-of-ho600-django-gae-default-trunk/ 內有文件被更新，\
則在該資料夾自動編譯 document 。

.. note::

    本程式只能在 Unix-like 系統中執行。

conf_example/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

放置 Apache+wsgi 及 Nginx+uWSGI 的設定範例檔。建議使用時，\
是將所需 apache2.conf 或 nginx.conf 檔案複製到 trunk/ 中，\
並在系統的 apache.conf 內使用：

.. code-block:: apache
    :linenos:

    # YOUR_SYSTEM_APACHE/httpd.conf
    Include "WHERE_YOU_PUT_CONF_DIR/apache2.conf"

或是在系統的 nginx.conf 內使用：

.. code-block:: nginx
    :linenos:

    # YOUR_SYSTEM_NGINX/nginx.conf
    Include "WHERE_YOU_PUT_CONF_DIR/nginx.conf"

其中因為 nginx 是結合 uWSGI 一起使用的，所以需另外設定 uwsgi 設定檔：

.. code-block:: ini
    :linenos:

    ## /etc/uwsgi/apps-enabled/www.ini
    ## sudo invoke-rc.d uwsgi start
    ## sudo invoke-rc.d uwsgi stop
    ## sudo invoke-rc.d uwsgi restart
    ##
    [uwsgi]
    socket = /var/run/uwsgi/app/www/socket
    chmod-socket = 666
    limit-as = 256
    processes = 6
    max-request = 2000
    memory-report = true
    enable-threads = true
    pythonpath = /YOUR_PROJECT_DIR/
    chdir = /YOUR_PROJECT_DIR/
    wsgi-file = /YOUR_PROJECT_DIR/wsgi.py

docs/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

為 sphinx-based 的文件資料夾。給「應用專案」使用的預設文件寫作位置，\
當然也可以全刪除不使用或是自行再利用 sphinx-quickstart 生成一個。

docs-of-ho600-django-gae-default-trunk/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本專案的文件所在處。

ho600_lib/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

方便作 django-based 程式開發的函式庫，主要有 bugrecord 功能，在執行程式時，\
若發生 404|500 錯誤時，能紀錄在資料庫內。

樣版選擇順序: get_template_by_site_and_lang
................................................................................

.. todo::

    @hoamon: 先直接看程式碼

樣版中 static/media 檔案的 url 找尋
................................................................................

.. todo::

    @hoamon: 先直接看程式碼

得知使用者以什麼網域名稱瀏覽： get_site_from_settings
................................................................................

.. todo::

    @hoamon: 先直接看程式碼

PostCode Model
................................................................................

郵遞區號的資料表，目前已放置臺灣 3 碼郵遞區號資料( ho600_lib/fixtures/taiwan_postcode.json )，\
資料來源版本為 `http://download.post.gov.tw/post/download/臺灣地區郵遞區號前3碼一覽表_9912.xls
<http://download.post.gov.tw/post/download/臺灣地區郵遞區號前3碼一覽表_9912.xls>`_ (2011/8/15 version) 。\

使用方式是在你自己所寫 moduels 的 models.py 建立另一個 model ，如：

.. code-block:: python

    # filename: mymodules/models.py
    from ho600_lib.models impor PostCode as PC
    class PostCode(PC):
        pass

這樣在 syncdb 後，資料庫會產生一個 mymodules_postcode 資料表。若是需要使用 taiwan_postcode.json 資料，\
則先把 ho600_lib/fixtures/taiwan_postcode.json \
複製到 mymodules/fixtures/my_taiwan_postcode.json ，一定要更名，要不然系統上會同時有兩個 taiwan_postcode.json。

my_taiwan_postcode.json 中的 model: "ho600_lib.postcode" 須修改為 model: "mymodules.postcode"，\
再來執行 ./manage.py loadddata my_taiwan_postcode.json ，就可把臺灣 3 碼郵遞區號資料匯入 mymodules_postcode 資料表。

其中，要注意的是 PostCode.id 並不是用連續自然數為值，而是要自定的且必須為 unique 。\
如： “臺灣” 的 id 為 "tw000"、\
"臺北市" 為 "tw001" ，而 "臺中市南區" 為 "tw402“ 。但因為 ”新竹市“ 、 "嘉義市" 全市只有 1 個郵遞區號，\
前者為 300 ，後者為 600 ，所以 "新竹市北區“ 的 id 為 “tw300-北區” ， "嘉義市東區" 的 id 為 “tw600-東區” 。\
也就是把 parent.id + self.name 作為 self.id 。

id 不為連續自然數的好處，在於系統資料要作統整時，不同來源的 PostCode 其 id 勢必為相同。

H6_lib/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

為商業套件，並不是以 new BSD 授權發佈。

trunk/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

這裡是執行 ./manage.py runserver 0.0.0.0:8080 的地方，若要執行 GAE-based 的應用專案，\
則到上層目錄執行 dev_appserver.py . -a 0.0.0.0 -p 8080 。

trunk/depends_modules/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在使用 jenkins 發佈應用專案時，利用 bin/before_deployment.py 可將 \
settings.INSTALLED_APPS 中所需的 modules (扣除 django 自己的)全複製到 \
trunk/depends_modules/ 下。這樣 jenkins 發佈時，就只需要把 trunk/ 上傳至伺服器。\
目標伺服器就不需要預先安裝特定 pure-python 函式庫，\
但還是要裝 django 函式庫以及其他需事先編譯的函式庫如： PIL 、 numpy 、 scipy …等。

trunk/modules/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

配置應用專案所開發的 modules 位置。不過如果「應用專案」本身並不是一個獨立網站，\
而是以 module 的形式存在者，建議是把 module 配置與 ho600_lib 同一層級，也就是根目錄的位置。

trunk/local_settings.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

不被 hg 控管的本地設定檔，本檔案所設定的參數會覆蓋 trunk/settings.py 的設定，\
但設定時，有一限制： 在 local_settings 的參數名稱必須預先存在 trunk/settings.py 中，\
這是確保開發者在本地自行開發後，也必須記得把該參數登記到 trunk/settings.py ，\
以利其他開發者更正自己的 trunk/settings.py 。

--------------------------------------------------------------------------------
實際應用範例
--------------------------------------------------------------------------------

到 `https://bitbucket.org/hoamon/ho600-django-gae-default-trunk/downloads <https://bitbucket.org/hoamon/ho600-django-gae-default-trunk/downloads>`_ \
這裡點選 Tags 頁面，下載所需的 ho600-django-gae-default-trunk 版本。也可以是用 \
hg clone ssh://hg@bitbucket.org/hoamon/ho600-django-gae-default-trunk \
指令再配合 hg update -C 'release-1.X.X' 來使用。

得到 ho600-django-gae-default-trunk 資料夾後，先把它改名成自己的應用專案，像是： \
my-example ，並刪除 .hg 資料夾及 .hgtags 檔案，\
這是 ho600-django-gae-default-trunk 版本控制庫所使用的檔案，\
如是從 bitbucket downloads 頁面下載的，則無此資料夾。

修改 ./depends_modules.conf 。而後執行：

.. code-block:: bash

    hoamon@localhost my-example # bin/prepare_programming.py

修改 trunk/settings.py 。而後執行：

.. code-block:: bash

    hoamon@localhost my-example/trunk # ./manage.py runserver 0.0.0.0:8080

然後你可以在瀏覽器中看到：

.. figure:: _static/hello.png

接下來修改 trunk/urls.py (先把 urls.ho600_default_view 移除)，\
刪除 trunk/__docs__ 、 ./docs-of-ho600-django-gae-default-trunk/ 。

如果你的應用專案是 gae-based 的，那請再修改 ./app.yaml 檔案。且利用下列指令在本地端開發。

.. code-block:: bash

    hoamon@localhost my-example # dev_appserver.py . -a 0.0.0.0 -p 8080

現在你可以在 trunk/moduels/ 加入自己的模組了。恭喜你!
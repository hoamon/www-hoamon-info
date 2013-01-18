難道我真的是 Windows 白癡! 搞個 https 憑證花了一個上午還是沒成功
================================================================================

照著這位仁兄的筆記： http://blog.roodo.com/myroodo/archives/4219557.html ，就是會在最後一個指令

> openssl ca -config openssl.cnf -days 3650 -cert ssl/ca.crt -keyfile
ssl/ca.key -in ssl/server.csr -out ssl/server.crt

出現

I am unable to access the ssl
ewcerts directory
ssl
ewcerts: Invalid argument

查了相當多的地方，也找不出原因。後來想想，這不過是個憑證，它是一種資料，所以它應該與平台無關，且之前我在 Linux
上作了那麼多的憑證，也沒遇過機器重灌，憑證得重作的現象，所以它應與當時製作的平台也無關，索性在 Ubuntu 上打了三個指令，作出憑證，再送到
Windows 去用。

您猜猜，這麼著了?

It's Work~

Old Comments in Blogger
--------------------------------------------------------------------------------



`雨蒼 <http://www.blogger.com/profile/15287359091259963633>`_ at 2009-02-10T20:48:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Windows自己也有發憑證的伺服器
叫做CA Server

搭配IIS使用，要在網頁上申請，然後到控制中心核准，再去網頁上下載這樣。

熟悉一點的話還是到Linux上打指令比較方便XD
反正CA就是CA，到哪邊都一樣

.. author:: default
.. categories:: chinese
.. tags:: linux, ssl, windows, apache, ubuntu
.. comments::
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

.. author:: default
.. categories:: chinese
.. tags:: linux, ssl, windows, apache, ubuntu
.. comments::
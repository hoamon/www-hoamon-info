apache2 + ssl on ubuntu 7.04
================================================================================

和 Fedora 的設定方式稍有不同。

1. 產生認證檔案
sudo mkdir /etc/apache2/ssl
sudo make-ssl-cert /usr/share/ssl-cert/ssleay.cnf /etc/apache2/ssl/apache.pem

2. 修改設定檔案 /etc/apache2/sites-available/ssl
NameVirtualHost *:443
<virtualhost *:443>
　　ServerAdmin `webmaster@localhost`_
　　...
　　...
　　SSLEngine On
　　SSLCertificateFile /etc/apache2/ssl/apache.pem
</virtualhost>

3. 重新啟動 Apache 伺服器
sudo /etc/init.d/apache2 restart

.. _webmaster@localhost: mailto:webmaster@localhost


.. author:: default
.. categories:: chinese
.. tags:: linux, ssl, apache, ubuntu
.. comments::
管理apache的基本觀念
================================================================================

::
    [[1]].網頁伺服器基本原理及設定
    [[2]].進階模組說明及設定
    [[3]].效能調校

    1.網頁伺服器基本原理及設定

    伺服器和瀏覽器的溝通

      TCP/IP協定及HTTP協定
        Client 端先經過 DNS 解析得到 WWW 主機的 IP ，然後會發出一個資料封包，
        告知 WWW 主機我們要進行交涉，這個時候使用的是 TCP 協定，
        亦即需要經過三向交握的過程。
        三向交握：Client 端與 Server 端在經過了要求主動建立(SYN)、
        回覆確認封包(SYN/ACK)、
        再次確認(ACK)，最後建立起兩邊的相關埠口的連線，由於為了建立起最終的連線，
        需要進行三次封包的要求與確認，因此我們也稱這個建立連線前的步驟為
        『三向交握, Three-way handshake』。
      主機端資料處理
        連線建立後，客戶端以http協定傳送需求。
        WWW 主機收到這個資料封包之後，會根據 Client 端的要求，
        提供相關的訊息來回應，
        大部分的情況下皆是使用 http 的協定回應傳送具有 HTML
        語法的網頁資料到 Client 端的瀏覽器上。
      客戶端資料處理
        Client 端的瀏覽器將 HTML 的語法經過解析後，以相關的畫面來顯示到螢幕上，
        提供用戶來觀賞。

      例子一 http/1.0：

      [amon@amon amon]$ telnet www.apache.org 80
          Trying 209.237.227.195...
          Connected to www.apache.org (209.237.227.195).
          Escape character is '^]'.
      GET http://www.apache.org/[[enter]]
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
          Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <!--
          Copyright 1999-2004 The Apache Software Foundation
          Licensed under the Apache License, Version 2.0 (the
          "License");
          you may not use this file except in compliance with the
          License.
          You may o.................................

      例子二 http/1.1：

      [amon@amon amon]$ telnet www.apache.org 80
          Trying 209.237.227.195...
          Connected to www.apache.org (209.237.227.195).
          Escape character is '^]'.
      GET http://www.apache.org/ HTTP/1.1[[enter]]
      Host: www.apache.org/foundation/members.html[[enter]]
      [[enter]]
          <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
          Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
          <!--
          Copyright 1999-2004 The Apache Software Foundation
          Licensed under the Apache License, Version 2.0 (the
          "License");
          you may not use this file except in compliance with the
          License.
          You may o.................................
      GET http://www.apache.org/ HTTP/1.1[[enter]]
      Host: www.apache.org/foundation/members.html[[enter]]
      [[enter]]

    apache基本架構

      Core模組
      # AcceptPathInfo # AccessFileName # AddDefaultCharset

      # AddOutputFilterByType # AllowEncodedSlashes # AllowOverride

      # AuthName # AuthType # CGIMapExtension # ContentDigest

      # DefaultType # <directory> # <directorymatch> # DocumentRoot

      # EnableMMAP # EnableSendfile # ErrorDocument # ErrorLog

      # FileETag # <files> # <filesmatch> # ForceType # HostnameLookups

      # IdentityCheck # <ifdefine> # <ifmodule> # Include # KeepAlive

      # KeepAliveTimeout # <limit> # <limitexcept> #
      LimitInternalRecursion

      # LimitRequestBody # LimitRequestFields # LimitRequestFieldSize

      # LimitRequestLine # LimitXMLRequestBody # <location>

      # <locationmatch> # LogLevel # MaxKeepAliveRequests

      # NameVirtualHost # Options # Require # RLimitCPU # RLimitMEM

      # RLimitNPROC # Satisfy # ScriptInterpreterSource # ServerAdmin

      # ServerAlias # ServerName # ServerPath # ServerRoot #
      ServerSignature

      # ServerTokens # SetHandler # SetInputFilter # SetOutputFilter

      # TimeOut # UseCanonicalName # <virtualhost>


      MPM模組(Multi-Processing Modules)
      apache運行機制有非常多種，乃因作業系統不同，對行程管理的方式不同所導致。
      粗分三類，依啟動一父行程後，其子行程運行方式可分為
      #prefork(前分流式)
        父行程啟動後，便生成特定數量之子行程，而每一子行程可處理一個請求。
        父行程本身只有管理子行程。
      #threaded(執行緒式)
        父行程啟動後，便生成特定數量之子行程，但每一子行程為多執行緒，
        故可一個子行程服務多個客戶端請求。
      #winnt(中文沒得翻)
        父行程啟動後，完全由它來服務所有的客戶端請求。
      MPM乃依作業系統習性不同，所分別設計的模組，
      斷無將prefork module應用在win server上，效能能有所提升，
      因為根本跑不起來。但是一個可以用threaded module的apache也可以使用
      prefork module。

      else
      (其他模組)
      #mod_so
      #mod_cgi
      #mod_cgid
      #mod_userdir
      #mod_speling
      (貢獻模組)
      #mod_perl
      #mod_ssl
      #mod_php

    簡單的設定檔
      ServerName 192.168.100.103:8080
      Listen 8080
      DocumentRoot /home/amon/httpd/htdocs/
      TransferLog /home/amon/httpd/logs/access_log
      Alias /manual /home/amon/httpd/manual
      DefaultType text/plain
      <location>
        Options -Indexes -Multiviews
        AllowOverride None
        DirectoryIndex index.html
      </location>

    2.進階模組說明及設定

    目前預設的MPM模組為perfork(前分流式)
      前分流式MPM是模擬apache1.3或更早以前的架構，也就是建立一池的子行程來服務請求。
      每一個子行程都是單一的執行緒。例如，如果apache啟動30個子行程，
      就表示apache可以同時服務30個請求。
      如果出了什麼差錯，或者某個子行程死去了，就只有一道請求會遺失而已。
      至於子行程的數量是由一組最大和最小指令來設定的。當請求的數量增加時，
      新的子行程就會不斷的新生出來，直到到達最大值為止。同樣的，當請求數量下降時，
      多餘的子行程也會被刪除。

      User：子行程的擁有者。
      Group：子行程的群組擁有者。
      MaxClients(最大服務請求數)：預設值為256。
      MaxSpareServers(最大等待請求數)：預設值為10。
      MinSpareServers(最小等待請求數)：預設值為5。
      StartServers(啟始等待請求數)：預設值為5。
      CoreDumpDirectory(核心頃印資料夾)：預設值為null。
      ListenBacklog：預設值為511。等待連結請求的佇列長度。
      SendBufferSize：tcp傳送緩衝區的大小。如果網路頻寬夠，應該儘量大一點。
      ScoreBoardFile：為父行程與子行程溝通時所用的檔案。


.. author:: default
.. categories:: chinese
.. tags:: apache
.. comments::
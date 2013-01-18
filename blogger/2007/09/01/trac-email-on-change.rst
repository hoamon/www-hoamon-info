讓 Trac 支援 Email on Change
================================================================================

當 Trac 系統上有人增加/修改了一篇 wiki 、 ticket ，它能直接以 email 的方式讓其他人知道。

方法是：只要在 trac.ini 中編輯以下選項即可。

smtp_enabled = true
smtp_server = localhost
smtp_from = dontreply@mailserver
smtp_replyto = dontreply@mailserver
smtp_always_cc = XXX@gmail.com, YYY@gmail.com
always_notify_owner = true # 任何改變也會寄給「被指派的人」
always_notify_reporter = true # 任何改變也會寄給「創ticket的人」
always_notify_updater = true # 寄給改變這個 ticket 狀態的人

smtp_server 是寄信伺服器，如果你是在 hinet 的網路之下，可使用 msa.hinet.net ，它不會擋你。smtp_from,
smtp_replyto 不重要，因為你不期待有人針對通知信回信。而 smtp_always_cc 則是每封通知信一定要寄的對象。

修改後，再重啟 apache 即可。

另外當你使用 ticket 時，要讓多人知道這個 ticket ，請使用 Cc: 欄位，其值為收信地址，若多值請用逗號隔開。


Old Comments in Blogger
--------------------------------------------------------------------------------



`正桓 <http://www.blogger.com/profile/07792178752458372525>`_ at 2007-12-10T17:16:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

請問一下，我新增一個ticket後，被assign的人沒有收到email，只有當負責的人接受了這個ticket或改變它的狀態後，才會收到mail，要如何讓
新增一個ticket時，trac也會發mail通知被assign的人?

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2007-12-10T21:20:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以在 trac.ini 使用下列設定：

always_notify_owner = true # 任何改變也會寄給「被指派的人」

always_notify_reporter = true # 任何改變也會寄給「創ticket的人」

always_notify_updater = true # 寄給改變這個 ticket 狀態的人

.. author:: default
.. categories:: chinese
.. tags:: trac
.. comments::
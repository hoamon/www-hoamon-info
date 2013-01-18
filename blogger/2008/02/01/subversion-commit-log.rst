subversion 的 commit log 寫錯了。
================================================================================

把伺服器中的 svn/hooks/pre-revprop-change.tmpl copy 一份成 svn/hooks/pre-revprop-
change ，並且要給它可執行的權限。

然後在自己 co 出來的專案資料夾中，打

# svn propset svn:log "xxxxxxx" -r 903 --revprop

即可把 903 版的 log 變成 xxxxxxx

.. author:: default
.. categories:: chinese
.. tags:: subversion
.. comments::
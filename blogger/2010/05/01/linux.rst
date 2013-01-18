使用公私錀登入 Linux 後，如何掛載被加密的目錄?
================================================================================

登入後，因為還沒有輸入過系統密碼，所以無法掛載加密目錄，這時候只會在家目錄看到




Access-Your-Private-Data.desktop README.txt




兩個檔案，其中 README.txt 的內容如下：




# cat README.txt

THIS DIRECTORY HAS BEEN UNMOUNTED TO PROTECT YOUR DATA.




From the graphical desktop, click on:

"Access Your Private Data"




or




From the command line, run:

ecryptfs-mount-private




也就是要你執行 ecryptfs-mount-private
，執行後，它會問你系統密碼，鍵入後，加密目錄就被掛載進來，只是你要重新再進入一次家目錄，才會看到還原的內容。




快速進入家目錄指令：




# cd

.. author:: default
.. categories:: chinese
.. tags:: ecryptfs, linux, ssh, ubuntu
.. comments::
使用 eCryptfs ，記得一定要備份下「加密錀匙」
================================================================================

使用 eCryptfs 加密目錄時，通常會隨機生成一把 32
字元的加密錀匙，來作目錄作加密，然後再使用使用者密碼來對「加密錀匙」作加密。所以如果因故弄丟了「加密錀匙」，但還記得「使用者密碼」，也是沒有用的。




所以記得，在使用此加密功能前，**一定一定一定**要先備份「加密錀匙」。




備份方式如下：




# cd /home/.ecryptfs/YOUR_ACCOUNT/.ecryptfs

or

# cd ~/.ecryptfs




# ls

auto-mount auto-umount Private.mnt Private.sig wrapped-passphrase




這個 wrapped-passphrase 就是「加密錀匙」被「使用者密碼」加密後的檔案。




# ecryptfs-unwrap-passphrase wrapped-passphrase

Passphrase: '''輸入使用者密碼'''

b19becdz81z8ba06aa4z35e6z1c0227f




這個 b19becdz81z8ba06aa4z35e6z1c0227f 就是「加密錀匙」，趕快把它記錄到其他檔案去。

.. author:: default
.. categories:: chinese
.. tags:: ecryptfs, linux, ubuntu
.. comments::
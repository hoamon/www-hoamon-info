SSH 的公私錀生成說明
================================================================================

Linux/Mac:

請在命令列鍵入如下指令：

$ ssh-keygen -t rsa -b 4096
::
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/tmp/.ssh/id_rsa): <<按
    Enter ，使用預設值>>
    Enter passphrase (empty for no passphrase): <<設個私錀密碼，請大於 5 個字元>>
    Enter same passphrase again: <<確認剛剛的私錀密碼>>

    Your identification has been saved in /home/tmp/.ssh/id_rsa.
    Your public key has been saved in /home/tmp/.ssh/id_rsa.pub.
    The key fingerprint is:
    72:fb:40:ba:8a:40:be:48:03:bd:20:13:6d:83:cb:d0 tmp@core2duo
    The key's randomart image is:
    +--[ RSA 4096]----+
    |                 |
    | +               |
    |+ A              |
    |o= .             |
    |*o. T . S        |
    |=o .   = .       |
    |.-.   . o        |
    |o.o.   . o       |
    |... ...   .      |
    +-----------------+


這樣，你的公錀就是 ~/.ssh/id_rsa.pub 而私錀就是 ~/.ssh/id_rsa 。

$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAgEAz22m/azvKC7uk05/D6qvl5c+QR95jkiqEpnn3/co/
zOGc4Gf7v1sc5H7Lf5CUOTxgfgAOZSmdr1OPaUYU1cvJTLTjKeVznifyTl3KabMH1Yy8wpSS1TjCT
bS8896uXXYtrdIL5KEHnVADYdS4fHWtY7uAR+JWlbh9OjN3deU77656knwW0PO5ELMYKUicSZZZFo
UFyDCflM61cNNP1i/rwa1pp8nFqyjzNOq5hKaEsssiJK4tPcm+5K8rwRXm3k7fprvoxYswebo9U85
kvyWPqY0iMFE0P019Pbq5VWCaqfv9nzD7rZaKe+aLk/7n+E4HSSSLYNlhnQkZUVm40zGnhGEZvT0e
+kmpJpXJKjAe3ZJkowc3o8xrBjD0ULP+jN1fHMUxllWOuxgNkqdD/UjXf5E777Zw+Fpoy2B1c/wRP
pRfsFisfLg9xxj3MF+E3wkHROOtrSv+M2wLKVtDODF4zwO8dr5g9s5xBTlSJFsBCJGmX2+zQ6y203
3amRnr/Xl0+KAqCOdO+BmQ+iw7X0DFCfxZtjx4RQXcGYw3HqSKP3I4Tft0IHD0g1HXuQhMezG6yVI
VABgbo47+Xbdxx7vFb82Anv7DnmhbOovk3LDrzPzyNe7fS2Jla5T5Etb5jyEHE1qNfJNzKVgxjBMG
KGk7L5GIx7pXUk= tmp@core2duo

把上面的公錀內容放到你想登入的 Linux/Mac 機器中的 ~/.ssh/authorized_keys2
(這個檔，其實是看系統管理員是怎麼設定的，只不過一般的 Linux 套件都是用這個作預設值)中，這樣你就能使用這一對公私錀登入遠端機器了。

Windows:

就比較麻煩了，請去下載 puttygen.exe 程式，執行它後如下圖：

`.. image:: http://2.bp.blogspot.com/-A3RPOKK9HxI/Tak2J1DneFI/AAAAAAAAC28/A0Z
nyMzw3bM/s400/putty-kengen.png
`_

選擇 SSH-2 RSA 及輸入 4096 的 Number of bits in a generated key 後，再按下 Generate
按鈕，讓滑鼠停留在綠色生成桿的下方空白處，並胡亂移動滑鼠遊標，讓 puttygen.exe 得到亂數種子，待進度達百分百後，可得到下圖：

`.. image:: http://2.bp.blogspot.com/-0hfTIG0dhUE/Tak2KAvGatI/AAAAAAAAC3E/ISc
lOw8JEzI/s400/putty-keygen-result.png
`_

選取的藍色文字即公錀內容，請貼到你欲登入的 Linux/Mac 機器中的 ~/.ssh/authorized_keys2
中，而私錀部份，請在設定密碼「Key passphrase」及確認密碼「Confirm passphrase」後，按下 Save private key
按鈕以存檔至系統硬碟。

最後，請保護好你的私錀檔(最好不要離開生成它的機器硬碟)，遺失它或是被別人盜取後的代價相當大。 Good Luck!

.. _就比較麻煩了，請去下載 puttygen.exe 程式，執行它後如下圖：: http://2.bp.blogspot.com/-A3RPO
    KK9HxI/Tak2J1DneFI/AAAAAAAAC28/A0ZnyMzw3bM/s1600/putty-kengen.png
.. _選擇 SSH-2 RSA 及輸入 4096 的 Number of bits in a generated key 後，再按下
    Generate 按鈕，讓滑鼠停留在綠色生成桿的下方空白處，並胡亂移動滑鼠遊標，讓 puttygen.exe
    得到亂數種子，待進度達百分百後，可得到下圖：: http://2.bp.blogspot.com/-0hfTIG0dhUE/Tak2KAvGatI
    /AAAAAAAAC3E/ISclOw8JEzI/s1600/putty-keygen-result.png


.. author:: default
.. categories:: chinese
.. tags:: linux, ssh, windows, mac
.. comments::
screenrc 再進化
================================================================================

改進來源：`設定 screen`_、`我也screenrc`_

我新的 screenrc 如下：
::shelltitle '$ | '
    hardstatus alwayslastline "%?%{yk}%-Lw%?%{wb}%n*%f
    %t%?(%u)%?%?%{yk}%+Lw%? %{-} %= %{= KR} %l %{-}%{= KG} @%H %y-%m-%d
    %{-}%0c:%s"
    bindkey "^[[1;5A" screen
    bindkey "^[[1;5B" other
    bindkey "^[[1;5C" next
    bindkey "^[[1;5D" prev
    startup_message off
    maxwin 10
    另外在 .bascrc 中，須加入：
::case "$TERM" in
    screen)
       PS1='\033k\033\\\\\u@\h: \W\\$ ';
       ;;
    *)
       PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
       ;;
    esac
    為了讓我清楚了解那個 Window 在幹什麼事，我另外在 .bashrc 中定義 alias sh_django="./manage
    shell" 及 alias core2duo="ssh -A 123.345.456.456" ，這樣在 window title
    上就會顯示它現在在執行的是那一個指令。整體效果如下：

`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/Sq40DOEVx4I/AAAAAAAACBU/Pq9
oojOxMa8/s400/Screenshot-2.png
`_
``_

.. _設定 screen: http://hoamon.blogspot.com/2009/03/screen.html
.. _我也screenrc:
    http://heaven.branda.to/%7Ethinker/GinGin_CGI.py/show_id_doc/254
.. _為了讓我清楚了解那個 Window 在幹什麼事，我另外在 .bashrc 中定義 alias sh_django="./manage
    shell" 及 alias core2duo="ssh -A 123.345.456.456" ，這樣在 window title
    上就會顯示它現在在執行的是那一個指令。整體效果如下：: http://2.bp.blogspot.com/_eKM9lHjTZjs/Sq40DOE
    Vx4I/AAAAAAAACBU/Pq9oojOxMa8/s1600-h/Screenshot-2.png


.. author:: default
.. categories:: chinese
.. tags:: screen, linux
.. comments::
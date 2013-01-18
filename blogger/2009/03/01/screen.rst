設定 screen
================================================================================

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/Sb2iwWrTcFI/AAAAAAAAB0A/21q
ncW69IaM/s400/screen.png
`_
UN*X 的使用者多半會是 screen 的愛好者，而我也不例外。

一個設定良好的 screen 是非常令人賞心悅目的。不過，我之前一直想要在不同的 window 上秀出它當下的資料夾位置，卻找不到如何設定 screen
的方法。

今天讓我發現原來可以在 .bashrc 中設定。只不過，在設定後，一直有一個小小的困惱，它會在 shell 提示符號前多輸出 134134 的字串。

以下是我的 .screenrc
::startup_message off
    hardstatus alwayslastline \
    " %-Lw%{= BW}%n%f %{-}%+Lw %=| @%H %{-} %= %{= KR} %l %{-}%{= KG}
    %y-%m-%d %{-}%0c:%s"
    maxwin 10


.bashrc
::case $TERM in
    xterm*|rxvt*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}:
    ${PWD/$HOME/~}\007"'
    ;;
    screen*)
    #若刪除 \134 ，則 screen window 就不會出現資料夾位置
    #但保留 \134 ，則 shell 提示符號會多出現 134134 的字串
    PROMPT_COMMAND='echo -ne "\033k\033\134\033k${PWD##/*/}\033\134"'
    ;;
    *)
    ;;
    esac


.. _: http://4.bp.blogspot.com/_eKM9lHjTZjs/Sb2iwWrTcFI/AAAAAAAAB0A/21qnc
    W69IaM/s1600-h/screen.png


.. author:: default
.. categories:: chinese
.. tags:: un*x, linux, shell script
.. comments::
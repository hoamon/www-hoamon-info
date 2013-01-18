自動更新 hg 儲存庫的 shell script
================================================================================

因為 hg 不同與 svn 可以資料夾結構來看待專案，在 hg 中，一個專案就是一個資料夾，其下不會有子專案，所以像我手頭有二十幾個 hg
專案時，如果要同時更新( pull -u )這些專案，我必須一個專案一個專案進去打 hg pull -u ，這實在太花時間了。但還好我用的是 Linux
，所以就把這些煩人且重複的指令寫成一個 shell script ，執行一次就更新全部。以下是我的程式碼：
::#!/bin/bash
    today=`date +%Y%m%d`
    me=`whoami`
    echo ${today}
    original_dir=${PWD}
    touch '/tmp/.'${today}

    if [ "$1" != "" ];then
        dest=`find $1 -regex ".*\/\.hg$"`
    else
        dest=`locate -r "\/home\/${me}\/.*\/\.hg$"`
    fi

    for dir in $dest;do
        if [ ! ${dir/*mercurial_appengine*/} ];then
            continue
        fi
        cd ${dir}/..
        echo -ne "\t*** ${PWD} ***\n"
        hg pull -u || exit
        cd $original_dir
    done

.. author:: default
.. categories:: chinese
.. tags:: mercurial, linux, shell script
.. comments::
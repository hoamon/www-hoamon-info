#!/bin/bash
root=`pwd`

for d in `find -name "conf.py"`;do
    cd `dirname $d`
    if [ -d "modern5" ];then
        tinker --build
    else
        make html
    fi
    cd $root
done

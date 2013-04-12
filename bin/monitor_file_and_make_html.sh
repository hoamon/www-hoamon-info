#!/bin/bash

cd $1

OLD=`stat -t ./*|grep -v "_build"|sort`
# OLD=`stat -t testdir | sed 's/[0-9][0-9]*$//'`
# if SE linux stat
while true; do
    NEW=`stat -t ./*|grep -v "_build"|sort`
    # NEW=`stat -t testdir | sed 's/[0-9][0-9]*$//'` if SE linux stat
    [ "$NEW" == "$OLD" ] || make html || tinker -b
    OLD=$NEW
    sleep 3
done

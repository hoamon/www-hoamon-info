#!/bin/bash
#from 855:1cd29be2e74f to 900:5cb480f47e4b for XXX module

cd `dirname $0`
cd ../trunk
./manage.py syncdb
./manage.py migrate XXX 0001 --fake
./manage.py migrate XXX
./manage.py syncdb --all
./manage.py loaddata XXX_data.json
./manage.py loaddata XXX_test_data.json
./manage.py set_XXX

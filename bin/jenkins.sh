#!/bin/bash
now=`date "+%Y%m%d%H%M%S"`
cd $WORKSPACE && \
bin/prepare_programming.py && \
echo 'DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": "test_ho600",
        "PASSWORD": "test_ho600",
        "HOST": "localhost",
        "NAME": "test_ho600",
        "OPTIONS": {
            "autocommit": True,
            }
        }
    }
import os
TRUNK = os.path.dirname(os.path.abspath(__file__))
DEVELOPER_DOCS_PATH = os.path.join(TRUNK, "__docs__")' > /tmp/eiorqewldf_${now}_jlasdjflkoifjewfq_trunk_local_settings.py && \
cd docs/ && make html && rm -rf ../trunk/__docs__/ && cp -rf _build/html/ ../trunk/__docs__/ && \
cd ../trunk && \
sudo /bin/mv /tmp/eiorqewldf_${now}_jlasdjflkoifjewfq_trunk_local_settings.py trunk_local_settings.py && \
./manage.py test && ./manage.py syncdb && cd .. && bin/before_deployment.py && find trunk -name "*.pyc" -exec rm -rf {} \; && \
version=`hg id -i` && \
if [ -x /mnt/vol-38cbf01a/nginx/ho600-${version} ]; then sudo /bin/mv /mnt/vol-38cbf01a/nginx/ho600-${version} /mnt/vol-38cbf01a/nginx/trash/${now}-ho600-${version} ; fi && \
cp -rf trunk "/mnt/vol-38cbf01a/nginx/ho600-${version}" && \
sudo /bin/chown -R www-data:jenkins "/mnt/vol-38cbf01a/nginx/ho600-${version}" && \
sudo /bin/mv /mnt/vol-38cbf01a/nginx/test_ho600 /mnt/vol-38cbf01a/nginx/trash/${now}-test_ho600 && \
sudo /bin/mv /mnt/vol-38cbf01a/nginx/ho600-${version} /mnt/vol-38cbf01a/nginx/test_ho600 && \
sudo /bin/chown -R www-data:jenkins /mnt/vol-38cbf01a/nginx/test_ho600.log && \
touch /mnt/vol-38cbf01a/nginx/test_ho600.reload
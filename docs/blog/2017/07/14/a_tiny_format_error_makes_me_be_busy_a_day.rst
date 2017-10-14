一個小小的格式錯誤
==============================================================================

一個小小的格式錯誤，我查了一整天。前句當然是誇飾法，畢竟我一整天還是得吃飯、上廁所、站起來走來走去，最重要的是不能忘了呼吸。

.. code-block:: bash

	(ap.example.com-env) ubuntu@ip-172-16-32-60:/var/www-aps/ap.example.com-36-81a1/trunk$ ./manage.py runserver 0.0.0.0:8000 --nothread
	Traceback (most recent call last):
	  File "./manage.py", line 11, in <module>
	    execute_from_command_line(sys.argv)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 353, in execute_from_command_line
	    utility.execute()
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 345, in execute
	    self.fetch_command(subcommand).run_from_argv(self.argv)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 195, in fetch_command
	    klass = load_command_class(app_name, subcommand)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 39, in load_command_class
	    module = import_module('%s.management.commands.%s' % (app_name, name))
	  File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
	    __import__(name)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/core/management/commands/runserver.py", line 16, in <module>
	    from django.db.migrations.executor import MigrationExecutor
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/migrations/executor.py", line 7, in <module>
	    from .loader import MigrationLoader
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/migrations/loader.py", line 10, in <module>
	    from django.db.migrations.recorder import MigrationRecorder
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/migrations/recorder.py", line 12, in <module>
	    class MigrationRecorder(object):
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/migrations/recorder.py", line 26, in MigrationRecorder
	    class Migration(models.Model):
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/migrations/recorder.py", line 27, in Migration
	    app = models.CharField(max_length=255)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/models/fields/__init__.py", line 1072, in __init__
	    super(CharField, self).__init__(*args, **kwargs)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/db/models/fields/__init__.py", line 166, in __init__
	    self.db_tablespace = db_tablespace or settings.DEFAULT_INDEX_TABLESPACE
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/conf/__init__.py", line 55, in __getattr__
	    self._setup(name)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/conf/__init__.py", line 43, in _setup
	    self._wrapped = Settings(settings_module)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/conf/__init__.py", line 116, in __init__
	    setattr(self, setting, setting_value)
	  File "/var/www/ap.example.com-env/local/lib/python2.7/site-packages/django/conf/__init__.py", line 85, in __setattr__
	    raise ImproperlyConfigured("If set, %s must end with a slash" % name)
	django.core.exceptions.ImproperlyConfigured: If set, STATIC_URL must end with a slash

.. more::

上面的錯誤訊息是 Jenkins Server 在執行網站發佈指令檔所產生的，指令檔是用 bash 語法所寫的。

我之所以漏看這個錯誤，原因是在於 script 內的指令多用 && \\ 連接而成，如下 :

.. code-block:: bash

	command_1 && \
	command_2 && \
	command_3 && \
	command_4 && \
	command_5 && \
	command_6 && \
	command_7 && \
	command_8 && \
	command_9
	command_10 && \
	... && \
	command_27 && \
	command_28 && \
	command_29 && \
	command_30

整個跑完跑到 command_30 後，它的 stdout 有一大堆，到最後面則是直接秀 Deploy Successfully ，\
所以我一直以為發佈過程順利，發佈後的網站之所以看不到新的 css/js 是出在我的程式碼寫錯了。\
於是，我一直 debug 、 debug 、 debug 、 ... 。

但其實它在 command_6 的時候，就出現錯誤了，而又因為 command_9 後面沒接著 && \\ ，
在 command_6 得到 stderr 後，它一路就跳到 command_10 繼續執行下去， \
command_10 ~ command_30 恰巧也沒出錯，就這樣它最後是顯示「發佈成功」。

執行 command_6 所得到的 "If set, STATIC_URL must end with a slash" ，\
其實是我在 command_4 所搞砸的， settings.STATIC_URL 原本是 '/static/' ，\
但在發佈到商用網站時，要把 static files 全丟到 AWS S3 去，\
STATIC_URL 這時要改成 "https://s3-ap-northeast-1.amazonaws.com/MY_BUCKET/<build_number>-<git_commit_hash>/" 。\
但就是這裡，我誤修改成了 "https://s3-ap-northeast-1.amazonaws.com/MY_BUCKET/<build_number>-<git_commit_hash>" ，後綴沒有用 / 結尾。

我在本機查半天，它都是用 STATIC_URL = '/static/' 來打包 static files 的，也都不會出錯。\
於是，只能東查一個、西查一個，始終沒打到要害。

花了一堆時間後，終於某次不小心讓我瞄到這個 Error Log ，我才恍然大悟: 一個 command_4 的錯誤取代，\
再加上 command_9 後面沒加上 && \\ ，這兩個小錯，合起來讓我難以 debug 。

說出這麼愚蠢的 debug 故事，只是想跟各位分享一個 Python 禪法:

.. code-block:: plain

	Errors should never pass silently.

	切勿讓錯誤悄稍溜走。

而 `TDD <http://chimera.labs.oreilly.com/books/1234000000754/index.html`_ 可以幫到這一點。

.. author:: default
.. categories:: chinese
.. tags:: django, TDD
.. comments::

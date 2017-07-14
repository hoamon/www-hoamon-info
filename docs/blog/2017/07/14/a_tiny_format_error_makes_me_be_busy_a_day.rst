a tiny format error makes me be busy a day
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

.. author:: default
.. categories:: chinese
.. tags:: django
.. comments::

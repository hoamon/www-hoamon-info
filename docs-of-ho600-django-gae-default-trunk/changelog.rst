.. Copyright (c) 2012, ho600.com
   All rights reserved.
   
   Redistribution and use in source and binary forms, with or without modification,
   are permitted provided that the following conditions are met:
   
       Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.
   
       Redistributions in binary form must
       reproduce the above copyright notice, this list of conditions and the
       following disclaimer in the documentation and/or other materials provided
       with the distribution.
   
       Neither the name of the ho600.com nor the names of its contributors
       may be used to endorse or promote products derived from this software
       without specific prior written permission.
   
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
   IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
   INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
   OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
   EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

.. ho600-default-trunk for django or gae documentation master file, created by
   sphinx-quickstart on Tue Dec  7 16:10:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================================================================
Changelog
================================================================================

release-1.0.4
--------------------------------------------------------------------------------

 * add "downloads" and "copies" in depends_modules.conf
 * import django-guardian and django-debug-toolbar library
 * modify "ho600_lib.get_template_by_site_and_lang" to change template finding flow
 * add "ho600_lib.static" and  "ho600_lib.media" function in ho600_lib/__init__.py for url discovering in templates
 * add "ho600_lib.get_site_from_settings" to get the SITE is user browsing
 * add "bin/monitor_file_and_make_html.sh" to automatically generating sphinx-document
 * add "bin/symbol_to_unicode.py" to convert code(ex, "\u65b0") to "新", for example
 * add taiwan post code data(臺灣地區郵遞區號前3碼一覽表_9912.xls, 2011/8/15 version) in taiwan_postcode.json
 * add a PostCode Model

release-1.0.3
--------------------------------------------------------------------------------

 * include mimeparse-0.1.3 lib in asset/ directly
 * include python-dateutil-1.5 lib in asset/ directly
 * add context processor: ho600_lib.context_processors.settings
 * add template tags: ho600_lib.templatetags.ho600_lib_tags.use_jqueryui
 * add settings.ANOTHER_DEPENDS_MODULES to copy modules that were needed but not in settings.INSTALLED_APPS
 * use settings.SDK_MODE to find out the execute environment right now
 * recursively load settings.py and local_settings.py in modules
 * insert path to sys.path once

release-1.0.2
--------------------------------------------------------------------------------

 * also delete the top directory of depends moduels

release-1.0.1
--------------------------------------------------------------------------------

 * bin/before_programming is renamed to bin/prepare_programming.
 * can copy multi-hierarchy modules.

release-1.0.0
--------------------------------------------------------------------------------

 * bin/before_programming.py and bin/before_deployment.py are both working.
 * Directory layout is stable.


The problem of moinmoin for adding MathML support
================================================================================

Environment
MoinMoin version: 1.5.8
ASCIIMathML.js version: 2.0.1

I can use $ Z_if $ to show math expression. But when i run to edit page in
text mode,the expression was replaced to

<p align="center">\displaystyle$ Z_if }$</p>

by ASCIIMathML.js

Because i don't know the structure of moinmoin, so i hard code the raw
source. Around the 1271 line of MoinMoin/wikiutil.py.

Replace the line

user_head = [request.cfg.html_head]

With

----if request.query_string.count('action=edit'):
--------user_head = ['']
----elif request.form and ( request.form.has_key('button_spellcheck') or
----request.form.has_key('button_switch') or
request.form.has_key('button_preview') ):
--------user_head = ['']
----else:
--------user_head = [request.cfg.html_head]

Maybe someone else has better solution.


.. author:: default
.. categories:: chinese
.. tags:: moinmoin, python
.. comments::
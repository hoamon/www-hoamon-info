from subversion to mercurial
================================================================================

It's enough for me to test/learn/use mercurial, i decide to convert my old
subversion repositories now.

To convert subversion repository, you need the '''python-svn''', '''python-
subversion''' plugins in the Ubuntu.

Then you should check the working subversion repository has no need to type
username/password at the status of '''svn update''', or you will get the
'''XXX does not look like a Subversion repo''' message from '''hg convert'''.

When you are ready, just type '''hg convert -s svn your_svn_repo_dir''', and
you can get a dir named '''your_svn_repo_dir-hg'''.

Congratulation! It's a peice of cake.

.. author:: default
.. categories:: chinese
.. tags:: mercurial, subversion
.. comments::
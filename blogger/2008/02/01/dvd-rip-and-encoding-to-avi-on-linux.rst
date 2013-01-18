DVD rip and encoding to .avi on Linux
================================================================================

just take it, don't ask me. i have no patience to understand vedio encoding
principle yet.


1.  First the sound:
``# mencoder -dvd-device /tmp/dvd dvd://1 -ovc frameno -o frameno.avi -oac
mp3lame -lameopts abr:br=128``
2.  First pass:
``# mencoder ````-dvd-device /tmp/dvd dvd://1 ````-nosound -oac copy -o
/dev/null -ovc lavc -lavcopts
vcodec=mpeg4:vbitrate=800:vhq:vpass=1:vqmin=1:vqmax=31 -vop scale -zoom -xy
640
``
3.  Second pass:
``# mencoder ````-dvd-device /tmp/dvd dvd://1 ````-oac copy -o file.avi -ovc
lavc -lavcopts vcodec=mpeg4:vbitrate=800:vhq:vpass=2:vqmin=1:vqmax=31 -vop
scale -zoom -xy 640``

after steps above here and you get the '''file.avi'''

But, this method don't get the subtitle.

.. author:: default
.. categories:: chinese
.. tags:: mencoder, linux, vedio, mplayer
.. comments::
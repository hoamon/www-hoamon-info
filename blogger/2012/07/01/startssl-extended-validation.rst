StartSSL Extended Validation Certificate has sec_error_unknown_issuer error with Firefox
================================================================================




A few days ago, i bought a Extended Validation Certificate from
`www.startssl.com`_ for my client( in strictly speaking, cooperate with
someone's help ).



`.. image:: http://2.bp.blogspot.com/-3Sn5sCOvtOY/T_151iKmQBI/AAAAAAAAEiI/5pi
GnulgXUw/s1600/bookcat.png
`_


The price of two years EV certificate is more cheaper than other
competitors's in Taiwan.  `StartSSL EV quotes USD$199`_( closing to TWD 6,000
), and the same level competitors in Taiwan quote TWD 55,000 ~ 90,000.  Yes,
you did not lost, the ten times expensiveness.

But it costs something else, because the `www.startssl.com`_ is a `Israel
company`_, we must verify the personal and  company authorization with law
notarization first.  This law jobs spend our half month.  Anyway, we done,
and obtain a real green bar certificate now.

After i install and configure certificate in Nginx Server, Chrome and IE can
pop up rightly, but Firefox alerts a "sec_error_unknown_issuer" message to
me.

The solution is catching "sub.class4.server.ca.pem"( Exclusive only for
Extended Validation Cert ) and "ca.pem" into your_example_domain.crt file,
and the order must be "your_domain_crt", "sub.class4.server.ca.pem" and
"ca.pem".  You can find the two files in the `www.startssl.com/certs/`_.

Below is my Nginx conf:

listen                  443;
ssl                     on;
ssl_certificate         /etc/ssl/your_example_domain.crt;
ssl_certificate_key     /etc/ssl/your_example_domain.key;





This solution wasted me about one hour, because i did not known the
sub.classX.server.ca.pem is different to free-class and Extended Validation
Cert.  Free-class cert uses class1 and EV cert uses class4.

Finally, i got a green internet address bar.  So happy~

.. _www.startssl.com: http://www.startssl.com/
.. _for my client( in strictly speaking, cooperate with someone's help
    ).: http://2.bp.blogspot.com/-3Sn5sCOvtOY/T_151iKmQBI/AAAAAAAAEiI/5piGnul
    gXUw/s1600/bookcat.png
.. _StartSSL EV quotes USD$199: http://www.startssl.com/?app=39
.. _Israel company: http://www.startssl.com/?app=27
.. _www.startssl.com/certs/: http://www.startssl.com/certs/


.. author:: default
.. categories:: chinese
.. tags:: extended validation certificate, startssl firefox, sec_error_unknown_issuer
.. comments::
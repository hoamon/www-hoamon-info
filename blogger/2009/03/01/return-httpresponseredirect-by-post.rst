return HttpResponseRedirect with Post Data?
================================================================================

This is an example to solve the question from `Django User Group`_

In the specification of http status code 302, there are no way to pass a post
data to user's browser. But we can use AJAX method to reach this requirement.
The principle is using the AJAX request to do some thing must run in the
server and return a json data to browser, then the callback function that
defined in the html will shape a html form and submit this form.

::def readReturnHttpRedirectWithPost(R):
        if R.GET.get('var', None):
            # do something what you want
            return HttpResponse(json.write({'action':
            'https://your.web.sitek/', 'vars': {'var1': 'var1', 'var2':
            'var2'}}))
        html = """
        <html><head><script type="text/javascript"
        src="/media/jquery.ui-1.5.1/jquery-1.2.6.js"></script></head>
            <body>
              <ul><li><input type="text" id="var"></li>
                  <li><input type="submit"
                  id="updateFormWithPost"></li></ul>
              <form id="post_form" method="POST"></form>
              <script>
                $(document).ready(function(){
$('#updateFormWithPost').click(function(){
                        var value = $('#var').val();
$.getJSON('/u/readreturnhttpredirectwithpost/',
                        {'var': value}, function(json){
                            var $post_form =
                            $('#post_form');
$post_form.attr('action', json['action']);
                            for (var i in
                            json['vars']){
                                var $input =
                                $('<input type="hidden" name="'+i+'"
                                value="'+json['vars'][i]+'">');
$post_form.append($input);
                            }
                            $post_form.submit();
                        });
                    });
                });
              </script>
            </body>
        </html>"""
        return HttpResponse(html)


.. _Django User Group: http://groups.google.com/group/django-
    users/browse_thread/thread/1c4fae7a3dd1982e/4938233a7341c0a0


.. author:: default
.. categories:: chinese
.. tags:: http, django, jquery, ajax, python
.. comments::
Connect MS SQL Server with python-pymssql
================================================================================

Two years ago, i writed a blog: "`How to connect MS SQL Server with Python in
the Linux OS?`_". I used freetds + python-sybase in this Howto. Now i have to
upgrade the linux server to x86_64 architecture(original in i386), then the
old python-sybase package have always been failured. The newest version
released at 2010 DEC, but i tried all the 39, 38, 36 versions that no one can
compile accurately.

Fortunately, my underclassman talked to me about python-pymssql. And it has
been packaged in the Ubuntu, so i just use the magic command:

$ sudo apt-get install python-pymssql

My Linux server takes the power back!!!

The usage likes python-sybase, below is the example:

::
     1 #!/usr/bin/env python
     2 import sys, datetime, pymssql
     3 from types import IntType
     4
     5 DB = {
     6     'ip': '127.0.0.1',
     7     'port': '1433',
     8     'user': 'user',
     9     'password': 'password',
    10     'database': 'database',
    11 }
    12
    13 try:
    14     Database = pymssql.connect(host=':'.join([DB['ip'],
    DB['port']]), user=DB['user'], password=DB['password'],
    database=DB['database'], as_dict=True)
    15 except pymssql.OperationalError, msg:
    16     print "Could not Connection SQL Server"
    17     sys.exit()
    18 else:
    19     DBCursor = Database.cursor()
    20
    21 sql = "select * from data_table"
    22 print('sql: %s' % sql)
    23 DBCursor.execute(sql)
    24
    25 while 1:
    26     row = DBCursor.fetchone()
    27     if not row: break
    28
    29     for k, v in row.items():
    30         if type(k) == IntType: continue
    31
    32         if k.lower() in ('some_date_field', ):
    33             # change field type
    34             if type(v) == datetime.date:
    35                 value = v
    36             else:
    37                 try:
    38                     value = datetime.date(*time.strptime(v,
    '%Y/%m/%d')[:3])
    39                 except:
    40                     value = None
    41         else:
    42             value = unicode(str(v), 'cp950')
    43
    44         print('%s => %s'%(k, v))


.. _How to connect MS SQL Server with Python in the Linux OS?:
    http://hoamon.blogspot.com/2008/03/how-to-connect-ms-sql-server-with.html


.. author:: default
.. categories:: chinese
.. tags:: freetds, linux, python, mssql
.. comments::
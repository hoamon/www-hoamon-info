How to connect MS SQL Server with Python in the Linux OS?
================================================================================

Basically, the general method is using ODBC Interface. In the Unix
environment, we can use unixODBC library, but i had tried in failure.

So... another method is using hard core TDS protocol of Sybase Server.
because MicroSoft buy the MSSQL server source code from Sybase, so they use
the same protocol. maybe there are some difference between the servers. but i
could not found it as far.

and i wanted using Python to program, so the requirement is below here:


-   freetds(http://www.freetds.org/): TDS protocol library written in C
-   python-sybase(http://www.freetds.org/userguide/python.htm): python
    interface for controll freetds library
-   python-devel (using in compile python-sybase)

Installation in Ubuntu is so easy, try apt-get install python-devel first.
and then install freetds and python-sybase. command is below here:

# tar -zxf freetds.tgz

# cd freetds

# ./configure --prefix=/usr/local/freetds

# make

# sudo make install

# tar -zxf python-sybase.0.37.tgz #PS i try 0.37, because 0.38 is having
something wrong in my server

# cd python-sybase.0.37

# sudo SYBASE=/usr/local/freetds \
CFLAGS="-DHAVE_FREETDS" \
LD_LIBRARY_PATH=/usr/local/freetds/lib:${LD_LIBRARY_PATH} \
python setup.py install

OK! installation is done!

try the freetds library is OK!

# /usr/local/freetds/bin/tsql -H {ServerIP} -p 1433 -U {Username} -P
{Password}

> EXEC sp_databases

> go

this 『EXEC sp_databases』 command will show the all databases that this
{Username} can read.

> use testdb

> EXEC sp_tables

> go

this 『EXEC sp_tables』 command will show the all tables of testdb.

> EXEC sp_columns @table_name = 'users'

> go

this 『EXEC sp_columns @table_name = 'users'』 command will show the all fields
of table 'users'.

if everything seen OK! you can try Sybase module in the python interpreter.

# SYBASE=/usr/local/freetds CFLAGS="-DHAVE_FREETDS"
LD_LIBRARY_PATH=/usr/local/freetds/lib /usr/bin/python::** 1 ****import**
Sybase

    ** 2 ****class** **DictCursor**(Sybase.Cursor):

    ** 3 **    **def** **row2dict**(self, row):

    ** 4 **        d = {}

    ** 5 **        **for** i,elt **in** enumerate(row):

    ** 6 **            d[self.description[i][**0**]] = elt

    ** 7 **        **return** d

    ** 8 **    **def** **fetchall**(self):

    ** 9 **        rows = Sybase.Cursor.fetchall(self)

    **10 **        result = []

    **11 **        **for** row **in** rows:

    **12 **            result.append(self.row2dict(row))

    **13 **        **return** result

    **14 **    **def** **fetchone**(self):

    **15 **        **return** row2dict(Sybase.Cursor.fetchone(self))

    **16 **    **def** **fetchmany**(self):

    **17 **        rows = Sybase.Cursor.fetchmany(self)

    **18 **        result = []

    **19 **        **for** row **in** rows:

    **20 **            result.append(self.row2dict(row))

    **21 **        **return** result

    **22 ****class** **Connection**(Sybase.Connection):

    **23 **    **def** **dictcursor**(self):

    **24 **        **return** DictCursor(self)

    **25 **db = Connection(ip:port, account, password, dbname)

    **26 **c = db.dictcursor()

    **27 **sql = **"select * from sometable"**

    **28 **c.execute(sql)

    **29 **rows = c.fetchall()

    **30 ****for** row **in** rows:

    **31 **    **for** k, v **in** row.items():

    **32 **        **print** k, v

    **33 ****print** **'done'**
    OK! this is real done!

.. author:: default
.. categories:: chinese
.. tags:: freetds, sybase, python, microsoft
.. comments::
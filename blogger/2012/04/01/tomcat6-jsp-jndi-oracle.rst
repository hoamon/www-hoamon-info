Tomcat6 + JSP + JNDI + Oracle 設定
================================================================================

朋友公司最近想要接個案子：『在 `AWS`_ 上面架一個 JSP 網站，而且指定資料庫須用 Oracle DB 』。

用 Oracle DB 不是難事，拿信用卡註冊進去就有了，跑一個小時最低收你 0.17 美金(約臺幣 6 元)，很多人都付得起。麻煩的是朋友及我都不是熟
JAVA 及 Oracle 的人。因為我們愛用 Open Source (奇怪 JAVA 明明就是 Open Source 呀!
怎麼我直覺不是呢???)。

為此，我找了高中同學 K ，他可是名門正派(資工背景)出身，從 C ， Delphi ， VisualBasic ， JAVA ， .Net
一路走來的程式設計師。而且他幫客戶開發時，多半是採用 Oracle 或是 SQL Server 的資料庫。於是一拍即合。

那我要幹麼呢? 也不是作個牽溝仔怎麼簡單的工作就結束了。 K 只熟 Windows ，而那個 AWS EC2 是要跑 Linux 的。所以我的工作就是搞定
Linux 上的 Http 伺服器( Apache or Nginx )、 AP 伺服器( Tomcat6 ) 及 JNDI Container
(其實，我一直想不懂這 JAVA 或物件導向的術語)。

在 AWS 上租用 Oracle DB 是即用即付的，所以我想要在本機先測試 Tomcat6, JNDI 設定成功後再送上去。

我的作法是在本機的 VirtualBox Windows 上裝一個 Oracle 11g express (因 Oracle 沒出 Ubuntu
版)，再作一個 `1521 port 的 forward`_ ，下載 `sqlplus, basic`_ 套件，測試連線正常：

$ sqlplus test/test@//localhost/XE

第一個 test 表帳號，第二個表密碼，最後面的 XE 表資料庫實例的名稱，預設是 XE 。能看到 SQL> 提示就表示可連線 Oracle 11g 了。

安裝 Tomcat6 非常簡單，在 Ubuntu 中打上 apt-get install tomcat6 就夠了。接下來去抓 Oracle 的 jdbc
driver: `ojdbc6.jar`_ ，置入 /usr/share/java 目錄。然後修改 tomcat6 設定檔：

# /etc/tomcat6/catalina.properties
common.loader=${catalina.base}/lib,${catalina.base}/lib/*.jar,${catalina.home
}/lib,${catalina.home}/lib/*.jar,/var/lib/tomcat6/common/classes,/var/lib/tom
cat6/common/*.jar,**/usr/share/java/*.jar**
**
**# /etc/tomcat6/content.xml

::<Context>
        <WatchedResource>WEB-INF/web.xml</WatchedResource>
        <Resource name="jdbc/OracleDB" auth="Container"
        type="javax.sql.DataSource"
        driverClassName="oracle.jdbc.OracleDriver"
        url="jdbc:oracle:thin:@localhost:1521:XE"
        username="test" password="test" maxActive="20" maxIdle="10"
    maxWait="-1"/>
    </Context>

# /var/lib/tomcat6/webapps/MyApps/WEB-INF/web.xml

::<?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web
    Application 2.3//EN" "http://java.sun.com/dtd/web-app_2_3.dtd">
    <web-app>
        <display-name>My Web Application</display-name>
        <description>
            A application for test.
        </description>
        <resource-ref>
            <description>Oracle Datasource example</description>
            <res-ref-name>jdbc/OracleDB</res-ref-name>
            <res-type>javax.sql.DataSource</res-type>
            <res-auth>Container</res-auth>
        </resource-ref>
    </web-app>

然後在 /var/lib/tomcat6/webapps/MyApps/ 放入一個 test_oracle.jsp 程式：

::
    <%@ page import="java.sql.*" %>
    <%@ page import="javax.sql.*" %>
    <%@ page import="javax.naming.*" %>
    <%@ page language="java" contentType="text/html;charset=UTF8" %>
    <%
    Connection con = null;
    Context initContext = new InitialContext();
    Context envContext  = (Context)initContext.lookup("java:/comp/env");
    DataSource ds = (DataSource)envContext.lookup("jdbc/OracleDB");
    try {
        con = ds.getConnection();
        if(!con.isClosed()){
            out.println("與 Oracle db 有連線!!\n<br/>");
        }
        con.close();
    } catch (SQLException sqle) {
        out.println("sqle = "+sqle);
    } finally {
        con = null;
    }
    %>



最後到瀏覽器去觀看 http://localhost:8080/MyApps/test_oracle.jsp 網頁，有看到『與 Oracle db
有連線!! 』那就成功了。



`.. image:: http://paper.hoamon.info/stock.jpg
`_




.. _AWS: http://blog.hoamon.info/2012/04/aws.html
.. _1521 port 的 forward: http://blog.hoamon.info/2007/11/virtualbox-
    guest-os-host-os-linux.html
.. _sqlplus, basic:
    http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
.. _ojdbc6.jar: http://www.oracle.com/technetwork/database/enterprise-
    edition/jdbc-112010-090769.html
.. _』那就成功了。: http://paper.hoamon.info/stock.jpg


.. author:: default
.. categories:: chinese
.. tags:: java, linux, tomcat6, oracle
.. comments::
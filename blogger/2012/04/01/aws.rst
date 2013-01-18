AWS 初試
================================================================================

因綠際會讓我有機會去研究 `Amazon Web Service`_ 。那是個與 `GAE`_ 功能相同，但操作模式不盡相同的雲端服務。

GAE 像是個套裝雲端平台，有些東西它已幫你決定好，要就用，不用就拉倒，當然可以寫 ticket
去建議他們，但不一定會立案。犧性自由的收獲就是得到『自動擴展性』，當你的網站流量大時， GAE 自動開分身，也因為你寫的程式一開始就受 GAE
平台的限制，而這些限制的目的主要就是為了提升擴展性，所以一開始在 GAE 上寫網站很痛苦，但後期維護很輕鬆。

AWS 就像是個高級積木組，你想怎麼兜就怎麼組，在自己架站環境中跑的網站，不用改任何一行程式碼就能移至 AWS
上。但等到你的網站流量大，使用者多時，就得再利用 AWS 提供的系統維護工具來自行維護了。缺點當然是你得多請一組系統管理員，但相較於自己搞機房、架站，利用
AWS 平台可以讓系統管理員工作簡單多了。

對我而言，兩種開發平台各有好處，這我當然兩者都學，唯其資源分配乃先 GAE ，後 AWS 。

AWS 的主力產品就是 Elastic Compute Cloud (EC2) ，一個 EC2 可以想像它就是你的一台電腦，只是放在 Amazon
機房裡。

我們可以開一台 EC2 出來後，在裡面安裝 ubuntu, nginx, django, postgresql 等軟體，讓它跑網頁伺服器。或是裝了
postfix 就能變郵件伺服器，或是裝了 vlc 變影音串流伺服器。簡單講，只要有安裝相對應的軟體， EC2 也能變火箭。

但是 EC2 的硬碟不多，近 10 G 而已，如果你想放很多資料，那就需要 Simple Storage Service(S3)
。而且為了擴展性，你也得用 S3 ，用了 S3 ，當網站熱門到得多開幾台 EC2 出來時，它們才有共同儲存的地方。

當網站只用一台 EC2 時，可以把 MySQL/PostgreSQL/Oracle 資料庫裝在同一個 EC2 裡，但當有多個 EC2 時，怎麼辦?
AWS 有給獨立的資料庫伺服器，除了關聯式資料庫( RDS )外，也有 NoSQL ( DynamoDB )的。把資料庫託給 RDS/DynamoDB
管理，也省得自己作備援、備份、調校等管理工作，而且以 Oracle DB 來看，可以不用購買授權改以每小時租用計費，這相當方便。易言之，在 AWS
上花錢就能換得輕鬆。

整個 AWS 架構是在一個虛擬化的機房內，每開啟一個 EC2 實體，它會得到一個虛擬 IP ，我們可以透過 `boto`_(Python base)
去管理它，也可以直接在 `AWS Management Console`_ 頁面管理。

目前 AWS 在美國維吉尼亞、奧勒岡、北加州、愛爾蘭、日本、新加坡、巴西聖保羅都有機房。你想把機器開在那裡，自己決定就行了。

如果要讓 EC2 有公共 IP ，可以到 `Elastic IPs`_ 去索取一個實體 IP ，但記得在索取後就要把它綁定到 EC2 實體去，如果要了公共
IP ，但沒有拿去用，是會被 AWS 索取 0.01/hours 的罰款，我就被罰了 0.71 元美金，因為我關了 EC2 實體後，並沒有再去退 IP
，結果那個 IP 就被我佔了 71 個小時。

其他 AWS 產品還有 CloudWatch, CloudFront, CloudCache, SQS, SES, SNS,
SWF...，實在很多，請自行到`官網`_了解。

目前 AWS 有`免費試用方案`_，方案為註冊後一年之內使用，而每個月的免費額度如下：

AWS Free Usage Tier (Per Month):


-   750 hours of `Amazon EC2`_ Linux Micro Instance usage (613 MB of
    memory and 32-bit and 64-bit platform support) – enough hours to run
    continuously each month``*``
-   750 hours of `Amazon EC2`_ Microsoft Windows Server Micro Instance
    usage (613 MB of memory and 32-bit and 64-bit platform support) – enough
    hours to run continuously each month``*``
-   750 hours of an `Elastic Load Balancer`_ plus 15 GB data processing*
-   30 GB of `Amazon Elastic Block Storage`_, plus 2 million I/Os and 1
    GB of snapshot storage``*``
-   5 GB of `Amazon S3`_ standard storage, 20,000 Get Requests, and 2,000
    Put Requests``*``
-   100 MB of storage, 5 units of write capacity, and 10 units of read
    capacity for `Amazon DynamoDB`_.**
-   25 `Amazon SimpleDB`_ Machine Hours and 1 GB of Storage``**``
-   1,000 `Amazon SWF`_ workflow executions can be initiated for free. A
    total of 10,000 activity tasks, signals, timers and markers, and 30,000
    workflow-days can also be used for free``**``
-   100,000 Requests of `Amazon Simple Queue Service`_``**``
-   100,000 Requests, 100,000 HTTP notifications and 1,000 email
    notifications for `Amazon Simple Notification Service`_``**``
-   10 `Amazon Cloudwatch`_ metrics, 10 alarms, and 1,000,000 API
    requests``**``
-   15 GB of bandwidth out aggregated across all AWS services``*``


我已把未送到 `bitbucket.org`_ 的專案及 zotero webdav 丟上 AWS 了。

自己家裡的機器正式結束「網站」的工作，專職作「寫程式機」了。



.. _Amazon Web Service: http://aws.amazon.com/
.. _GAE: https://developers.google.com/appengine/
.. _boto: https://github.com/boto/boto
.. _AWS Management Console: https://console.aws.amazon.com/
.. _Elastic IPs: https://console.aws.amazon.com/ec2/home?region=us-
    west-1#s=Addresses
.. _免費試用方案: http://aws.amazon.com/free
.. _Amazon EC2: http://aws.amazon.com/ec2
.. _Elastic Load Balancer: http://aws.amazon.com/elasticloadbalancing/
.. _Amazon Elastic Block Storage: http://aws.amazon.com/ebs (EBS)
.. _Amazon S3: http://aws.amazon.com/s3
.. _Amazon DynamoDB: http://aws.amazon.com/dynamodb/
.. _Amazon SimpleDB: http://aws.amazon.com/simpledb
.. _Amazon SWF: http://aws.amazon.com/swf
.. _Amazon Simple Queue Service: http://aws.amazon.com/sqs (SQS)
.. _Amazon Simple Notification Service: http://aws.amazon.com/sns (SNS)
.. _Amazon Cloudwatch: http://aws.amazon.com/cloudwatch
.. _bitbucket.org: http://bitbucket.org/


.. author:: default
.. categories:: chinese
.. tags:: zotero, mysql, linux, python, s3, rds, ec2, boto, google app engine, amazon web service, postgresql, oracle
.. comments::
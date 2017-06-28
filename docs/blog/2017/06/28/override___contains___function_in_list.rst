將錯就錯: 子類別覆載(Override)父類別函式
===============================================================================

多年前，寫了一個內部用的除錯系統，因為有可能登入模組本身就是有 bug 的，\
為了降低系統的複雜性，所以不以 django auth 架構作身份驗證，\
單純檢查 remote_ip 有沒有在 settings.INTERNAL_IPS 裡來達到安全性檢查:

.. code-block:: python
    :linenos:

    from django.conf import settings
    def check_internal_ips(function):
        def _inner_function(*args, **kw):
            request = args[0]
            if hasattr(settings, 'INTERNAL_IPS') and request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
                return function(*args, **kw)
            else:
                return HttpResponseForbidden('You have no right!!!')
        return _inner_function

    @check_internal_ips
    def list_bugrecords(R):
        """ list the latest 10 records about automated bug tracker
        """
        pass

但這有一個問題，每次家裡 IP 有變動，或是在別的地方處理 bug 時，\
就得先登入機器內部修改 settings.py 才能從網頁上閱讀 bug 紀錄。\
實在不方便，大概拖了近 10 年之久了，今天終於改良了這個功能。

.. more::

因為 check_interla_ips 函式是位在一個獨立的 ho600_lib 函式庫中，\
不想破壞原本簡單的安全性驗證方式，\
所以 override 原 list 物件的 __contains__ 函式來作「額外 IP 」的查詢:

.. code-block:: python
    :linenos:

    # settings.py
    class CheckIPInSG(list):
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        region_name = 'us-west-2'
        security_group_ids = ['sg-12345678', 'sg-87654321']

        def __contains__(self, remote_ip, *args, **kw):
            result = super(CheckIPInSG, self).__contains__(remote_ip, *args, **kw)
            if result: return True
            #INFO: above is just equivalent '"X.Y.Z.W" in list', if False, then run below

            import boto3, netaddr
            ec2 = boto3.resource('ec2',
                                 aws_access_key_id=self.aws_access_key_id,
                                 aws_secret_access_key=self.aws_secret_access_key,
                                 region_name=self.region_name)
            for sg in ec2.security_groups.filter(GroupIds=self.security_group_ids):
                for rule in sg.ip_permissions:
                    for ip in rule['IpRanges']:
                        if netaddr.IPAddress(remote_ip) in netaddr.IPNetwork(ip['CidrIp']):
                            return True
            return False
    INTERNAL_IPS = CheckIPInSG(['127.0.0.1', '192.168.1.1', '192.168.1.2', '192.168.1.254'])

其中 CheckIPInSG 繼承了 list 類別，並 override(覆載) __contains__ 函式，\
此函式被執行的時間點就在 request.META.get('REMOTE_ADDR') \
in settings.INTERNAL_IPS 時。\
作 in 運算其實就是在執行 settings.INTERNAL_IPS.__contains__(\
request.META.get('REMOTE_ADDR')) 。

於是，系統在原始 ['127.0.0.1', '192.168.1.1', '192.168.1.2', '192.168.1.254'] \
比對不到 REMOTE_ADDR 時，就往 AWS EC2 SecrityGroups 去查詢，\
只要有查到 REMOTE_ADDR 就回傳 True ，完全找不到就回傳 False 。

其中利用 AWS EC2 Security Groups 來存 ip 的作法，\
也可以改成在 allow-my-ips.ho600.com 作 DNS A 紀錄來儲存。\
這樣就不用去變動 ho600_lib 內部的任何一行程式碼來達成新需求。

.. author:: default
.. categories:: chinese
.. tags:: AWS, python
.. comments::

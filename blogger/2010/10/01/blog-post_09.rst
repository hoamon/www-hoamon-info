工程施工項目預算編列
================================================================================

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TLAhWBWYsbI/AAAAAAAACmY/yyM
kzoYBkpw/s400/contract_price.png
`_
本文與台北花博爭議有間接關係，當然不是因為我要為郝龍斌說話，也不是要撻伐他。只是純粹就「工程施工項目編算編列」這個讓大家都有話說的爭議問題來提供我的所學。

基本上，我對整個花風暴的資訊掌握的不如他們局內人了解，所以，我只是分享我在「營建管理」這個學科所學到的東西。

常收看這個 blog 的朋友們，或許會認為我學的是資訊方面的學科，畢竟我發的文多半是 python, google app engine,
mercurial, django 相關的文章，不過，我可是道道地地的土木系學生，從大學、研究所，一直到現在的營建管理博士班。

一個傳統的土木系學生主要有幾種專長可以選擇： 結構、大地、水利、測量、運輸、建築、環工、營建管理(奇怪我記得應該有九項的，到底少了那一項?)，其中建築、環
工、運輸多半早已分家，而水利、測量、營建管理則視學校發展方向而有所不同，像中興土木就包含了結構、大地、水利、測量、營建管理，但逢甲土木就只有結構、大地、測
量、營建管理。

而這次大家吵得十分火熱的話題，也就是營建管理學生應當了解的課題： 工程預算編列。

一個營建專案的生命周期有五個階段： 規劃構想(業主)、設計(工程顧問/建築師)、發包(業主)、施工(營造廠)、保固營運(管理公司/業主)。由業主針對本身需
求提出構想，委託顧問公司設計，確認施工圖說後，由業主招開發標程序依「最有利標」或「最低價標」方式委託營造廠商施工，在施工階段，由監造單位(業主/工程顧問/
建築師)負責監督施工品質及工期，待驗收合格後，由廠商向業主請款，通常會保留 10%
工程款，作為保固工作之保證，最後再交由業主或管理公司管理最終產品(大樓、橋梁、道路…)。

一個項目單價編列會有三個單位接觸到這件事： 業主、設計公司、營造廠。這也就是工信為什麼會在報上刊登`聲明稿`_，請台北市政府說明為何不採用工信編列之項目單
價，而是使用自己編列的預算書。而這份市政府決定的預算書現在卻被叮得滿頭包。

再回到生命周期五個階段，這次聚焦在預算編列上，業主在規劃構想階段中，首先要先拿到錢，如果是公家機關，它們可能是從上級單位那邊拿到錢，然後要針對某種計劃，給
予它特定金額，而這個計畫下又會分好幾種工程，這些工程主要是呼應所屬計畫的目的，如中央政府提出八年八百億要治水，它就會拿一筆錢給水利署，而水利署也會提出幾個
計畫來達到治水目標，像是易淹水計畫…等，而這個易淹水計畫中，轄下再分成幾個工程，而這幾個工程就會交由水利署工程專業人員主導，把錢花掉，來換回工程設施，就公
共工程預算分配課題可詳讀我`學弟的論文`_來了解。

工程專業人員在拿到工程預算後，就會委託設計單位，或自行設計工程的施工圖說，並撰寫分標計畫書、施工綱要計畫書、工程數量概算書…等。這個工程的建造金額在設計後
，發現其小於預算金額，則會回沖到所屬計畫中由其他工程支領，若不足則反之，又或者直接刪減設計。而這個建造金額是怎麼來的，就是在施工圖說中，由設計單位作了工料
分析，統計出要多少材料(鋼筋、混凝土、模版)、多少人工(鋼筋綁紮工、模版工)的數量，再乘以各項單價得之。

這個規劃總價與實際建造金額真的相等嗎? 不可能!!!

在規劃總價中，通常工料分析的數量是不準的，而且單價也是不準的。數量不準其原因是，設計單位在設計階段，是否能得到施工現地的詳細資訊，如基地高程、地質報告、水
流速度、流量…等，以基地高程來說，若取得點不夠多，則其他位置就必須用內插法代換，當然也可以使用航空測量，不過飛機一起飛就要 40
萬(之前聽說的，不知行情有沒有變)。詳細的資訊是得用錢去換來的。那基地高程數據不準確，在整地時就會造成挖填不平衡
*1，像土方量過多的話，原本設計上沒有棄土作業，結果在實際整地上，就會出現棄土作業，數量從 0 變成 N 。

* 註1 挖填平衡，是指在整地作業上，要將原本過高的基地經過機具的開挖把土方運至過低的基地填入，而通常我們希望在一個建造基地中，挖方量是等於填方量的，這樣
我們就不需要從外地運入土方，或是將本地土方運至外地。可減少運輸成本及環境汙染成本。

那單價不準的原因在於時間因素及供應商因素兩種。在規劃工程到實際建造工程中間，短則半年，長則 10 年(像是水壩、高鐵)，這麼長的時間，都可以讓鋼筋從一噸
9 千漲到 4 萬，再跌到 1 萬 4 了，那你還會覺得單價準有必要嗎?
OK，我舉的例子太極端了，設計單位也的確不能因工期長，就亂訂單價，他們還是得自行訪價，自行訪價大致有三種方法：
機關內部訂價、電訪供應商、`營建物價`_(工商廣告： 這是我學長負責的，乃國內第一名的專業營建物價報告)。




-   機關內部訂價： 依過去工程經驗，明定工料價格，提供內部人員編列預算之用。其缺點為機關內部資料不夠豐富，還是有工料會沒有明確訂價。


-   電訪供應商： 從供應商那邊得到報價資訊。其缺點為一個施工項目要打三通電話(如果你都有這些供應商的電話)的話，一個工程若有 3000
    個項目，你覺得設計單位會乖乖每個項目都認真訪價嗎? 而且你問的供應商，也不是實際營造廠所配合的供應商，那設計單價真的能符合施工單價嗎?


-   營建物價：
    因應「機關內部訂價」不夠豐富，而「電訪供應商」又麻煩且不具公正性，所以營建研究院對國內的設計單位提供「營建物價」資訊，由他們幫你打電話，而且不只問
    3 家，提供高達 4000 項的常見營建工料價格資訊。




如果「營建物價」都已提供價格資訊了，那這次花博相關工程直接套用，不就行了。何必自己生單價數據呢? 原因在於「營建物價」是包山包海，不過它還是沒包到宇宙呀!
我相信，這次花博的「馬蘭花」、「龍吐珠」的報價資訊，它一定沒有，所以這二項報價又回到使用「電訪」方式。

看到這裡，你會不會覺得公共工程的錢，好像花得不踏實，居然在設計時，沒有一個公正且明確的項目單價分析表來決定出工程真正的成本價，然而這就是營建專案的特性：規
模大、項目雜、工期長所造成的。無法明確定出成本價也沒有關係，因為到時候成本價也會被營造廠商的投標價所修改，且通常是往下修改。

當設計單位決定施工圖說後，業主就會進行發包招標程序，採用`最有利標`_或是最低標方式發包。在最低標中，營造廠商只提供一個工程總價，只要它的工程總價比其他在
場的營造廠商低，它就得標了。而得標後，業主與營造廠商就會簽約，約定該工程各項施工細節，而其中，就重要的是「單價分析表」，這個單價分析表乃紀錄該工程有多少施
工項目，每個施工項目的施作數量，及施工項目的單價。

前述所提之單價分析表，除了設計單位要製作，營造廠商也會製作一套內部的單價分析表。

營造廠商在提出投標總價前，它會作幾件事，將招標的施工圖說拿來分析，研究設計單位提供的各項現地測量、實驗報告，得到自己一套的工料數量，再透過供應商報價或「營
建物價」刊物決定每個項目的單價，再加上可接受的利潤成數，這樣就能得到一個「營造總價金額」，如果以這個「營造總價金額」去投標，且幸運得標後。業主與營造廠商就
會協調(合併)出一套契約項目單價分析表，把雙方自己分析的表合併成一張。並依照這張契約項目單價分析表，作為廠商請款依據。

契約項目單價分析表的合併有二個限制，一、契約項目的總價就是廠商的得標價，這也就是工信在聲明稿中第二點所強調的『本工程契約除訂約總價與決標總價相同之外，契約
個別項目單價是依據政府機關的預算而來，與本公司實際投標單價並不相同。』，這是其來有自的呀!; 二、契約項目的施工數量必須依照業主招標文件，就算業主認定該工
程沒有棄土作業，但營造廠商評估一定會多餘土方要棄土而且是營造廠商考量正確，也必須依照業主招標文件。所以在這兩者的限制下，惟有調整各項契約的單價方可滿足。

從這裡看來，就可以知道項目單價是不可能與實際市價相符的。有可能因為設計單位認定的數量計算過低，所以單價必須往上調，也有可能是營造廠商以超低價搶標，造成單價
往下調。所以當你提出某個項目單價去評估它與市價有所差別，這都是不盡合理的。

在合併契約項目單價分析表上，營造廠商會提出一套，而業主也會提出一套，但通常是採用業主的。為什麼?
因為出錢的人最大。另一方面，也因為從調整單價數據上，可能會讓營造廠商有超額利潤，或是增加工程無法完工的風險。

契約項目單價分析表是廠商計價的依據，對廠商而言，它一定希望將較早施工的項目單價調高一點(這個動作一定會讓較晚施工的項目單價變低，因為「總價不變」的限制)，
這樣它在早期施工時，可得到超額利潤，雖然在晚期施工時，它會是賠錢施工的，不過，這部份的成本早在之前就領到了。我們來看看下面這個簡單例子。

::
    業主編定的XXX工程契約項目如下:
        A工項: 設計數量 1000 ，施工開始日 1 ，施工完成日 10 ，單價 100 元
        B工項: 設計數量 1000 ，施工開始日 6 ，施工完成日 15 ，單價 450 元
        C工項: 設計數量 1000 ，施工開始日 16 ，施工完成日 30 ，單價 350 元
        廠商利潤: 設計數量 1 ，施工開始日 1 ，施工完成日 30 ，單價 100 元

::
    營造廠商編定的XXX工程契約項目如下:
        A工項: 設計數量 1000 ，施工開始日 1 ，施工完成日 10 ，單價 800 元
        B工項: 設計數量 1000 ，施工開始日 6 ，施工完成日 15 ，單價 50 元
        C工項: 設計數量 1000 ，施工開始日 16 ，施工完成日 30 ，單價 50 元
        廠商利潤: 設計數量 1 ，施工開始日 1 ，施工完成日 30 ，單價 100 元


由業主的單價分析表來看，可繪製下圖的藍線，而廠商的則是繪出紅線。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TLAlGKe4-8I/AAAAAAAACmg/U6l
sMvTLazA/s400/ori.png
`_

上圖是預定進度曲線，橫軸是工作日，縱軸是進度百分比。因為每個項目都有先後施工依據，所以每張單價分析表，都可以繪出這條曲線，而這條曲線往往是 S
型的，所以又稱 S curve 。

在上圖中，我們假設藍線是真實世界的預定進度曲線，但契約項目單價分析表卻是簽紅線版本的話，這代表廠商得到了紅線減藍線面積的現金流量利息，這是對「有良心」廠商
的超額利潤。又或者遇到的是「沒良心」的廠商，它會在第 10 日請款，並在一領到錢後馬上倒閉，這樣它會領到 86% - 8.6%(保固保證金) -
10%(期初繳交的履約保證金) = 67.4% 的價款，但此時，它卻只支付 37% 的貨款，而且還有可能都是開票的，所以它實際上可得到大於 30.4%
的差價。

所以呀! 本來業主就不會相信廠商提出的單價分析表，而是會自己生一套。

而業主在調整契約項目單價分析表上，如果只是單純就以得標價與預算金額作等比例的調整，那還簡單。如藍線版本，是招標時的單價分析表，而實際開標後，廠商以 92
折得標，那一律把單價乘以 92 折不就結了。如果世界這麼簡單美好，那很多人就沒有工作了。

一個工程的契約項目從 300 個到幾萬個都有可能，而有些工項是固定費用，如工程保險、試驗費用，有些工項是其他工項的等比例金額，如廠商利潤、營業稅，有些工項
在未來又可能遇到變更設計，需要增減數量，如果現在的單價調整的不合理，等到變更設計時，大家就會吵翻天。所以就單價調整工作本身來說，它本來就不是一件簡單的事，
這部份可詳讀蔡昇穎的`「工程採購標價審查與合約單價調整機制之研究」`_一文。

簡單講，如果該工程在簽定契約項目單價分析表後，並沒有變更設計(增減施工數量)，且工程品質完全通過監造要求，並依約完工的話，契約項目單價分析表訂得隨便一點也
不會有爭議，一朵蘭花要訂 200 元或是 2000 萬都沒關係，因為工程總價就是標價，差別只是廠商多領點利息或是少領點利息而已。

但如果有變更設計的話，那單價有沒有按照市價就很重要了，因為變更設計的數量，會對總工程款造成爭議。像是原本簽訂 1 朵蘭花單價 1000
萬，結果市政府覺得原先規劃的 10 朵蘭花太少了，要求再增加 10 朵，這樣工程款就會暴增 1 億，這樣合理嗎?
又或者反過來說，市政府後來覺得這次花博應該展示較稀有的花卉，所以就不展示蘭花了，在變更設計後，會讓整個工程款少 1 億，你覺得營造廠商作得下去嗎?

結論：




1.  無法期待一個幾年後才完工的工程，在規劃設計時就明確定出它的工料數量。


2.  只單看幾個施工項目的單價是不盡情理的。


3.  變更設計時，施工項目的單價才重要。


4.  施工項目訪價時，要善用「`營建物價`_」(再一次工商廣告)




以上是我對契約項目單價分析表相關資訊的分享，然而這內容畢竟是我參與政府機關計畫案中，從部份公務員口中聽來的，再混合課本所學，所以並不全面，且我本身尚無任何
工程實務經驗，如果有所闕漏錯誤，懇請指教。

.. _: http://3.bp.blogspot.com/_eKM9lHjTZjs/TLAhWBWYsbI/AAAAAAAACmY/yyMkz
    oYBkpw/s1600/contract_price.png
.. _學弟的論文: http://ndltd.ncl.edu.tw/cgi-
    bin/gs32/gsweb.cgi?o=dnclcdr&s=id=%22097NCHU5015034%22.&searchmode=basic
.. _營建物價: http://www.tcri.org.tw/chtv2/th/th.htm
.. _最有利標: http://plan3.pcc.gov.tw/govorder/intro.htm
.. _由業主的單價分析表來看，可繪製下圖的藍線，而廠商的則是繪出紅線。: http://3.bp.blogspot.com/_eKM9lHjTZ
    js/TLAlGKe4-8I/AAAAAAAACmg/U6lsMvTLazA/s1600/ori.png
.. _「工程採購標價審查與合約單價調整機制之研究」: http://ndltd.ncl.edu.tw/cgi-
    bin/gs32/gsweb.cgi?o=dnclcdr&s=id=%22096NCU05718007%22.&searchmode=basic


.. author:: default
.. categories:: chinese
.. tags:: construction management
.. comments::
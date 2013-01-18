再改寫「背包問題」的求解程式碼
================================================================================

之前的`作法`_是將 cut 函式所計算的 list 結果直接 append 到全域變數 tmps 中，這樣的 cut 函式是無法作 decorator
的。

新方法則是把 cut 函式的 input, output 重新規劃，讓答案就是 return 值，這樣 input 就能對應到單一 output
，透過這個特性，我們就能加上一個 @cache decorator ，去作快取。因為在求解的過程中，勢必會遇到重覆的 input
，有了快取，可以少算一次。

其中的 _no_cache_count 值指的是第一次遇到的 input 值，而 _cache_count 值則是利用 dictionary
找到答案的次數。

要怎麼建構出 cut 函式的樣貌? 我們一開始先抽象地想像這個 cut 函式要作到的事就是 answer = cut(bar, sizes)

answer 是我們要的答案，結構是 list of list( [[ , , , ..], [ , , , ..], ..] )。而 bar 是原長度，
sizes 則是需求尺寸的 list 。

假設我們帶 bar = 10， sizes = [7, 5, 3, 2] ，那麼經過 cut 運算，就能得到一個 list of list 的
answer，那到底 answer 是多少? 我們先不管。但我們可以知道 10 拿給 7 去切，可以得到 0, 1 兩種組合。

所以 cut(10, [7, 5, 3, 2]) 一定會等於 cut(10, [5, 3, 2]) 的結果其解全部在元素 0 的位置插入 0 +
cut(3, [5, 3, 2]) 的結果其解全部在元素 0 的位置插入 1 。

一樣地， cut(10, [5, 3, 2]) 也會等於 cut(10, [3, 2]) 的結果其解全部在元素 0 的位置插入 0 + cut(5,
[3, 2]) 的結果其解全部在元素 0 的位置插入 1 + cut(0, [3, 2]) 的結果其解全部在元素 0 的位置插入 2 。

直到 cut(10, [2]) 時，我們知道它的結果就是 ([5], ) ，為什麼是一個 tuple of list ? 因為之前我們就定義 cut
一定要回傳 list of list ，而因為這次的 cut 回傳值本身並不會被修改，所以傳個 tuple
回去，可以少用一滴滴的記憶體(應該是一滴滴而已)。

當開始有 answer 被回傳後，我們就開始作合併的工作(就是把前一個需求尺寸的用量插入 answer 內的 list)。合併後再回傳。

程式碼如下，不過在實際跑的時候，有二件事我不能理解，為了比較 cut 與 cache_cut 的效率差別，我在同一個行程上分別跑了兩次 cut, 兩次
cache_cut ，而順序是 cache_cut, cut, cut, cache_cut ，cache_cut 比 cut
快，這很容易理解，但第二次的 cut 居然會比第一次的 cut 還慢，這我就不懂了。

另外，我每次跑 cut 之前，都是用 cs = CutSteel(bar, sizes) 創建新的物件，為什麼第二次跑的 cache_cut
，它還是可以找到第一次 cache_cut 所儲存的 CACHE 呢?

最後，我還得到一個結論，當解答組合數不多時，用 cut 會比 cache_cut 快。因為小題目，遇到重覆 input 少，但如果還是全部的 input
要儲存 CACHE ，那所花費的時間還不夠重覆 input 所節省的時間了。

::
      1 #!/usr/bin/env python
      2 # -*- coding: utf8 -*-
      3 import types
      4
      5
      6
      7 class CutSteel:
      8     u"""  目的：解鋼筋切割的組合問題(也就是背包問題)，但不只是求組合數，
      9                 也要把所有的組合列出。
     10           例： 10 公尺長的鋼筋，要切成 7, 5, 3, 2 公尺等，有多少種組合。
     11           解：
     12                  7  5  3  2
     13                 [1, 0, 1, 0]
     14                 [1, 0, 0, 1]
     15                 [0, 2, 0, 0]
     16                 [0, 1, 1, 1]
     17                 [0, 1, 0, 2]
     18                 [0, 0, 3, 0]
     19                 [0, 0, 2, 2]
     20                 [0, 0, 1, 3]
     21                 [0, 0, 0, 5]
     22     """
     23     def __init__(self, bar, sizes):
     24         if type(bar) != types.IntType or bar <= 0:
     25             raise ValueError(u'只接受正整數')
     26         for s in sizes:
     27             if type(s) != types.IntType or s <= 0:
     28                 raise ValueError(u'只接受正整數')
     29
     30         self._no_cache_count = 0
     31         self._cache_count = 0
     32
     33
     34     def cache(my_function):
     35         CACHE = {}
     36         def inner_function(*args):
     37             key = str(args[1:])
     38
     39 #            try:
     40 #                #INFO 用 try 的會比 if 慢一點點。只慢一點點。
     41 #                CACHE[key]
     42 #                args[0]._cache_count += 1
     43 #            except KeyError:
     44 #                args[0]._no_cache_count += 1
     45 #                CACHE[key] = my_function(*args)
     46
     47             if not CACHE.get(key, None):
     48                 CACHE[key] = my_function(*args)
     49                 args[0]._no_cache_count += 1
     50             else:
     51                 args[0]._cache_count += 1
     52             return CACHE[key]
     53
     54         return inner_function
     55
     56
     57     @cache
     58     def bag(self, total, sizes):
     59         u""" 只計算組合數 from thinker"""
     60         propers = tuple([sz for sz in sizes if sz <= total])
     61         if not propers:
     62             if total >= self._minsize: return 0
     63             else: return 1
     64
     65         num = self.bag(total - propers[0], propers) +
     self.bag(total, propers[1:])
     66         return num
     67
     68
     69     def cut(self, total, sizes):
     70         u""" 本函式的 input 為「被切割長度」及「欲切割的種數」。
     71
     72             output 為該 input 的所有組合。
     73         """
     74         if len(sizes) == 1:
     75             return (
     76                     [(total / sizes[0]), ],
     77                     )
     78         elif total < sizes[-1]:
     79             return (
     80                     [0,] * len(sizes),
     81                     )
     82
     83         return [
     84                 [j] + tr
     85                     for j in xrange(0, total / sizes[0] + 1)
     86                     for tr in self.cut(total - sizes[0] * j,
     sizes[1:])
     87                 ]
     88
     89
     90     @cache
     91     def cache_cut(self, total, sizes):
     92         u""" 因為 cache_cut 函式本身是具有固定 input 就會產生固定 output ，
     93             它們具有一對一或多對一的關係，所以我把 input,
     94             output 放在一個 dictionary 中，若程式計算到相同的 input 時，
     95             可免計算，直接從 dictionary 拿答案。
     96
     97             其實本函式就是複製 cut 函式後，
     98             將函式內程式碼中的 self.cut 改成 self.cache_cut ，
     99             並在函式名前加上 @cache 而已。
    100         """
    101         if len(sizes) == 1:
    102             return (
    103                     [(total / sizes[0]), ],
    104                     )
    105 #        elif total < sizes[-1]:
    106 #            #INFO 多這個判斷式反而變慢了。因為已經用 cache 了，
    107 #            #所以那些 total < sizes[-1] 情況會變成比較少，
    108 #            #然而在一個 cache_cut 函式中多加一個 if ，則判斷時間會多一倍,
    109 #            #加速效果反而不如預期。
    110 #            return (
    111 #                    [0,] * len(sizes),
    112 #                    )
    113
    114         return [
    115                 [j] + tr
    116                     for j in xrange(0, total / sizes[0] + 1)
    117                     for tr in self.cache_cut(total - sizes[0] *
    j, sizes[1:])
    118                 ]
    119
    120
    121
    122 from time import time
    123 import sys
    124 if __name__ == '__main__':
    125     #bar = sys.argv[1:]
    126     #sizes = sys.argv[2:]
    127     bar = 10
    128     sizes = [7, 5, 3, 2]
    129     sizes.sort(reverse=True)
    130     sizes = tuple(sizes)
    131
    132     cs = CutSteel(bar, sizes)
    133     cs._minsize = min(sizes)
    134     print 'Total count: %s' % cs.bag(bar, tuple(sizes))
    135
    136     cs = CutSteel(bar, sizes)
    137     time0 = time()
    138     result = cs.cache_cut(bar, sizes)
    139     print 'cache_cut spend time: %s' % (time() - time0)
    140     print len(result)
    141     print('\tno cache count: %s, cache count:
    %s'%(cs._no_cache_count, cs._cache_count))
    142
    143 #    cs = CutSteel(bar, sizes)
    144 #    time0 = time()
    145 #    result = cs.cut(bar, sizes[:])
    146 #    print 'cut spend time: %s' % (time() - time0)
    147 #    print len(result)
    148 #    print('\tno cache count: %s, cache count:
    %s'%(cs._no_cache_count, cs._cache_count))
    149 #
    150 #    cs = CutSteel(bar, sizes)
    151 #    time0 = time()
    152 #    result = cs.cut(bar, sizes[:])
    153 #    print 'cut spend time: %s' % (time() - time0)
    154 #    print len(result)
    155 #    print('\tno cache count: %s, cache count:
    %s'%(cs._no_cache_count, cs._cache_count))
    156 #
    157 #    cs1 = CutSteel(bar, sizes)
    158 #    time0 = time()
    159 #    result = cs1.cache_cut(bar, sizes[:])
    160 #    print 'cache_cut spend time: %s' % (time() - time0)
    161 #    print len(result)
    162 #    print('\tno cache count: %s, cache count:
    %s'%(cs._no_cache_count, cs._cache_count))
    163
    164     for i in xrange(0, len(result)):
    165         print(result[len(result)-i-1])


.. _作法: http://hoamon.blogspot.com/2007/12/blog-post_20.html


.. author:: default
.. categories:: chinese
.. tags:: python, math, knapsack problem, computer, cmclass
.. comments::
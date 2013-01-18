另一種解鋼筋切割組合問題(無界背包問題)的方法(改自 thinker 所提觀念)
================================================================================

::
    #!/usr/bin/env python
    # -*- coding: utf8 -*-
    """ cut(10, [7, 5, 3, 2]) = cut(3, [7, 5, 3, 2]) + cut(10, [5, 3, 2])
    """
    def _plus1(a):
        a[0] += 1
        return a


    def _cache(my_function):
        CACHE = {}
        def inner_function(*args):
            key = str(args[:])
            if not CACHE.get(key, None):
                CACHE[key] = my_function(*args)
            return CACHE[key]

        return inner_function


    @_cache
    def cut(total, sizes):
        propers = tuple([sz for sz in sizes if sz <= total])
        if len(propers) == 1:
            return
            [[0,]*(len(sizes)-len(propers))+[total/propers[0],],]
        elif not propers:
            if total < 0:
                return []
            else:
                return [[0,]*len(sizes),]

        result1 = [_plus1(a) for a in cut(total-sizes[0], sizes)]
        result2 = [[0, ]+a for a in cut(total, sizes[1:])]
        return result1 + result2


    if __name__ == '__main__':
        from time import time

        bar = 10
        sizes = [7, 5, 3, 2]

        t0 = time()
        answer = cut(bar, sizes)
        print time() - t0

        print 'count: %s'%len(answer)
        #for a in answer:
        #    print a, sum([j*sizes[i] for i, j in enumerate(a)])


其計算邏輯是 cut(10, [7, 5, 3, 2]) = cut(3, [7, 5, 3, 2]) + cut(10, [5, 3, 2])
，這觀念從 `Thinker`_ 那邊學來的，它用在計算 cut(10, [7, 5, 3, 2])
的組合數有多少時，非常非常快，不過，我在擴充至求組合數有那些時，這方法的速度就比不上 `cut(10, [7, 5, 3, 2]) = (cut(10,
[5, 3, 2]) 的結果，其元素 0 插入 0) + (cut(3, [5, 3, 2]) 的結果，其元素 0 插入 1)`_ 了。

不曉得是不是我在運算過程中，那裡少了優化?

.. _Thinker:
    http://heaven.branda.to/~thinker/GinGin_CGI.py/show_id_doc/230
.. _cut(10, [7, 5, 3, 2]) = (cut(10, [5, 3, 2]) 的結果，其元素 0 插入 0) + (cut(3,
    [5, 3, 2]) 的結果，其元素 0 插入 1): http://hoamon.blogspot.com/2011/09/blog-
    post_15.html


.. author:: default
.. categories:: chinese
.. tags:: python, knapsack problem, cmclass
.. comments::
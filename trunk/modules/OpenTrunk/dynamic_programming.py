#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    前情提要： http://hoamon.blogspot.com/2007/09/blog-post_18.html

    完整題目： http://docs.google.com/Doc?id=dgkwg8bx_160gvhgw6

    程式概念： 
    
        解答的資料結構:

            Res = {
                27: {
                    'cost': 40 , 'list': [5, 1, 3, 10, 2, 0, 0, 6, 0, 0],
                    'costlist': [10, 1, 4, 15, 2, 0, 0, 8, 0, 0]
                },
                ....
            }

            27 代表當年度的總機組數量， cost 值代表在每年購買量為 [5, 1, 3, 10, 2, 0, 0, 6, 0, 0] 時的總成本，
            costlist 陣列則是每年購買成本。

        成本矩陣：

            Cost = [
                [0 , 2 , 5 , 7 , 9 , 10 , 12 , 16 , 18 , 19 , 20], # 第一年在各種購買量下的成本。
                [0 , 1 , 5 , 7 , 9 , 12 , 15 , 18 , 21 , 25 , 27], # 第二年在各種購買量下的成本。
                [0 , 2 , 3 , 4 , 7 , 9 , 10 , 13 , 15 , 19 , 22], 
                [0 , 1 , 2 , 6 , 7 , 8 , 10 , 11 , 12 , 14 , 15],
                [0 , 1 , 2 , 4 , 5 , 7 , 11 , 12 , 14 , 16 , 18],
                [0 , 2 , 3 , 6 , 9 , 11 , 12 , 13 , 16 , 17 , 21],
                [0 , 2 , 6 , 7 , 8 , 9 , 11 , 14 , 16 , 20 , 22],
                [0 , 2 , 4 , 5 , 6 , 7 , 8 , 12 , 14 , 17 , 19],
                [0 , 1 , 3 , 5 , 8 , 9 , 10 , 12 , 13 , 17 , 18],
                [0 , 3 , 7 , 10 , 12 , 15 , 18 , 21 , 24 , 25 , 27],
            ]

        需求矩陣：

            Limit = [3 , 4 , 9 , 11 , 14 , 18 , 18 , 21 , 24 , 27]

        運算流程：
            
            主要概念是把前一年度的購買組合與本年度的購買組作交叉組合配對，
            會得到本年度的購買組合，每一購買組合的形式如下：

            27: {
                'cost': 40 , 'list': [5, 1, 3, 10, 2, 0, 0, 6, 0, 0],
                'costlist': [10, 1, 4, 15, 2, 0, 0, 8, 0, 0]
            },

            27 代表當年度的總機組數量， cost 值代表在每年購買量為
            [5, 1, 3, 10, 2, 0, 0, 6, 0, 0] 時的總成本，
            costlist 陣列則是每年購買成本。

            跑完當年度的購買組合後，就把不滿足需求量機組數的購買組合刪除。

            等 10 個年度跑完後，再利用 sort_by_cost
            函式作排序，把最便宜的購買組合放到最前面。

        延伸閱讀：

            sort_by_cost 函式的原理：請參考
                http://wiki.python.org/moin/HowTo/Sorting#head-10e70070894a1bdb7580127b5cf764a44a2d6d29

            for k_i in [k for k in Res.keys() if k < Limit[i]]: del Res[k_i] 的語法等價於：

                toDel_k = []
                for k in Res.keys():
                    if k < Limit[i]: toDel_k.append(k)

                for k in toDel_k:
                    del Res[k]

"""
def sort_by_cost(x, y):
    if x.values()[0]['cost'] > y.values()[0]['cost']: return 1
    elif x.values()[0]['cost'] == y.values()[0]['cost']: return 0
    else: return -1

def getLimit(): return [3 , 4 , 9 , 11 , 14 , 18 , 18 , 21 , 24 , 27]

def getCost():
    Cost = [
        [0 , 2 , 5 , 7 , 9 , 10 , 12 , 16 , 18 , 19 , 20],
        [0 , 1 , 5 , 7 , 9 , 12 , 15 , 18 , 21 , 25 , 27],
        [0 , 2 , 3 , 4 , 7 , 9 , 10 , 13 , 15 , 19 , 22], 
        [0 , 1 , 2 , 6 , 7 , 8 , 10 , 11 , 12 , 14 , 15],
        [0 , 1 , 2 , 4 , 5 , 7 , 11 , 12 , 14 , 16 , 18],
        [0 , 2 , 3 , 6 , 9 , 11 , 12 , 13 , 16 , 17 , 21],
        [0 , 2 , 6 , 7 , 8 , 9 , 11 , 14 , 16 , 20 , 22],
        [0 , 2 , 4 , 5 , 6 , 7 , 8 , 12 , 14 , 17 , 19],
        [0 , 1 , 3 , 5 , 8 , 9 , 10 , 12 , 13 , 17 , 18],
        [0 , 3 , 7 , 10 , 12 , 15 , 18 , 21 , 24 , 25 , 27],
    ]
    return Cost

from copy import deepcopy
def Solve(interest):
    Cost = getCost()
    Limit = getLimit()
    Res = {}
    for (i, C) in enumerate(Cost):
        oldRes = deepcopy(Res)
        presumList = oldRes.keys()
        for (j, c) in enumerate(C):
            if i == 0 and j >= Limit[0]:
                thissum = j
                thiscost = c
                Res[thissum] = {
                    'cost': thiscost,
                    'costlist': [thiscost,],
                    'list': [j,]
                }
            else:
                for presum in presumList:
                    thissum = presum + j
                    if thissum < Limit[i]: continue
                    thiscost = oldRes[presum]['cost'] * (1+interest) + c
                    if Res.has_key(thissum):
                        if j == 0:
                            Res[thissum]['cost'] = thiscost
                            Res[thissum]['list'].append(j)
                            Res[thissum]['costlist'].append(c)
                        elif thiscost < Res[thissum]['cost']:
                            Res[thissum]['cost'] = thiscost
                            Res[thissum]['list'] = oldRes[presum]['list'] + [j,]
                            Res[thissum]['costlist'] = oldRes[presum]['costlist'] + [c,]
                    else:
                        Res[thissum] = {
                            'cost': thiscost,
                            'costlist': oldRes[presum]['costlist'] + [c,],
                            'list': oldRes[presum]['list'] + [j,]
                        }
        for k_i in [k for k in Res.keys() if k < Limit[i]]: del Res[k_i]
    sortRes = []
    for (k, v) in Res.items(): sortRes.append({k: v})
    #print sortRes
    sortRes.sort(sort_by_cost)
    #for i in sortRes:
    #    print '總機組數: %s' % i.keys()[0]
    #    print '\t%s' % i.values()[0]
    return sortRes[0].values()[0]['cost'], sortRes[0].values()[0]['list'], sortRes[0].values()[0]['costlist']

if __name__ == '__main__':
    (cost, list, costlist) = Solve(0.5)
    print '總成本為 %6.2f' % cost
    print '購買順序為:'
    for (i, l) in enumerate(list):
        print '第%d年購買%d台，花了%s。' % (i+1 , l, costlist[i])
    

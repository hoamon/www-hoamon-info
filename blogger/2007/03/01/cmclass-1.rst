CMCLass: 派送問題(1)
================================================================================

受強烈地震之災，USA--A區有 12 軍事基地 毀損，被迫需搬遷至 B 區 12 軍事基地。搬遷成本與軍事基地間搬遷直線距離成正比。

兩區的平面座標如下：

A區 X 座標 Y 座標
B區 X 座標 Y 座標
1 1130 863
1 1031 1206
2 1705 1283
2 1046 1000
3 1326 1736
3 1803 1809
4 975 825
4 1588 1821
5 1286 807
5 1300 1482
6 909 1143
6 1939 1228
7 1579 1608
7 1147 1703
8 1162 1118
8 1319 1254
9 876 1573
9 1300 1182
10 1198 1748
10 1817 1269
11 801 1134
11 1945 1605
12 956 1226
12 1349 1488

非常典型的 lp 問題，方程式也非常好設定。首先我們要列出這 a[12] 到 b[12] 的所有相對距離，共有 12 x 12 = 144
個，這也表示決策變數 Xij 有144個，當 Xij = 1 時，表示由 i 基地搬遷至 j 基地，當 Xij = 0 時，表示「沒事發生」。

所以目標函數就是所有相對距離 x 決策變數的總和。

接下來設定 25 條方程式：

all Xij >= 0。

sum j=1~12 Xij = 1 對所有的 i 成立。(實在不知道該如何展現數學方程式，只好用口語的方式)

sum i=1~12 Xij = 1 對所有的 j 成立。(實在不知道該如何展現數學方程式，只好用口語的方式)

這樣就有 25 條方程式了。跑一下 lp 程式就可以得到答案。

那麼 Python 如何跑 lp 程式呢!首先請裝 `GLPK`_ 函數庫，這是由 gnu 組織開發的 linear programming
toolkit ，功能還可以，但如果決策變數太多，有可能會跑不完。

理論上，你裝了 GLPK 後，就可以執行 lp 計算，但是直接用 GLPK 的話，必須用 mathprog 格式餵資料給 GLPK
，而這個格式太複雜了，所以我先去載入一個輸出 mathprog 格式的 Python 類別 `pulp`_ ，透過這個類別幫我控制 GLPK 函式庫。

以下是我的 Python 程式：

def caldest(From, To):
----from math import sqrt
----dest = []

----for start in From:
--------subdest = []
--------for end in To:
------------subdest.append(round(sqrt((start[0] - end[0])**2 + (start[1] -
end[1])**2), 0))
--------dest.append(subdest)

----return dest

def optima(coef):
----from pulp import *
----(Dest, var, obj) = (coef, [], 0)
----prob = LpProblem("dest", LpMinimize)

----for i in xrange(len(Dest)):
--------var.append([])
--------for j in xrange(len(Dest[0])):
------------(str_i, str_j) = ("%03d" % (i + 1), "%03d" % (j + 1))
------------var[i].append(LpVariable("var"+str_i+'_'+str_j, 0, 1, LpInteger))
------------obj += Dest[i][j] * var[i][j]

----prob += obj, 'OBJ.'

----for i in xrange(len(Dest)):
--------st = 0
--------for j in xrange(len(Dest[0])):
------------st += var[i][j]
--------prob += st == 1

----for j in xrange(len(Dest[0])):
--------st = 0
--------for i in xrange(len(Dest)):
------------st += var[i][j]
--------prob += st == 1

----#prob.writeLP("dest.lp")
----prob.solve()

----print "Status:", LpStatus[prob.status]

----for v in prob.variables():
--------if v.varValue >= 1:
------------print v.name[3:6] + ' => ' + v.name[7:10]

----print "objective=", value(prob.objective)

if __name__ == '__main__':
----A = [[1130, 863],
--------[1705, 1283],
--------[1326, 1736],
--------[975, 825],
--------[1286, 807],
--------[909, 1143],
--------[1579, 1608],
--------[1162, 1118],
--------[876, 1573],
--------[1198, 1748],
--------[801, 1134],
--------[956, 1226]]

----B = [[1031, 1206],
--------[1046, 1000],
--------[1803, 1809],
--------[1588, 1821],
--------[1300, 1482],
--------[1939, 1228],
--------[1147, 1703],
--------[1319, 1254],
--------[1300, 1182],
--------[1817, 1269],
--------[1945, 1605],
--------[1349, 1488]]

----dest = caldest(A, B)
----optima(dest)

執行後，得到搬遷方式為：

001 => 009
002 => 010
003 => 003
004 => 002
005 => 006
006 => 001
007 => 011
008 => 008
009 => 007
010 => 004
011 => 005
012 => 012

最小路徑為 4412.0

.. _GLPK: http://www.gnu.org/software/glpk/
.. _pulp: http://www.jeannot.org/%7Ejs/code/index.en.html#PuLP


.. author:: default
.. categories:: chinese
.. tags:: pulp, lp, python, glpk
.. comments::
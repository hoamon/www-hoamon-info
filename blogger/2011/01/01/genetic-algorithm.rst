使用 genetic algorithm 來求解非線性問題。如 y = [ sin(1*x0) * sin(2*x1) ] +  ... + [ sin(49*x48) * sin(50*x49) ]，求 y 的最大值
================================================================================

問題描述： 指定 0,1,2,.........49 等50個數字給 x0~x49(不可重複)，且

y = [ sin(1*x0) * sin(2*x1) ] + [ sin(3*x2) * sin(4*x3) ] + ... + [
sin(49*x48) * sin(50*x49) ]

請求解 y 之最大值?

本問題我使用 `pyevolve 函式庫`_來幫我處理染色體的突變、重組、交配工作。我只需要提供目標函數(eval_func)的計算方式即可。本問題我的
y 最佳解是 20.4676 ，決策變數是 [33, 26, 36, 16, 45, 28, 37, 1, 19, 2, 25, 14, 0, 22,
6, 17, 35, 24, 11, 12, 27, 42, 49, 32, 13, 20, 23, 43, 41, 30, 4, 9, 21, 3,
10, 34, 38, 15, 18, 5, 47, 39, 44, 40, 8, 7, 31, 48, 46, 29] 。
::
    ** 1 ****from** pyevolve **import** G1DList
    ** 2 ****from** pyevolve **import** GSimpleGA
    ** 3 ****from** pyevolve **import** Selectors
    ** 4 ****from** pyevolve **import** Statistics
    ** 5 ****from** pyevolve **import** DBAdapters
    ** 6 ****import** pyevolve
    ** 7 ****from** math **import** sin
    ** 8 **
    ** 9 ****""" 指定 (0,1,2,.........49 等50個數字不可重複）給 x0~x49，例如  x0=12,
    x1= 33, ....**
    **10 ****    y = [ sin(1*x0) * sin(2*x1) ] + [ sin(3*x2) * sin(4*x3)
    ] + ... + [ sin(49*x48) * sin(50*x49) ]**
    **11 ****    求解 y 之 最大值＝?**
    **12 ****"""**
    **13 **
    **14 ****def** **eval_func**(chromosome):
    **15 **    score = **20.0** **#為了不讓 score 的值小於 0，因為 pyevolve 不支援適存值小於
    0 。**
    **16 **    list = map(**lambda** a,b: (a, b), xrange(**50**),
    chromosome)
    **17 **    list.sort(key=**lambda** a: a[**1**])
    **18 **    **for** i **in** xrange(**25**):
    **19 **        score += sin((**2***i+**1**)*list[i***2**][**0**]) *
    sin((**2***i+**2**)*list[i***2**+**1**][**0**])
    **20 **
    **21 **    **return** score
    **22 **
    **23 ****# Enable the pyevolve logging system**
    **24 **pyevolve.logEnable()
    **25 ****# Genome instance, 1D List of 50 elements**
    **26 **genome = G1DList.G1DList(**50**)
    **27 ****# Sets the range max and min of the 1D List**
    **28 **genome.setParams(rangemin=**0**, rangemax=**500**)
    **29 ****# The evaluator function (evaluation function)**
    **30 **genome.evaluator.set(eval_func)
    **31 ****# Genetic Algorithm Instance**
    **32 **ga = GSimpleGA.GSimpleGA(genome)
    **33 ****# Set the Roulette Wheel selector method, the number of
    generations and**
    **34 ****# the termination criteria**
    **35 **ga.selector.set(Selectors.GRouletteWheel)
    **36 **ga.setGenerations(**5000**)
    **37 **ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    **38 ****# Sets the DB Adapter, the resetDB flag will make the
    Adapter recreate**
    **39 ****# the database and erase all data every run, you should use
    this flag**
    **40 ****# just in the first time, after the pyevolve.db was created,
    you can**
    **41 ****# omit it.**
    **42 **sqlite_adapter = DBAdapters.DBSQLite(identify=**"ex1"**,
    resetDB=True)
    **43 **ga.setDBAdapter(sqlite_adapter)
    **44 ****# Do the evolution, with stats dump**
    **45 ****# frequency of 20 generations**
    **46 **ga.evolve(freq_stats=**20**)
    **47 ****# Best individual**
    **48 ****print** ga.bestIndividual()


.. _pyevolve 函式庫: http://pyevolve.sourceforge.net/


.. author:: default
.. categories:: chinese
.. tags:: genetic algorithm, python, math, cmclass
.. comments::
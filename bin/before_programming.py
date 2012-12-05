#!/usr/bin/python
# -*- coding: utf8 -*-
from advance_hg import AdvanceHG
class Rargs:
    def __init__(self, rargs=[]): self.rargs = rargs

ahg = AdvanceHG(run_in_function=True)
a = Rargs(['-j'])
ahg.pullAll('', '--pullall', '.', a)
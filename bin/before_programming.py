#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from advance_hg import AdvanceHG
class Rargs:
    def __init__(self, rargs=[]): self.rargs = rargs

ahg = AdvanceHG(run_in_function=True)
pwd = os.path.dirname(os.path.abspath(__file__))
a = Rargs(['-j'])
ahg.pullAll('', '--pullall', os.path.join(pwd, '..'), a)
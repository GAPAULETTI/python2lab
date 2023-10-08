from sys import path
path.append('d:\\PythonEssential2\\PythonM1\\packages\\extrapack.zip')

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())
print(alp.FunA())
import modul1

print(modul1.max_1(123, 124))

import modul1 as m1

print(m1.max_1(777, 888))

from modul1 import max_1

print(max_1(125, 234))

from modul1 import *

print(max_1(567, 1234))

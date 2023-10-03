import modul1

print(modul1.max1(5, 9))  # 9

import modul1 as m1

print(m1.max1(50, 90))  # 90

# или

from modul1 import max1

print(max1(15, 204))  # 204

from modul1 import *

print(max1(15, 199))  # 199

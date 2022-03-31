import copy
from memory_profiler import profile
import numpy as np

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      7     31.0 MiB     31.0 MiB           1   @profile
#      8                                         def dz_3_9():
#      9     31.0 MiB      0.0 MiB           1       arr = [
#     10     31.0 MiB      0.0 MiB           1           [14, -4, -12, 19, 1],
#     11     31.0 MiB      0.0 MiB           1           [16, -6, 8, 7, 11],
#     12     31.0 MiB      0.0 MiB           1           [11, 2, -5, 1, 20],
#     13     31.0 MiB      0.0 MiB           1           [14, -4, -17, 15, 10]
#     14                                             ]
#     15
#     16     31.0 MiB      0.0 MiB           1       a = []
#     17
#     18     31.0 MiB      0.0 MiB           1       arr2 = np.rot90(arr)
#     19     31.0 MiB      0.0 MiB           6       for i in arr2:
#     20     31.0 MiB      0.0 MiB           5           a.append(min(i))
#     21     31.0 MiB      0.0 MiB           1       print(a)
#     22
#     23     31.0 MiB      0.0 MiB           1       print(max(a))


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     26     30.9 MiB     30.9 MiB           1   @profile
#     27                                         def manually():
#     28     30.9 MiB      0.0 MiB           1       arr = [
#     29     30.9 MiB      0.0 MiB           1           [14, -4, -12, 19, 1],
#     30     30.9 MiB      0.0 MiB           1           [16, -6, 8, 7, 11],
#     31     30.9 MiB      0.0 MiB           1           [11, 2, -5, 1, 20],
#     32     30.9 MiB      0.0 MiB           1           [14, -4, -17, 15, 10]
#     33                                             ]
#     34     30.9 MiB      0.1 MiB           2       temp = [[],
#     35     30.9 MiB      0.0 MiB           1               [],
#     36     30.9 MiB      0.0 MiB           1               [],
#     37     30.9 MiB      0.0 MiB           1               [],
#     38     30.9 MiB      0.0 MiB           1               [],
#     39                                                     ]
#     40     30.9 MiB      0.0 MiB           1       a = []
#     41
#     42     30.9 MiB      0.0 MiB           6       for c in range(0, 5):
#     43     30.9 MiB      0.0 MiB          25           for i in arr:
#     44     30.9 MiB      0.0 MiB          20               temp[c].append(i[c])
#     45
#     46     30.9 MiB      0.0 MiB           6       for i in temp:
#     47     30.9 MiB      0.0 MiB           5           a.append(min(i))
#     48
#     49     30.9 MiB      0.0 MiB           1       return max(a)

# Python 3.9.7
# Windows 10 64bit

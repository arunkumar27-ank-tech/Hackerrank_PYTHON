#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z').timestamp()
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z').timestamp()
    delta = int(math.fabs(dt1 - dt2))
    print (str(delta))



t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)



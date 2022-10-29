#!/bin/python3
# Name: Alfonso Areiza Guerra
# Date: 26/10/2022
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1: str, t2: str) -> str:
    """
    Calculates the difference in seconds of two dates,
    considering that they could be in differents time 
    zones.
        :param t1: String of first date.
            Ex.: 'Sun 10 May 2015 13:54:36 -0700'
        :param t2: Second Date
            Ex.: 'Mon 11 May 2015 23:14:22 -0000'
    :return: Result of the difference in seconds bweteen two dates

    >>> time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')
    25200
    >>> time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000')
    88200
    """
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((dt2 - dt1).total_seconds())))

import math
import os
import random
import re
import sys
n = int(raw_input().strip())   #raw_input function is used to take any input from the keyboard or from the user
#strip function is used to remove the extra spaces
if n%2!=0:
    print("Weird")
else:
    if n >=2 and n<=5:
        print "Not Weird"
    elif n >=6 and n<=20:
        print "Weird"
    elif n > 20:
        print"Not Weird"
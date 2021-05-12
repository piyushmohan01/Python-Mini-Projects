import math
import random

def alphabetic():
    if eitherOr(2)==1:return chr(random.randint(65,90))
    else:return chr(random.randint(97,122))
def numerical():
    return chr(random.randint(48,57))
def symbolic():
    if eitherOr(2)==1:return alphabetic()
    else:return chr(random.randint(33,47))
def eitherOr(n):
    return random.randint(1,n)
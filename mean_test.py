from mean import *

def testInts():
     nums = [4,5,28,3]
     obs = mean(nums)
     exp = 10
     assert obs == exp

def testZero():
    nums = [0,0,0]
    obs = mean(nums)
    exp = 0
    assert obs == exp

def testNeg():
    nums  = [-1,-1,-1]
    obs = mean(nums)
    exp = -1
    assert obs == exp

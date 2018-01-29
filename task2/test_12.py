from __future__ import division
import numpy as np

def theDiv(x):
    return x/8

def test_division_np():
    result = theDiv(np.array([2]))
    assert result[0] == 0.25
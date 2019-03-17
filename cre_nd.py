# create new ndarray
import numpy as np
one_nd = np.arange(6)
two_nd = one_nd.reshape(2,3)
print("one_nd is {0:*^20s}".format(one_nd.))
print(two_nd)
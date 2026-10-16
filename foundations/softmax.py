import numpy as np
from numpy.typing import NDArray
from math import exp

class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        expo = 0
        big = max(z)
        for i in range(len(z)):
            print(z[i])
            expo += exp(z[i] - big)
        for i in range(len(z)):
            z[i] = round(exp(z[i] - big) / expo, 4)
        return z


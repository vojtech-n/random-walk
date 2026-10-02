import numpy as np
from numpy.typing import ArrayLike, NDArray


def running_mean(x: ArrayLike) -> NDArray[np.float64]:
    values = np.asarray(x, dtype=np.float64)
    return np.cumsum(values) / np.arange(1, values.size + 1)

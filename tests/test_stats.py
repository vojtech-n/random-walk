import numpy as np

from random_walk import running_mean


def test_running_mean() -> None:
    np.testing.assert_allclose(running_mean([2, 4, 6]), [2.0, 3.0, 4.0])


def test_running_mean_empty() -> None:
    assert running_mean([]).size == 0

""" main metrics for events predictions"""

import numpy as np

__all__ = ["smape", "wmape"]


def smape(y_true, y_pred):
    eps = np.ones_like(y_true)
    return (np.abs(y_true - y_pred) / np.max([y_true, y_pred, eps], axis=0)).sum() * (
        100 / np.max(y_true.shape)
    )


def wmape(y_true, y_pred):
    numerator = np.abs(y_true - y_pred).sum()
    denominator = np.abs(y_true).sum()
    if denominator > 0:
        return 100 * numerator / denominator
    else:
        return 100 * numerator

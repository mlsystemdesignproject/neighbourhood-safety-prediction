from neighbourhood.utils.metrics import smape, wmape
import numpy as np

# 1)
# y1 = 1 1 1
# y2 = 1 1 1
# 2)
# y1 = 0 0 0
# y2 = 1 1 1
# 3)
# y1 = 1 1 1
# y2 = 0 0 0
# 4)
# y1 = 1 2 1
# y2 = 1 1 1
# 5)
# y1 = 1 1 1
# y2 = 1 2 1


def test_metric_smape_01():
    y1 = np.array([1, 1, 1])
    y2 = np.array([1, 1, 1])
    assert np.round(smape(y1, y2), 2) == 0


def test_metric_wmape_01():
    y1 = np.array([1, 1, 1])
    y2 = np.array([1, 1, 1])
    assert np.round(wmape(y1, y2), 2) == 0


def test_metric_smape_02():
    y1 = np.array([0, 0, 0])
    y2 = np.array([1, 1, 1])
    assert np.round(smape(y1, y2), 2) == 100


def test_metric_wmape_02():
    y1 = np.array([0, 0, 0])
    y2 = np.array([1, 1, 1])
    assert np.round(wmape(y1, y2), 2) == 300


def test_metric_smape_03():
    y1 = np.array([1, 1, 1])
    y2 = np.array([0, 0, 0])
    assert np.round(smape(y1, y2), 2) == 100


def test_metric_wmape_03():
    y1 = np.array([1, 1, 1])
    y2 = np.array([0, 0, 0])
    assert np.round(wmape(y1, y2), 2) == 100


def test_metric_smape_04():
    y1 = np.array([0, 0, 0])
    y2 = np.array([1, 0, 1])
    assert np.round(smape(y1, y2), 2) == 66.67


def test_metric_wmape_04():
    y1 = np.array([0, 0, 0])
    y2 = np.array([1, 0, 1])
    assert np.round(wmape(y1, y2), 2) == 200


def test_metric_smape_05():
    y1 = np.array([1, 2, 1])
    y2 = np.array([1, 1, 1])
    assert np.round(smape(y1, y2), 2) == 16.67


def test_metric_wmape_05():
    y1 = np.array([1, 2, 1])
    y2 = np.array([1, 1, 1])
    assert np.round(wmape(y1, y2), 2) == 25


def test_metric_smape_06():
    y1 = np.array([1, 1, 1])
    y2 = np.array([1, 2, 1])
    assert np.round(smape(y1, y2), 2) == 16.67


def test_metric_wmape_06():
    y1 = np.array([1, 1, 1])
    y2 = np.array([1, 2, 1])
    assert np.round(wmape(y1, y2), 2) == 33.33

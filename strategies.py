def strategy_spendpart(part=0.5):
    return lambda m, n, u, v: part * u


def strategy_spendall(m, n, u, v):
    return strategy_spendpart(1)(m, n, u, v)


def strategy_spendnone(m, n, u, v):
    return strategy_spendpart(0)(m, n, u, v)

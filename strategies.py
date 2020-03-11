def strategy_spendpart(part=0.5):
    return lambda m, n, u, v: part * u


def strategy_spendall(m, n, u, v):
    return strategy_spendpart(1)(m, n, u, v)


def strategy_spendnone(m, n, u, v):
    return strategy_spendpart(0)(m, n, u, v)

def human(m, n, u, v):
    print("The score is you: %d, opponent: %d." % (m, n))
    print("You have %.2f money and your opponent has %.2f money."
           % (u, v))

    acceptable = False
    while True:
        spend = input("How much would you like to spend? [0-%.2f] " % u)
        try:
            spend = float(spend)
        except ValueError:
            continue

        if spend < 0 or spend > u:
            continue
        else:
            return spend

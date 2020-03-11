def skillful_payoff(skill1, skill2):
    # Probability of player 1 winning a round when player 1 spends x and
    # player 2 spends y.
    return lambda x, y: (skill1 * x + 1)/(skill1 * x + skill2 * y + 2)


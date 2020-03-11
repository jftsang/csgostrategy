#!/usr/bin/env python3

import logging
import math
import random

from simulations import simulate_match, simulate_matches
from strategies import strategy_spendpart, human
from payoffs import skillful_payoff


# Play a series of matches between two strategies
# simulate_matches(strategy_spendpart(0), strategy_spendpart(0), skillful_payoff(1,1))

# Play a match against a computer
simulate_match(human, strategy_spendpart(1), skillful_payoff(1,1), verbose=True)

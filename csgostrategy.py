#!/usr/bin/env python3

import logging
import math
import random

from simulations import simulate_matches
from strategies import strategy_spendpart
from payoffs import skillful_payoff


simulate_matches(strategy_spendpart(0), strategy_spendpart(0), skillful_payoff(1,1))

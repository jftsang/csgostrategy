import logging
import random

def simulate_match(strategy1, strategy2, payoff,
        first_to=16, max_rounds=30,
        verbose=False):

    if verbose:
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.getLogger().setLevel(logging.WARNING)

    if max_rounds < first_to:
        raise ValueError("Not playing enough rounds for a victory to be possible.")

    score1 = 0
    score2 = 0
    money1 = 1;
    money2 = 1;
    reward_win = 3;
    reward_lose = 2;
    round_number = 0;

    while score1 < first_to and score2 < first_to and round_number < max_rounds:
        round_number += 1

        spend1 = strategy1(score1, score2, money1, money2)
        spend2 = strategy2(score2, score1, money2, money1)
        prob_p1win = payoff(spend1, spend2)
        logging.info("Round %d: spending %.2f, %.2f, P(p1win) = %.3f",
                round_number, spend1, spend2, prob_p1win);

        money1 -= spend1
        money2 -= spend2
        if random.random() < prob_p1win:
            score1 += 1
            money1 += reward_win
            money2 += reward_lose
            logging.info("Round %d: Player 1 wins round.",
                round_number)
        else:
            score2 += 1
            money2 += reward_win
            money1 += reward_lose
            logging.info("Round %d: Player 2 wins round.",
                round_number)

        logging.info("Round %d, score %d-%d, money %.2f, %.2f",
                round_number, score1, score2, money1, money2)

    if score1 == first_to:
        logging.info("Player 1 wins match.")
        victor = 1
    elif score2 == first_to:
        logging.info("Player 2 wins match.")
        victor = 2
    else:
        logging.info("Draw.")
        victor = 0

    result = {
        "victor": victor,
        "score1": score1,
        "score2": score2
    }
    return result


def simulate_matches(strategy1, strategy2, payoff, matches=10000):
    matches1 = 0
    matches2 = 0
    draws = 0
    rounds1 = 0
    rounds2 = 0
    for match_number in range(matches):
        res = simulate_match(strategy1, strategy2, payoff)
        if res["victor"] == 1:
            matches1 += 1
        if res["victor"] == 2:
            matches2 += 1
        if res["victor"] == 0:
            draws += 1
        rounds1 += res["score1"]
        rounds2 += res["score2"]

    logging.getLogger().setLevel(logging.INFO)
    logging.info("P1 won %d matches, P2 won %d matches, drawn %d matches",
            matches1, matches2, draws)
    logging.info("P1 won %d rounds, P2 won %d rounds",
            rounds1, rounds2)
    logging.info("P1 won %.1f%% of matches and %.1f%% of rounds",
            matches1 / matches * 100,
            rounds1 / (rounds1 + rounds2) * 100)
    logging.info("rounds per victory: P1: %.2f, P2: %.2f",
            rounds1 / matches1,
            rounds2 / matches2)

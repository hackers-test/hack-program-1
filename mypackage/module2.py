#!/usr/bin/env python


"""
A class for playing rock paper scissors
"""

import numpy as np
import pandas as pd


POSSIBLE_THROWS = np.array(["rock", "paper", "scissors"])


def make_record(trials=100, probs=(1/3, 1/3, 1/3)):
    """
    Sample 100 random throws from a professional with the results
    weighted by the person's preference/bias.

    Parameters:
    -----------
    trials: int
        Number of samples to observe from professional.
    probs: tuple
        Three values summing to 1 representing the probability of
        sampling rock, paper, or scissors in that order. Default
        is 1/3 equal probability.
    """
    return np.random.choice(POSSIBLE_THROWS, size=trials, p=probs)


def learn_freqs_from(record):
    """
    Examine professional's records and estimate frequency of throws.
    """
    # get frequency of professional's throws
    freqs = pd.value_counts(record) / len(record)
    
    # recommendation is to return winner at frequency they chose loser
    recommendation = [
        freqs["scissors"] if "scissors" in freqs else 0.0,  # return rock as freq as they return sciss
        freqs["rock"] if "rock" in freqs else 0.0,          # return paper as freq as they return rock
        freqs["paper"] if "paper" in freqs else 0.0,        # return sciss as freq as they return paper
    ]
    return recommendation


def play_rps(trials=100, probs=(1/3, 1/3, 1/3)):
    """
    Play many trials of rock-paper-scissors after first studying the
    frequency of the other players throws to learn their bias.
    """
    # sample professional's throws
    record = make_record(trials, probs)

    # get recommendations from studying their previous throws
    recommend = learn_freqs_from(record)

    # keep track of my wins
    wins = 0
    ties = 0

    # perform new trials for myself and the professional
    for _ in range(trials):

        # we both throw
        mine = np.random.choice(POSSIBLE_THROWS, p=recommend)
        theirs = np.random.choice(POSSIBLE_THROWS, p=probs)

        # compare
        if mine == theirs:
            ties += 1
        elif mine == "rock" and theirs == "scissors":
            wins += 1
        elif mine == "scissors" and theirs == "paper":
            wins += 1
        elif mine == "paper" and theirs == "rock":
            wins += 1
        # print(mine, theirs, wins)

    # if zero wins then percentage is zero
    if not wins:
        percentage = 0.0
    else:
        percentage = round(100 * wins / (trials - ties), 2)

    # report winning
    print(f"I won {percentage}% of {trials} trials (ties={ties})")


if __name__ == "__main__":

    # play a game with equal weighting
    play_rps(trials=1000)

    # play a game where they are biased towards rock
    play_rps(trials=1000, probs=[0.8, 0.1, 0.1])

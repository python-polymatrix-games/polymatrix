import numpy as np
from .logger import log
class PairFractional():
    def __init__(self, alpha, players):
        self.players = players
        self.alpha = alpha

    def __call__(self, player1: int, player2: int):
        """ Computer payoff between two players (one edge) """
        alpha = 1 / len(self.players)
        p1 = self.players[player1]
        p2 = self.players[player2]
        p1_payoff = np.zeros(2)
        p2_payoff = np.zeros(2)
        if p1.strategy != p2.strategy:
            log.debug(
                f"{self.__class__}.pair_fractional() strategy pair is: ({p1.strategy},{p2.strategy})"
            )
            p1_losing_type = [1 - p1.strategy]
            p1_losing_amount = self.payoff_function(
                x=p1.population[p1_losing_type], alpha=alpha
            )
            p1_payoff[p1_losing_type] -= p1_losing_amount
            p2_payoff[p1_losing_type] += p1_losing_amount
            log.debug(
                f"{self.__class__}.pair_fractional() p1 loss {p1_losing_type} {p1_losing_amount} {p1_payoff} {p2_payoff}"
            )
            p2_losing_type = [1 - p2.strategy]
            p2_losing_amount = self.payoff_function(
                x=p2.population[p2_losing_type], alpha=alpha
            )
            p2_payoff[p2_losing_type] -= p2_losing_amount
            p1_payoff[p2_losing_type] += p2_losing_amount
            log.debug(
                f"{self.__class__}.pair_fractional() p2 loss {p2_losing_type} {p2_losing_amount} {p1_payoff} {p2_payoff}"
            )
        log.debug(p1.label, p1.strategy, p1_payoff, p2.label, p2.strategy, p2_payoff)
        return [p1_payoff, p2_payoff]

    def payoff_function(self, x: int, alpha: float = 0.1, roundoff=False):
        """ A function that decides how much a player looses """
        # ! alpha is overriden b self.alpha
        y = x * self.alpha / (len(self.players) - 1)
        # print(f'Payoff function x={x},alpha={self.alpha},not rounded y={y}')
        if roundoff:
            y = int(y)
        log.debug(
                f"{self.__class__}.payoff_function() y={y}"
            )
        assert y >= 0
        return y
# LICENSE
see LICENSE.txt

# USAGE

from corpgame import PolymatrixGame
game_settings = {
            "start_populations_matrix": [[4,4],[2,6],[10,0]],
            "player_labels": [1,2,3],
            "topology": "fully_connected",
            'alpha': 1.0,
            'log_level': "error",
        }
game = PolymatrixGame(**game_settings)
strategies = [[0, 1, 0],[0, 0, 1], [1, 1, 0], [0, 1, 1]]

X = [[]]*(len(strategies)+1)
X[0] = game.state

for i, p in enumerate(strategies):
    game.play(p)
    game.solve()
    X[i+1] = game.state
    print('round: ', i+1)
    print('strategy: ', p)
    print('state transition: \n', X[i+1]-X[i])
    print('payoff: ', np.sum(X[i+1]-X[i], axis=1))
    print('state: \n', game.state)
    print('pne: ', game.pne)
    print()

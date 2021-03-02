import polymatrix

number_of_players = 5

manager = polymatrix.GameManager(number_of_players)
players = manager.get_random_players()

game_settings = {
    "start_populations_matrix": players,
    "topology": "fully_connected",
    'alpha': 1.0,
    'log_level': 'info'
}

game = polymatrix.PolymatrixGame(**game_settings)

timesteps = 3

print(f"Simulated for {len(players)} players")
print(f" Network topology: {game_settings['topology']}")
print(f" Game state {game.state.tolist()}")
for i in range(timesteps):
    game.play(manager.get_random_strategy_profile())
    print(f" Strategy profile: {game.strategy_profile}")
    print(f" Game state {game.state.tolist()}")
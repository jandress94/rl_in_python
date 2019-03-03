from TicTacToeEnvironment import * 
from TicTacToeAgent import * 
from TicTacToeHuman import *
from tqdm import tqdm as tqdm

def play_game(p1, p2, env, train=True, draw=False):
	# loop until game done
	current_player = None

	while not env.game_over():
		# alternate players, starting with p1
		if current_player == p1:
			current_player = p2
		else:
			current_player = p1

		# draw the board before the user who wants to see it moves
		if draw and ((draw == 1 and current_player == p1) or \
							(draw == 2 and current_player == p2)):
			env.draw_board()

		current_player.take_action(env)

		# update state histories
		if train:
			state = env.get_state()
			p1.update_state_history(state)
			p2.update_state_history(state)

	if draw:
		env.draw_board()

	# do the value function updates
	if train:
		p1.update(env)
		p2.update(env)

	return env.game_over()

p1 = TicTacToeAgent('X', epsilon = 0.2)
p2 = TicTacToeAgent('O', epsilon = 0.2)

for _ in tqdm(range(100000)):
	env = TicTacToeEnvironment()

	play_game(p1, p2, env)


# p1_values = p1.get_value_lookup()
# p2_values = p2.get_value_lookup()

# # print(p1_values)

# print(p1_values["X  \n   \n   "])
# print(p1_values[" X \n   \n   "])
# print(p1_values["  X\n   \n   "])
# print(p1_values["   \nX  \n   "])
# print(p1_values["   \n X \n   "])
# print(p1_values["   \n  X\n   "])
# print(p1_values["   \n   \nX  "])
# print(p1_values["   \n   \n X "])
# print(p1_values["   \n   \n  X"])

pHX = TicTacToeHuman('X')
pHO = TicTacToeHuman('O')


while True:
	print("Playing a game as X")

	winner = play_game(pHX, p2, TicTacToeEnvironment(), train=False, draw=1)
	if len(winner) == 1:
		print("The winner is %s" % winner)
	else:
		print("Tie Game")
		

	print("Playing a game as O")

	winner = play_game(p1, pHO, TicTacToeEnvironment(), train=False, draw=2)
	if len(winner) == 1:
		print("The winner is %s" % winner)
	else:
		print("Tie Game")
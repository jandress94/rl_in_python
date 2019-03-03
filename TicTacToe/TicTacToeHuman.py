import random

class TicTacToeHuman(object):
	"""docstring for TicTacToeHuman"""
	def __init__(self, marker):
		super(TicTacToeHuman, self).__init__()
		self.marker = marker

	def take_action(self, env):
		while True:
			move = raw_input("Enter your move: ")

			r = int(move[0])
			c = int(move[1])

			if env.get_state().get(r, c):
				print("That move is not allowed")
			else:
				break

		env.record_move(r, c, self.marker)

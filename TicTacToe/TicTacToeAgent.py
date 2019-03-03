import random

class TicTacToeAgent(object):
	"""docstring for TicTacToeAgent"""
	def __init__(self, marker, learning_rate=0.1, epsilon=0.1):
		super(TicTacToeAgent, self).__init__()
		self.marker = marker
		self.state_history = []
		self.value_lookup = {}
		self.learning_rate = learning_rate
		self.epsilon = epsilon

	def update_state_history(self, state):
		self.state_history.append(state)

	def update(self, env):
		i_won = env.game_over() == self.marker

		next_state = str(self.state_history[-1])
		self.value_lookup[next_state] = 1 if i_won else 0

		for i in range(len(self.state_history) - 2, -1, -1):
			state = str(self.state_history[i])

			curr_val = self.value_lookup.get(state, 0.5)
			next_val = self.value_lookup.get(next_state, 0.5)

			self.value_lookup[state] = curr_val + self.learning_rate * (next_val - curr_val)
			next_state = state
		self.state_history = []

	def take_action(self, env):
		possible_actions = []
		state = env.get_state()
		nrows, ncols = state.size()

		for r in range(nrows):
			for c in range(ncols):
				if not state.get(r, c):
					possible_actions.append((r, c))

		best_action = None
		best_value = -float('inf')

		for r, c in possible_actions:
			state.set(r, c, self.marker)

			next_value = self.value_lookup.get(str(state), 0.5)
			if next_value > best_value:
				best_value = next_value
				best_action = (r, c)
			state.set(r, c, None)

		if random.random() < self.epsilon:
			best_action = random.choice(possible_actions)

		r, c = best_action
		env.record_move(r, c, self.marker)

	def get_value_lookup(self):
		return self.value_lookup
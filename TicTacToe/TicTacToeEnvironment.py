import copy

class TicTacToeBoard(object):
	"""docstring for TicTacToeBoard"""
	def __init__(self):
		super(TicTacToeBoard, self).__init__()
		self.board = [[None]*3 for _ in range(3)]

	def __repr__(self):
		result_str = ""
		for r in range(len(self.board)):
			if r > 0:
				result_str += "\n"
			for c in range(len(self.board[r])):
				result_str += self.board[r][c] if self.board[r][c] else ' '
		return result_str

	def size(self):
		return (len(self.board), len(self.board[0]))

	def get(self, r, c):
		return self.board[r][c]

	def set(self, r, c, v):
		self.board[r][c] = v

class TicTacToeEnvironment(object):
	"""docstring for TicTacToeEnvironment"""
	def __init__(self):
		super(TicTacToeEnvironment, self).__init__()
		self.board = TicTacToeBoard()

	def draw_board(self):
		print("\n%s\n" % str(self.board))

	def game_over(self):
		nrows, ncols = self.board.size()
		# check rows
		for r in range(nrows):
			winner = self.board.get(r, 0)
			for c in range(ncols):
				if not self.board.get(r, c) or self.board.get(r, c) != winner:
					winner = None
					break
			if winner:
				return winner

		# check cols
		for c in range(ncols):
			winner = self.board.get(0, c)
			for r in range(nrows):
				if not self.board.get(r, c) or self.board.get(r, c) != winner:
					winner = None
					break
			if winner:
				return winner

		# check diagonals
		winner = self.board.get(0, 0)
		for r in range(nrows):
			if not self.board.get(r, r) or self.board.get(r, r) != winner:
				winner = None
				break
		if winner:
			return winner

		winner = self.board.get(0, 2)
		for r in range(nrows):
			if not self.board.get(r, 2-r) or self.board.get(r, 2-r) != winner:
				winner = None
				break
		if winner:
			return winner

		# check if there was a tie
		for r in range(nrows):
			for c in range(ncols):
				if not self.board.get(r, c):
					return None
		return "".join(set([self.board.get(0, c) for c in range(self.board.size()[1])]))

	def get_state(self):
		return copy.deepcopy(self.board)

	def record_move(self, r, c, marker):
		self.board.set(r, c, marker)
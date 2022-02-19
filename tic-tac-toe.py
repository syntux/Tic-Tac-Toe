class Board:
  def __init__(self):
    self.board = [str(i) for i in range(9)] 
    self.invalidMoves = [] # Keep track of all moves so far
    # All the ways to win
    self.winConds = [ 
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
        ]
    # Current turn, first turn is always X
    self.turn = 'X'

  # Print the board in a nice manner
  def printBoard(self):
    print("="*12) 
    for i in range(9):
      print(f" {self.board[i]} |", end="")
      if i % 3 == 2:
        print("\n", end="")
        print("="*12) # New line for next row

  # Check if the game is over by counting the player's
  # moves match the winning moves
  def gameOver(self, moves):
    for condition in self.winConds:
      count = 0
      for pos in condition:
        if pos in moves:
          count += 1
      if count == 3:
        print("\n\n GAME OVER")
        return True

    return False

  # Get the player's desired move and make sure
  # it is a valid move
  def playerMove(self, player):
    move = int(input("Enter a valid move: \n"))
    # Make sure it is a move that has not been done before
    # and that it is a number 0-8 inclusive (for the board)
    while (not (self.validMove(move)) and (move >= 0 and move <= 8)):
      move = int(input("Incorrect. Enter a valid move: \n"))
    # Update the move to the board and player
    self.board[move] = player.string
    player.moves.append(move)
    self.invalidMoves.append(move)
    # Change the turn
    if self.turn == 'X':
      self.turn = 'O'
    else:
      self.turn = 'X'

  # Make sure the move has not happened yet
  def validMove(self, move):
    if move in self.invalidMoves:
      return False
    else:
      return True

class Player:
  def __init__(self, first):
    self.turn = None 
    self.string = 'X' if first == 1 else 'O'
    self.moves = []

def main():
  newBoard = Board()
  newBoard.printBoard()
  player1 = Player(1)
  player2 = Player(2)

  isOver = False
  while (not (isOver)):
    if newBoard.turn == 'X':
      newBoard.playerMove(player1)
      isOver = newBoard.gameOver(player1.moves) 
    else:
      newBoard.playerMove(player2)
      isOver = newBoard.gameOver(player2.moves) 
  
    newBoard.printBoard()


if __name__ == '__main__':
    main()

class Board:
  def __init__(self):
    self.board = ['-' for i in range(9)] 

  def printBoard(self):
    print("="*12) 
    for i in range(9):
      print(f" {self.board[i]} |", end="")
      if i % 3 == 2:
        print("\n", end="")
        print("="*12) # New line for next row
def main():
  newBoard = Board()
  newBoard.printBoard()

if __name__ == '__main__':
    main()

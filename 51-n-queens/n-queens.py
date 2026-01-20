def checkplace(row , col , board ):
    for i in range(row-1 , -1 , -1):
        if(board[i][col] !='.'):
            return False

    dummy_row = row
    dummy_col = col
    while(dummy_row>=0 and dummy_col >=0):
        if(board[dummy_row][dummy_col] != '.'):
            return False

        dummy_row -=1
        dummy_col -=1

    dummy_row = row
    dummy_col = col
    while(dummy_row>=0 and dummy_col<len(board[0])):
        if (board[dummy_row][dummy_col] != '.'):
            return False


        dummy_col +=1
        dummy_row -=1

    return True



def NQueen(board , result   , row , no_of_queens):
    print(board)
    if(no_of_queens == 0 and board not in result ):
        result.append(board[:])
        return

    for col in range( len(board[row])):
        if( checkplace(row , col , board ) == True):
            row_list = list(board[row])
            row_list[col] = 'Q'
            board[row] = "".join(row_list)

            NQueen(board, result, row+1 ,  no_of_queens-1)


            row_list = list(board[row])
            row_list[col] = '.'
            board[row] = "".join(row_list)





class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result , board = [] ,[]
        for i in range(n):
            board.append('.'*n)


        row = 0
        NQueen(board , result  ,  row  , n )
        return (result)
                
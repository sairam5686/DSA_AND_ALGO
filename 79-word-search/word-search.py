def BoardSearch(board , word , current_row , current_col , visited , word_index):

    if(len(word) == word_index):
        return True
    if( current_row<0 or current_col<0 or current_col>=len(board[0]) or current_row>=len(board) or board[current_row][current_col] != word[word_index] or (current_row, current_col) in visited):
        return False



    visited.add((current_row ,  current_col))

    res =  (BoardSearch(board, word, current_row+1, current_col, visited, word_index+1)
            or BoardSearch(board, word, current_row-1, current_col, visited, word_index+1)
            or BoardSearch(board, word, current_row, current_col+1, visited, word_index+1)
            or BoardSearch(board, word, current_row, current_col-1, visited, word_index+1))
    visited.remove((current_row ,  current_col))

    return res

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(word[0] == board[row][col]):
                    res = BoardSearch(board ,word  , row , col  , set() , 0)
                    if(res == True):
                        return True
        return False
                    
                            
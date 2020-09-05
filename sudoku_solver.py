import unittest 


def solve(puzzle): 
    s=[1,2,3,4,5,6,7,8,9]   
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j]==0:
                row= [puzzle[i][k] for k in range(0,9)]
                col= [puzzle[k][j] for k in range(0,9)]
                sqr= [puzzle[3*(i//3)+k][3*(j//3)+l] for k in range(0,3) for l in range(0,3)]
                opt=set(s)-set(row)-set(col)-set(sqr)
                if len(opt)==0:    return 0
                if len(opt)>2:    continue 
                for num in opt:
                    puzzle[i][j]= num
                    #print(puzzle)
                    solve(puzzle)
                    if sum(puzzle[8])==45:
                        return puzzle
                else:
                    puzzle[i][j]= 0
                    return 0


problem = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]

solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1], [7, 1, 3, 4, 2, 6, 9, 8, 5], [8, 4, 5, 9, 7, 1, 3, 6, 2], [3, 6, 2, 8, 5, 7, 1, 4, 9], [4, 7, 1, 2, 6, 9, 5, 3, 8], [5, 9, 8, 3, 1, 4, 7, 2, 6], [6, 5, 7, 1, 3, 8, 2, 9, 4], [2, 8, 4, 7, 9, 5, 6, 1, 3], [1, 3, 9, 6, 4, 2, 8, 5, 7]]


class Test1(unittest.TestCase):

   def test_assert_equals(self):
       self.assertEqual(solve(problem), solution, "I felt a disturbance in the force")
       
      
if __name__ == '__main__': 
    unittest.main() 







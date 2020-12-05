import time

inicio = time.time()
def print_grid(arr):
	for i in range(16):
		if i in [4, 8, 12]:
			print("------------+-------------+-------------+-------------")
		for j in range(16):
			if(arr[i][j] <10):
				print(arr[i][j],end='  ')
			else:
				print(arr[i][j],end=' ')
			if j in [3, 7, 11]: print("|",end=' ')
			
		print()

def find_empty_location(arr, l):
	for row in range(16):
		for col in range(16):
			if(arr[row][col] == 0):
				l[0] = row
				l[1] = col
				return True
	return False


def used_in_row(arr, row, num):
	for i in range(16):
		if(arr[row][i] == num):
			return True
	return False


def used_in_col(arr, col, num):
	for i in range(16):
		if(arr[i][col] == num):
			return True
	return False


def used_in_box(arr, row, col, num):
	for i in range(4):
		for j in range(4):
			if(arr[i + row][j + col] == num):
				return True
	return False


def check_location_is_safe(arr, row, col, num):
	return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 4, col - col % 4, num)


def solve_sudoku(arr):
    l = [0, 0]
    if(not find_empty_location(arr, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 17):
        if(check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0		 
    return False

if __name__=="__main__": 
	 
	grid =[[0 for x in range(16)]for y in range(16)] 
	
	grid =[[1, 2, 0, 4, 5, 0, 7, 8, 0, 10, 11, 0, 13, 14, 0, 16],
		   [0, 6, 7, 0, 1, 2, 0, 4, 13, 0, 15, 16, 0, 10, 11, 12],
		   [9, 0, 11, 12, 0, 14, 15, 0, 1, 2, 0, 4, 5, 0, 7, 8],
		   [13, 14, 0, 16, 9, 0, 11, 12, 0, 6, 7, 0, 1, 2, 0, 4],
		   [0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 12, 11, 14, 13, 16, 15],
		   [6, 5, 8, 7, 2, 1, 0, 3, 0, 13, 0, 15, 0, 9, 0, 11],
		   [10, 0, 12, 0, 14, 0, 16, 0, 2, 0, 4, 3, 6, 5, 8, 7],
		   [14, 13, 0, 15, 0, 9, 0, 11, 0, 5, 0, 7, 2, 1, 4, 3],
		   [3, 0, 0, 2, 0, 0, 5, 6, 11, 0, 9, 10, 15, 16, 13, 14],
		   [7, 8, 5, 6, 3, 4, 1, 0, 0, 16, 0, 0, 11, 0, 9, 10],
		   [0, 0, 9, 0, 0, 16, 13, 0, 3, 4, 1, 2, 7, 8, 5, 6],
		   [15, 0, 13, 14, 0, 12, 9, 10, 0, 8, 0, 6, 0, 4, 1, 2],
		   [4, 3, 2, 1, 8, 0, 6, 0, 12, 0, 10, 9, 0, 0, 14, 13],
		   [8, 7, 6, 5, 4, 0, 2, 1, 0, 0, 14, 13, 0, 11, 0, 9],
		   [12, 11, 10, 9, 16, 15, 14, 0, 4, 0, 2, 0, 8, 0, 0, 5],
		   [16, 15, 0, 13, 12, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
	if(solve_sudoku(grid)): 
		print_grid(grid) 
	else: 
		print("Solução não existe!")
 
fim = time.time()
print("\nTempo: ",fim - inicio)

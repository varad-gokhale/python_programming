import sys

def generate_all_sorted_arrays(A,B):
	
	def helper(A,B,C,i,j,flag):
		if not flag:
			for idx in range(i,len(A)):
				if not C:
					C.append(A[idx])
				else:
					for num in A:
						if num > C[-1]:
							helper(A[1:],B,C + [num], i+1, j, 1)
		if flag:
			for idx in range(j, len(B)):
				for num in B:
					if num > C[-1]:
						print(C + [num])
						helper(A,B[1:],C+[num], i,j+1,0)
	
	A = [10,15,25]
	B = [5,20,30]
	helper(A,B,C,0,0,0)

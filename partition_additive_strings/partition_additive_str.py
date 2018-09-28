import sys

def partition_additive_str(s):
	output = []
	def helper(s, index, op1, op2, n):
		if index == len(s):
			return

		if n == 0:
			current_val = 0
			for i in range(index, len(s)):
				current_val = current_val*10 + int(s[i])
				print("{} {} {}\n".format(op1,op2,current_val))
				if current_val == op1 + op2:
					output.extend([str(op1),str(op2),str(current_val)])
			return	
		op = 0
		for i in range(index, len(s)):
			op = op * 10 + int(s[i])
			if(n == 2):
				helper(s, i+1, op, op2, n-1)
			elif n == 1:
				helper(s, i+1, op1, op, n-1)

	helper(s,0,0,0,2)
	return output

def main():
	print(partition_additive_str(sys.argv[1]))

if __name__ == "__main__":
	main()

import sys

def partition_additive_str(s):
	output = []
	def helper(s, index, op1, op2, n, flag):
		if index == len(s):
			return flag==1

		if n == 0:
			current_val = 0
			for i in range(index, len(s)):
				if current_val > op1 + op2:
					return False
				current_val = current_val*10 + int(s[i])
#				print("{} {} {}\n".format(op1,op2,current_val))
				if current_val == op1 + op2:
					if not flag:
						while output:
							output.pop()
						output.extend([str(op1),str(op2),str(current_val)])
					else:
						output.append(str(current_val))
					return helper(s,i+1, op2, current_val,n,1)
			return False	

		op = 0
		for i in range(index, len(s)):
			op = op * 10 + int(s[i])
			if(n == 2):
				ret = helper(s, i+1, op, op2, n-1,0)
			elif n == 1:
				ret = helper(s, i+1, op1, op, n-1,0)
			
			if ret:
				return True

	if helper(s,0,0,0,2,0):
		return output
	else:
		return []

def main():
	if len(sys.argv) <= 1:
		print("argument not provided. Exiting...")
	else:
		print(partition_additive_str(sys.argv[1]))

if __name__ == "__main__":
	main()


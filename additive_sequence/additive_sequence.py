def additive_sequence(s):


	def helper(s, i, op1, op2, n):
		if i == len(s):
			return False 
		if n == 2:
			current_sum = 0
			while i < len(s):
				current_sum = current_sum*10 + s[i]
				if current_sum == int(op1) + int(op2):
					return True
				i += 1
			return False
		op = 0	
		for i in range(i, len(s)):
			op = op*10 + int(s[i])
			
			if n == 0:
				ret = helper(s, i+1, op, op2, n+1)
			elif n == 1:
				ret = helper(s, i+1, op1, op, n+1)
			
			if ret is True:
				return True
			


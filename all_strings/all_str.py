def all_str(n_set, k):
	output = []
	def helper(n_set, rem, partial):
		if rem == 0:
			output.append(partial)
			return
		for ch in n_set:
			helper(n_set, rem-1, partial + ch)

	helper(n_set, k, "")
	return output

def main():
	print(all_str({'a','b'},3))
	print(all_str({'a','b','c'},3))
	print(all_str({},2))

if __name__ == '__main__':
	main()	

import sys

def string_combinations(s):

	str_set = set() 	
	def helper(s, index):	
		if index == len(s):
			return
		for i in range(index, len(s)):
			str_set.add(s[index:i+1])	
			helper(s, index+1)
	
	helper(s,0)
	return str_set

def main():
	print(string_combinations(sys.argv[1]))

if __name__== "__main__":
	main()

import sys

def string_combinations(s):
	
	def helper(s, index):	
		if index == len(s):
			return
		for i in range(index, len(s)):
			print(s[index:i+1] + " ")
			helper(s, index+1)
	
	helper(s,0)

def main():
	string_combinations(sys.argv[1])

if __name__== "__main__":
	main()

import sys

def substring_count(string):

	output = [0]
	def helper(string, index, s):
		if index == len(string):
			return
		for i in range(len(s)):
			if s[0] == s[i]:
				output[0] += 1
		helper(string, index + 1, s[1:])
	
	helper(string, 0, string)
	print("output is: " + str(output[0]))

def main():
	substring_count(sys.argv[1])

if __name__ == "__main__":
	main()


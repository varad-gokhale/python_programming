import sys

def count_consonants(s):
	result = [0]
	vowels = {'a', 'e', 'i', 'o', 'u'}

	def helper(s, index, s_orig):
		if index == len(s_orig):
			return
		helper(s[1:],index+1,s_orig)
		if(s[0].isalpha() and s[0].lower() not in vowels):
			result[0] += 1

	helper(s,0,s)
	return result[0]

def main():
	if len(sys.argv) == 1:
		return
	print(count_consonants(sys.argv[1]))

if __name__ == "__main__":
	main()

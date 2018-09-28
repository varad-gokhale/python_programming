import sys

def no_consec_1s(n):
	def helper(n, prev, s):
		if n == 0:
			print(s+" ")
			return
		
		helper(n-1, 0, s+'0')
		if prev != 1:
			helper(n-1, 1, s+'1')

	helper(n,2,"")

def main():
	no_consec_1s(int(sys.argv[1]))

if __name__ == "__main__":
	main()

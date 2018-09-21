import sys
def even_len_bin(n):
	if n == 0:
		return
	output = []
	def helper(two_n, partial_num, count):
		if count == two_n:
			if sum(int(x) for x in partial_num[:two_n/2]) == sum(int(y) for y in partial_num[two_n/2:]):
				output.append(partial_num)
			return

		helper(two_n, partial_num + "0", count+1)
		helper(two_n, partial_num + "1", count+1)

	helper(2*n, "", 0)
	return output

def main():
	if len(sys.argv) <= 1 or int(sys.argv[1]) < 0:
		print("Did not enter valid number. ByeBye!")
		return

	print(even_len_bin(int(sys.argv[1])))

if __name__ == "__main__":
	main()

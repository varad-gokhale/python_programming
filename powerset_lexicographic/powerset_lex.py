import sys

def powerset(s):
	s = "".join(sorted(s))
	def helper(al, s, n):
		if n == 1:
			return [al]
		ret = helper(s[0], s[1:], n-1)
		temp = [al]
		for el in ret:
			temp.append(al+el)
		return temp + ret
	print(helper(s[0], s[1:], len(s)))

def main():
	if(len(sys.argv) == 1 or sys.argv[1] == ""):
		print("No argument provided..Exiting...")
	else:
		powerset(sys.argv[1])

if __name__ == "__main__":
	main()

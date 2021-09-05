def create_triangle(n):
	for i in range(1, n+1):
		spacer = ''.join(" " for i in range((n-i)+1))
		dots = ''.join("* " for i in range(i))
		print(f"{spacer}{dots}")


if __name__ == '__main__':
	row = int(input("Input the number of the row: "))
	create_triangle(row)
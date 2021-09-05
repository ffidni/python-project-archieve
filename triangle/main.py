def create_triangle(n):
	for i in range(1, n+1):
		spacer, dot = " "*((n-i)+1), "* "*i
		print("{}{}".format(spacer, dot))

if __name__ == '__main__':
	number = int(input("Input a number for the row: "))
	create_triangle(number)


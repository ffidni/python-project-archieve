import os

def rename(p1, p2):
	path1 = os.walk(p1)
	path2 = os.walk(p2)
	for i, j in zip(path1, path2):
		dir1 = i[0]
		for file1, file2 in zip(i[2], j[2]):
			try:
				os.rename(f"{dir1}/{file1}", f"{dir1}/{file2}")
			except Exception as err:
				print(err)

def check_length(p1, p2):
	l1, l2 = [], []
	path1, path2 = os.walk(p1), os.walk(p2)
	l1 = list(path1)[0][2]
	l2 = list(path2)[0][2]

	return len(l1) == len(l2)

def main():
	p1 = input("Input path of the folder you want to modify: ")
	p2 = input("Input path of the folder you want to copy the name: ")
	is_same = check_length(p1, p2)
	if is_same:
		rename(p1, p2)
		print("Changed succesfully!")
	else:
		print("Error, the length of folders its not the same.")
		main()

if __name__ == '__main__':
	main()


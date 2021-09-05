def count_boomerang(lst):
	count = 0
	turns = 0
	for item in lst:
		if turns == len(lst)-2:
			break
		if is_boomerang(lst[turns:turns+3]):
			count += 1
		turns += 1

	return count

def is_boomerang(lst):
	if len(lst) == 3:
		if lst[0] == lst[2] and lst[1] != lst[0] and lst[1] != lst[2]:
			return True
	return False

if __name__ == '__main__':
	lst = list(map(int, input("Input numbers sep by spaces: ").split()))
	count = count_boomerang(lst)
	print(f"There {'are' if count > 1 else 'is'} {count} {'boomerangs' if count > 1 else 'boomerang'} in {lst}")

	
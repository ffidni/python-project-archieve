def repeat_letter(word, n=2):
	return ''.join(char*n for char in word)

def main():
	word = input("Input a word: ")
	n = int(input("How many times which each character is gonna be repeated?: "))
	print(repeat_letter(word, n))

if __name__ == '__main__':
        main()

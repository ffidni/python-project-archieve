def duplicate_count(text):
	return len([char for char in set(text) if text.lower().count(char)])

def show_result(text, result):
	return f"There {'are' if result > 1 else 'is'} {result} {'duplicates' if result > 1 else 'duplicate'} on the word {text}"

if __name__ == '__main__':
	text = input("Input a text: ")
	result = duplicate_count(text)
	print(show_result(text, result))
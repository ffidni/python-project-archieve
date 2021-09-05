def count_syllabel(word):
	VOWELS = "AEIOUYaeiouy"
	vowel_count = 0
	result = 0
	for index, letter in enumerate(word):
		if letter in VOWELS:
			if letter.lower() == 'e' and index == len(word)-1:
				if word[-2].lower() == 'l':
					result += 1
			elif letter.lower() == 'y' and vowel_count:
				vowel_count = 0
			else:
				if not vowel_count:
					result += 1
					vowel_count += 1
		else:
			vowel_count = 0

	return result



if __name__ == '__main__':
	for i in range(1, 12):
		word = input(f"Word {i}: ")
		count = count_syllabel(word)
		print(f"There are {count} {'syllables' if count > 1 else 'syllable'} in {word}.")
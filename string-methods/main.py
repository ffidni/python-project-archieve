from time import perf_counter as timer

class str(str):
	ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	NUMBER= "123456789"

	def __init__(self, value):
		super().__init__()
		self.value = value

	def __getitem__(self, index):
		if isinstance(index, int):
			return str(self.value[index])
		else:
			raise TypeError("string indices must be interger")

	def split(self, value=" "):
		result = []
		founded = False
		for char in self.value:
			if char != value:
				if result and not founded:
					result[-1] += char
				else:
					founded = False
					result.append(char)
			else:
				founded = True
		return result

	def upper(self):
		return ''.join(chr(ord(char)-32) if char.islower() else char for char in self.value)

	def lower(self):
		return ''.join(chr(ord(char)+32) if str(char).isupper() else char for char in self.value)

	def isupper(self):
		return all((False if chr(ord(char)-32).isalpha() else True) for char in self.value if char.isalpha())

	def islower(self):
		return all((False if chr(ord(char)+32).isalpha() else True) for char in self.value if char.isalpha())

	def isalpha(self):
		return all(char in self.ALPHABET for char in self.value)

	def isalnum(self):
		return all(char in self.ALPHABET or char in self.NUMBER for char in self.value)

	def replace(self, old, new):
		chars = list(self.value)
		chars[self.value.find(old)] = new
		return ''.join(chars)

	def find(self, value):
		indices = {char:index for index, char in enumerate(self.value)}
		return indices[value]

	def index(self, value):
		return self.find(value)

	def startswith(self, char):
		return self.value[0] == char

	def isnumeric(self):
		return all(char in self.NUMBER for char in self.value)

	def isdigit(self):
		return self.isnumeric()

	def strip(self, value=" "):
		char = list(self.value)
		for i in (0, -1):
			if char[i] == value:
				del char[i]
		return ''.join(char)

	def swapcase(self):
		return ''.join(char.lower() if char.isupper() else char.upper() for char in self.value)

	def title(self):
		result = []
		for chars in self.value.split():
			for index, char in enumerate(chars):
				if not index:
					result.append(char.upper())
				else:
					result.append(char.lower())
			result.append(" ")

		return ''.join(result)

	def istitle(self):
		return all(char.isupper() for chars in self.value.split() for index, char in enumerate(chars) if not index)

	def capitalize(self):
		return ''.join(char.upper() if not index else char.lower() for index, char in enumerate(self.value))

	def translate(self, values):
		result = self.value
		for old in values:
			new, old = values[old], chr(old)
			if not new:
				new = ""
			else:
				new = chr(new)

			result = result.replace(old, new)

		return result

	def maketrans(self, old, new, delete=None):
		result = {}
		if len(old) == len(new):
			for c_old, c_new in zip(old, new):
				result[ord(c_old)] = ord(c_new)

			if delete:
				for char in delete:
					result[ord(char)] = None
		else:
			raise ValueError("the first two maketrans argument must have equal length")

		return result

if __name__ == '__main__':
	pass


	


	
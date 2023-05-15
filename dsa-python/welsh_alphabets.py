"""
Given a special alphabet (alien dictionary?) sort a list of words in ascedning order alphabetically:  (INPUTS STRINGS WITHOUT SPACE)

alphabet: "a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"

Input: ["ddr",  "nah", "dea", "dd", "ngah"]

Output: "dea", "dd", "ddr", "ngah", "nah"

"""

welsh_alphabet = {"a": 1, "b": 2, "c": 3, "ch": 4, "d": 5, "dd": 6, "e": 7, "f": 8, "ff": 9, "g": 10, "ng": 11, "h": 12, "i": 13, "l": 14,
                  "ll": 15, "m": 16, "n": 17, "o": 18, "p": 19, "ph": 20, "r": 21, "rh": 22, "s": 23, "t": 24, "th": 25, "u": 26, "w": 27, "y": 28}


# USING CLASS AND METHOD

class Welsh:
    def __init__(self) -> None:
        self.alphabets = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i",
                          "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]
        self.store = {char: idx for idx, char in enumerate(alphabet)}

    def welshSort(self, words):
        def compare(word):
            temp = []
            i = 0

            while i < len(word)-1:
                if word[i:i+2] in self.store:
                    temp.append(self.store[word[i:i+2]])
                    i += 2
                else:
                    temp.append(self.store[word[i]])
                    i += 1
            temp.append(self.store[word[-1]])
            return temp
        words = sorted(words, key=compare)
        return [word.replace(" ", "") for word in words]


alphabet = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i",
            "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

input = ["ddr",  "nah", "dea", "dd", "ngah"]

obj = Welsh()
print(obj.welshSort(input))

# ==========================================================================================================================================

# FUNCTIONS ONLY


def sort_welsh(words):
    words = sorted(words, key=compare)
    return words


def compare(word):
    temp = []
    i = 0
    while i < len(word)-1:
        if word[i:i+2] in welsh_alphabet:
            temp.append(welsh_alphabet[word[i:i+2]])
            i += 2
        else:
            temp.append(welsh_alphabet[word[i]])
            i += 1
    if i == len(word) - 1:
        temp.append(welsh_alphabet[word[len(word)-1]])
    return temp


input = ["ddr",  "nah", "dea", "dd", "ngah"]
print(sort_welsh(input))

# ==========================================================================================================================================

"""
Given a special alphabet (alien dictionary?) sort a list of words in ascedning order alphabetically:  (SPACED INPUT STRINGS)

alphabet: "a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"

Input: ["dd r",  "n a h", "d e a", "dd", "ng a h"] 

Output: "dea", "dd", "ddr", "ngah", "nah"

"""


# WELSH WITH SPACED INPUT
welsh_alphabet = {"a": 1, "b": 2, "c": 3, "ch": 4, "d": 5, "dd": 6, "e": 7, "f": 8, "ff": 9, "g": 10, "ng": 11, "h": 12, "i": 13, "l": 14,
                  "ll": 15, "m": 16, "n": 17, "o": 18, "p": 19, "ph": 20, "r": 21, "rh": 22, "s": 23, "t": 24, "th": 25, "u": 26, "w": 27, "y": 28}


def sort_welsh(words):
    words = sorted(words, key=compare)
    return [word.replace(" ", "") for word in words]


def compare(word):
    word = word.replace(" ", "")

    temp = []
    i = 0
    while i < len(word)-1:
        if word[i:i+2] in welsh_alphabet:
            temp.append(welsh_alphabet[word[i:i+2]])
            i += 2
        else:
            temp.append(welsh_alphabet[word[i]])
            i += 1
    temp.append(welsh_alphabet[word[len(word)-1]])
    return temp


input = ["dd r",  "n a h", "d e a", "dd", "ng a h"]
print(sort_welsh(input))

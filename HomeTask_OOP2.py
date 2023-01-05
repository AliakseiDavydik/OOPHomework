import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__("Eng", string.ascii_lowercase)

    def is_en_letter(self, letter):
        if letter.lower() in string.ascii_lowercase:
            print("It is a letter of english alphabet!!!")
        else:
            print("Doesn't belong to the english alphabet!!!")

    def letters_num(self):
        print(EngAlphabet.__letters_num)

    @staticmethod
    def example():
        print("For example: It is a nice day today, isn't it?")


eng_l = EngAlphabet()
eng_l.print()
eng_l.letters_num()
eng_l.is_en_letter("F")
eng_l.is_en_letter("Щ")
eng_l.example()

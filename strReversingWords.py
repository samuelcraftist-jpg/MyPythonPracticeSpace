class Reverse:
    def rev(self, text):
        words = text.split()

        words.reverse()

        return " ".join(words)

obj = Reverse()
sentence = input("Enter a sentence: ")
result = obj.rev(sentence)

print("Reversed:", result)
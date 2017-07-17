sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(word_lengths)
    if number > 0:
        newlist.append(int(number))
print(newlist)

word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = []
for number in numbers:

newlist = [int(number) for number in numbers if number>0]
print(newlist)
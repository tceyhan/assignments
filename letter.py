string = "bugün baya canım sıkkın"
word_dict = {}

for n in string:
    if n in word_dict:
        word_dict[n] += 1
    else :
        word_dict[n] = 1
print(word_dict)
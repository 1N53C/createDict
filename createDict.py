import itertools

chars = "abcde12345"
n = 6

dict = open("dict.txt", "w")

for i in itertools.product(chars, repeat=n):
    dict.write(''.join(i) + '\n')

dict.close()

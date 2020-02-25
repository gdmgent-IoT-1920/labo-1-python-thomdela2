from collections import Counter

text_file = open('namen.txt', 'r')
text_read = text_file.read()
text_list = text_read.split()
text_names = Counter(text_list)

print(str(text_names))
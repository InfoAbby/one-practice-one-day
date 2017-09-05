file_name = 'movie.txt'

line_counts = 0
word_counts = 0
character_counts = 0

with open(file_name,'r') as f:
    for line in f:
        words = line.split()

        line_counts += 1
        word_counts += len(words)


print('line_counts ' , line_counts)
print('word_counts ' , word_counts)
import glob,os
dict = {}
most = -1
most_word = ''


def get_most_word(filename):
    global most,most_word,dict
    dict = {}
    most = -1
    most_word = ''
    with open(filename,'r') as f :
        for line in f:
            words = line.split()
            for word in words:
                if dict.get(word):
                    dict[word] += 1
                    if dict[word] >= most:
                        most=dict[word]
                        most_word = word
                else:
                    dict[word] = 1

def get_filename():
    for infile in glob.glob("*.txt"):
        file,ext = os.path.splitext(infile)
        filename = file+'.txt'
        yield filename

if __name__ == '__main__':
    for filename in get_filename():
        
        get_most_word(filename)
        print(filename,'中最重要的词是：',most_word)
        print('出现了',most,'次')
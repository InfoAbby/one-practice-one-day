import glob,os
import re




def count_code(filename):
    exp_re = re.compile(r'^#.*')
    with open(filename,'r',encoding='utf-8') as f:
        all_lines = 0
        space_lines = 0
        exp_lines = 0
        for line in f.readline():
            all_lines += 1
            if line.strip() == '':
                space_lines += 1
                continue
            exp = exp_re.findall(line.strip())
            if exp:
                exp_lines += 1
        print('%s\t%s\t%s\t%s' % (filename,all_lines,space_lines,exp_lines))

def get_filename():
    for infile in glob.glob("*.py"):
        file,ext = os.path.splitext(infile)
        filename = file + '.py'
        yield filename

if __name__ == '__main__':
    for filename in get_filename():
        count_code(filename)



import glob
files = glob.glob('*.md')
lines = [line.strip() for file in files for line in open(file, 'rt')]
with open('singlefile.txt', 'wt') as fout:
    for line in lines: fout.write(line + '\n')
pass

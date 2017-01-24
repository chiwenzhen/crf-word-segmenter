# coding=utf-8

"""
测试CRF++训练的模型
"""
import codecs
import sys
import CRFPP


if len(sys.argv) != 4:
    print "Usage: python run_test.py crf_model in_file out_file"
    sys.exit()
crf_model = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]
tagger = CRFPP.Tagger("-m " + crf_model)

with codecs.open(in_file, 'r', 'utf-8') as input, codecs.open(out_file, 'w', 'utf-8') as output:
    for line in input.readlines():
        tagger.clear()
        for word in line.strip():
            word = word.strip()
            if word:
                tagger.add((word + "\to\tB").encode('utf-8'))
        tagger.parse()
        size = tagger.size()
        xsize = tagger.xsize()
        for i in range(0, size):
            for j in range(0, xsize):
                char = tagger.x(i, j).decode('utf-8')
                tag = tagger.y2(i)
                if tag == 'B':
                    output.write(' ' + char)
                elif tag == 'M':
                    output.write(char)
                elif tag == 'E':
                    output.write(char + ' ')
                else:  # tag == 'S'
                    output.write(' ' + char + ' ')
        output.write('\n')

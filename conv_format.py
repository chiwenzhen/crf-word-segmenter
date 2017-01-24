# coding=utf-8

"""
将文本转换成CRF++要求的格式
"""
import sys
import codecs


if len(sys.argv) != 3:
    print "Usage: python conv_format.py inputfile outputfile"
    sys.exit()
in_file = sys.argv[1]
out_file = sys.argv[2]

# 将分词后的文件转换成四种标记的文件：B(Begin), E(End), M(Middle), S(Single)
with codecs.open(in_file, 'r', 'utf-8') as input, codecs.open(out_file, 'w', 'utf-8') as output:
    for line in input.readlines():
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output.write(word + "\tS\n")
            else:
                output.write(word[0] + "\tB\n")
                for w in word[1:-1]:
                    output.write(w + "\tM\n")
                output.write(word[-1] + "\tE\n")
        output.write("\n")

import codecs

f = codecs.open('foo.txt', 'rU')
for line in f:
    f.write(line)

f.close()

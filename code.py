import codecs
#f2 = open("dataset-eng-hindi","w")

with codecs.open('english-hindi transliteration', encoding='utf-8') as f1:
    line = f1.readlines()
with codecs.open('dataset-eng-hindi', 'w', encoding='utf-8') as f2:
    i = 1
    for l in line:
        i = i+1
        for char in l:
            if char != '\n':
                f2.write(char + " ")
            #f2.write(unicode(char + " ", "utf-8"))
            print char,
        f2.write("\n")
        #print '\n'

    print 'total line = ' + str(i)


with codecs.open('github wala eng-hindi dataset', encoding='utf-8') as f1:
    line = f1.readlines()
with codecs.open('dataset-eng-hindi', 'a', encoding='utf-8') as f2:
    j = 1
    for l in line:
        i = i+1
        for char in l:
            if char != '\n':
                f2.write(char + " ")
            #f2.write(unicode(char + " ", "utf-8"))
            print char,
        f2.write("\n")
        #print '\n'

    print 'total line = ' + str(i+j)



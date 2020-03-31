import pinyin

f = open("cj5-20902.txt", "r")
outfile = open("out.txt", "w")
outfile.write("{")
while f:
    line = f.readline().strip()
    if len(line) < 1:
        break
    ch = line[-1]
    print(ch, end="=>")
    p = pinyin.get(ch)
    print(p)
    outfile.write(ch + ": '" + pinyin.get(ch) +  "', \n")
outfile.write("}")
outfile.close()
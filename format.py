f = open(r"\TestSetFrames\Labels\MultiActionLabels\3840x2160\1.2.10.txt")

def writeLine(line):
    str = line.split()
    if (str[6] == "0"):
        width = int(str[3])-int(str[1])
        height = int(str[4])-int(str[2])
        center_x = width/2.0+int(str[1])
        center_y = height/2.0+int(str[2])
        width /= 3840.0
        height /= 2160.0
        center_x /= 3840.0
        center_y /= 2160.0
        newLine = "0 "+repr(center_x)+" "+repr(center_y) + \
            " "+repr(width)+" "+repr(height)
        outputPath = "/1.2.10/" + \
            str[5]+".txt"
        w = open(outputPath, 'a', encoding="UTF-8")
        w.write(newLine)
        w.write("\n")
        w.close


nextline = f.readline()
while nextline:
    writeLine(nextline)
    nextline = f.readline()

f.close
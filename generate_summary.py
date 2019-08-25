import os

def generate(dir):
    filePath = os.path.join(dir, 'problems.txt')
    file = open(filePath, 'r')
    lines = file.readlines()

    idToName = {}

    for line in lines:
        problem = line.split(',')
        idToName[int(problem[0])] = (problem[1][1:], problem[2][1:-1])
    file.close()

    outFileName = 'SUMMARY.md'
    outfile = open(outFileName, 'w')
    outfile.write("# Summary\n\n")

    count = 0
    print idToName
    for id in idToName:
        problemFileName = os.path.join(dir, idToName[id][0] + '.md')
        if (os.path.exists(problemFileName)):
            entry = "* [{}.{}]({})\n".format(str(id), idToName[id][1], problemFileName)
            outfile.write(entry)
            count += 1
    outfile.close()

generate('./leetcode')

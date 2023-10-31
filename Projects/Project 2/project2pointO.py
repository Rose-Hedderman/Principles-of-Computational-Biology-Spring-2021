# Rose Hedderman
# EID: rrh2298

# os is imported to be able to access files
import os

# doBWT carries out the Burrows Wheeler Transform algorithm
def doBWT(i):
    doB = []
    # add $ to beginning & add ^ to end
    i = "$" + i + "^"
    # roate string 8 times
    temp = []

    for n in range(len(i)):

        temp.append(i)
        end = i[-1]
        beg = i[:-1]
        i = end + beg

        # sort into lexical order
    temp.sort()
        # take the character in the last column
    fin = ""
    for j in temp:
        fin += j[-1]

    return fin

# this function counts the number of consecutive similar letters
def countLetters(w):
    # takes in a string called "w" for word
    finW= ""
    count = 1
    last = ""
    for i in range(len(w)):
        if i != len(w)-1:
            if w[i] == w[i+1]:
                count += 1
            else:
                finW += str(count)+ w[i]
                count = 1
        last = w[i]
    finW += str(count)+ last
    return finW

# doIBWT runs the algorithm for the inverse Burrows Wheeler Transform
def doIBWT(i):
    doiB = []

        # do the inverse burrows wheeler transform
        # make a square matrix
    mat = [[0 for c in range(len(i))] for r in range(len(i))]

        # fill in the square matrix
    for z in range(len(i)):

        for b in range(z,0, -1):
            for a in range(len(i)):
                mat[a][b] = mat[a][b-1]
        for x in range(len(i)):
            mat[x][0] = i[x]
        # sort into lexical order
        mat.sort()

    # take the last column
    f = ""
    for el in mat[0]:
        f += el
    f = f.replace("$","")
    f = f.replace("^","")

    return f

# makeDict is where the files are read into a dictionary
def makeDict():
    p2Dict = {}
    direct = input("Please enter the path to the files from 'WORK' to the folder the file is in: ")
    #direct = '.'
    for i in os.listdir(direct):
        #for i in os.listdir(direct):
        if i == "bwt.txt" or i == "ibwt.txt":
            f = open(i, "r")
            #f = open(direct + i,"r")
            lineC = 0
            for lines in f:
                lineC += 1
                if lines[0]!= "#":
                    lines = lines.rstrip("\n")
                    #if ("line"+str(lineC)) in p2Dict:
                    if lines[0] == "^" and ("line"+str(lineC)) in p2Dict:
                        p2Dict["line"+str(lineC)].append(lines)
                        #print(p2Dict)
                    elif lines[0] != "^":
                        p2Dict["line"+str(lineC)] = [lines]
                        #print(p2Dict)
                    else:
                        p2Dict["line"+str(lineC)] = ["",lines]
    return p2Dict

    '''    
    #for file in temp:
        if file == "bwt.txt":
            b = open(file, "r")
            lineCb = 0
            for lb in b:
                lineCb = lineCb + 1
                if lb[0]!= "#":
                    lb = lb.rstrip("\n")
                    if ("line"+str(lineCb)) in p2Dict:
                        p2Dict["line"+str(lineCb)].append(lb)
                    else:
                        p2Dict["line"+str(lineCb)] = [lb]
            print(p2Dict)
                        
        if file == "ibwt.txt":
            ib = open(file, "r")
            print(ib)'''

        
# actually is where all the functions defined above are called
def actually(d):
    masterList = []
    for x in range(1,len(d)+1):
        it = d['line'+str(x)]
        if it[0] != "":
            masterList.append(doBWT(it[0]))
            masterList.append(countLetters(it[0]))
        masterList.append(countLetters(it[1]))
        masterList.append(doIBWT(it[1]))
    return masterList

# print the master list of all the answers
def printList(l):
    for i in l:
        print(i)

# run all the main functions
def main():
    dictionary = makeDict()
    runDict = actually(dictionary)
    printList(runDict)

main()

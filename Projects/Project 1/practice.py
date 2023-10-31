# This is a python file to perfect the functions before putting them
# in the official file in TACC.
# Rose Hedderman
# EID: rrh2298

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
    doB.append(fin)
    #print(doB)
    return doB

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
            
        mat.sort()
        
    f = ""
    for el in mat[0]:
        f += el
    f = f.replace("$","")
    f = f.replace("^","")
    doiB.append(f)
          
    return doiB

def countLetters(w):
    # takes in a string called "w" for word
    finW= ""
    count = 1
    if len(w) >1 :
        for j in range(1,len(w)):
            if w[j-1] == w[j]:
                count += 1
            else:
                finW += (str(count)+w[j-1])
                count = 1
        finW += (str(count) + w[j])
    else:
        finW += str(count) + w[0]
    return finW

def printList(l):
    for i in l:
        print(i)

def main():
    pract = {'line1':['TTTTTT','^GCGGTATGGATCCAGATAAATAAAC$GGTTTTGGGGGTAACATGGGTGCCGTCCACA'],'line2':['TGGTTAACCATGTAACCTGTTGTGTAATTTTGGGTTTAACCTTGTA','^TATTTTAATAAATCACAACCTTTTTGTTTT$TTTGGTTTCGTTCTGTGAGGCATGAC']}

    masterList = []
    for x in range(1,len(pract)):
        it = pract['line'+str(x)]
        masterList.append(doBWT(it[0]))
        masterList.append(countLetters(it[0]))
        masterList.append(countLetters(it[1]))
        masterList.append(doIBWT(it[1]))
    print(masterList)
        
    
main()

# Rose Hedderman
# EID: rrh2298

# Function definitions
# Note that the function below are incomplete.
# Where appropriate you will need to fill out the
# body of the function, the arguments/parameters as well as the
# return value (if required).

def inputFunc():
    value = input("Please enter a string of DNA sequences:")
    print("The input string was:", value)
    return str(value)

def countFunc(dna):
    
    # count number of As
    countA = dna.count("A")
    # count number of Gs
    countG = dna.count("G")
    # count number of Cs
    countC = dna.count("C")
    # count number of Ts
    countT = dna.count("T")

    # determine if there are any characters that are not A, C, T, or G
    # This is kind of an inefficient way to do this, but nothing else would work.
    safe = True
    for i in dna:
        if (i == "A") or (i == "G") or (i == "C") or (i == "T"):
            safe = True
        else:
            safe = False
            break

    # count the largest substring with repeating characters
    countConsec = 0
    if dna != None:
        current = dna[0]
        for x in range(len(dna)):
            curCount = 1
            for y in range(x+1, len(dna)):
                if dna[x] != dna[y]:
                    break
                curCount += 1
            if curCount > countConsec:
                # countConsec is the number of occurences
                countConsec = curCount
                # current is the character that's being repeated
                current = dna[x]
                
    # remake the longest substring
    longest = countConsec*current
    # count the number of CG occurences
    countCG = dna.count("CG")
    
    # return results as a tuple
    return (countA, countC, countG, countT, safe, longest, countCG)

def printFunc(t):
    # The inputed string was printed when the input was made.
    if t[4] == False:
        print("Error: Your input string contained inadmissible characters. Please rerun the program inputting only strings that contain the characters A, C, G or T.")
    else:
        print("The number of As in the string were:", t[0])
        print("The number of Cs in the string were:", t[1])
        print("The number of Gs in the string were:", t[2])
        print("The number of Ts in the string were:", t[3])
        print("The largest substring with repeating characters was", t[5], "and was of length ",len(t[5]))
        print("The number of occurrences of CG in the string was:", t[6])
    return
  
# You can also define other functions to help you perform
# calculations but at a minimum your program
# should have the 3 functions defined above.

# Call the functions below in order of the parts of the
# assignment, and get it to print out the "
# desired output.

x = inputFunc()
y = countFunc(x)
printFunc(y)

install.packages("seqinr")
install.packages("ape")

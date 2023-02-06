import decimal


inches = float(input("inches: "))
unit = input("unit: ")
mmToInches = 25.4
cmToInches = 2.54
mToInches = 0.0254
numberOfInches = inches

def convertInchestoMM(numberOfInches, mm):
    return numberOfInches * mm

def convertInchestoCM(numberOfInches, cm):
    return numberOfInches * cm

def convertInchestoM(numberOfInches, m):
    return numberOfInches * m


def test(numberOfInches):
    if(unit == "-mm"):
        print(convertInchestoMM(numberOfInches, mmToInches))

    elif(unit == "-m"):     
        print(convertInchestoM(numberOfInches, mToInches))

    elif(unit == "-cm"):
        print(convertInchestoCM(numberOfInches, cmToInches))
        
    else:
        print("Error: ukjent enhet")


print(test(numberOfInches))

#måten formen det skal være på er
#output = funksjon() 
#expected output = KONKRET VERDI
#if output = expected output
#   print ('rett')
#else
#   print ("feil")

successmsg = ('Grønn: Suksess det funker fint')
errormsg = ('Rød: Det funker ikkje prøv igjen')


if convertInchestoCM(1, mmToInches) == cmToInches:
    print(successmsg)
else:
    print(errormsg)

if convertInchestoM(1, mmToInches) == mToInches:
    print(successmsg)
else:
    print(errormsg)

if convertInchestoMM(1, mmToInches) == mmToInches:
    print(successmsg)
else:
    print(errormsg)
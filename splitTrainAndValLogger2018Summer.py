#python 2, I've not gotten around to making a py3 version

import sys

#HARDCODE these 3 lines:
trainMin = 0
valMin = 0
percentTrain = (2.0/3) #I'd actually suggest about 3/4, REMEMBER .0 to declare this a double

startTrainMin = trainMin
startValMin = valMin
extra = 0 #round up or down
rounds = []

def printRounds():
    print "Started with " + str(startTrainMin) + " files in Train and " + str(startValMin) + " files in Val\n"
    for i in range(len(rounds)):
        print "Round: " + str(i),
        print "   Train added: " + str(rounds[i][0]),
        k = startTrainMin
        for j in range(i):
            k += rounds[j][0]
        print " Train now had total: " + str(int(rounds[i][0])+k),
        print "   Val added: " + str(rounds[i][1]),
        k = startValMin
        for j in range(i):
            k += rounds[j][0]
        print " Val now had total: " + str(int(rounds[i][1])+k)
        print "\n\n"
    print "editing current deposits still not available, wait until next program update\n"

while True:
    usrInput = raw_input("Add how many files? (or p to print total stocks or q to quit)")
    if usrInput[:1].lower() == 'p':
        print "printing total stocks...\n"
        printRounds()
        pass
    elif usrInput[:1].lower() == 'q':
        print "You quit :( :( :("
        sys.exit()
    else:
        try:
            numNewFiles = int(usrInput)
        except:
            print "You did not type a valid answer."
            continue

        if numNewFiles%3 != 0:
            extra = 1

        rounds.append([int(numNewFiles*percentTrain)+extra,int(numNewFiles*(1-percentTrain))])
                                      
        print "\nTrain add: "+ str(rounds[len(rounds)-1][0])
        print "Val add: "+str(rounds[len(rounds)-1][1])

        print "\nTrain has: "+str(rounds[len(rounds)-1][0]+int(trainMin))+" total files"
        print "Val has: "+str(rounds[len(rounds)-1][1]+int(valMin))+" total files\n"

        trainMin = (numNewFiles*percentTrain)+trainMin
        valMin = (numNewFiles*(1-percentTrain))+valMin

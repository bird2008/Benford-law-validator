#Import library
import numbers
import re
import pickle
import matplotlib.pyplot as plt
import random


#Input file and open
with open("data.txt", "r", encoding="utf-8") as text:
    text_contents = text.read()


#Definition
numbers = re.findall('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', text_contents)
firstDigits = []
cleanNumbers = []
resultPercentageNumber = 0
countNumber = 0
results = 0
allResults = []


#Create clean text function
def functionCleanNumbers(): 
    for cleanNumber in numbers:
        cleanNumbers.append(cleanNumber)

def functionRemoveDate(dateNumber):
    if len(dateNumber) == 10:
        if dateNumber[2] == "." and dateNumber[5] == ".":
            return False

    return True    

def functionRemoveYear(yearNumber):
    if len(yearNumber) == 4:
        if yearNumber[0] == '2' and yearNumber[1] == '0':
            return False
        if yearNumber[0] == '1' and yearNumber[1] == '9':
            return False

    return True  

def functionRemoveDot(dotNumber):
    if dotNumber[0] == "." or dotNumber[0] == "," or dotNumber[-1:] == ".":
        return False

    return True   

def functionRemoveZeroNumbers(zeroNumber):
    if zeroNumber[0] == "0":
        return False

    return True

def functionFirstDigits(): 
    for firstDigit in cleanNumbers:
        firstDigits.append(firstDigit[0])


#Create function percent of number of all
def functionPercentOfNumberOfAll(num):
    countNumber = firstDigits.count(str(num))
    resultPercentageNumber = percentOfOneDigit * countNumber
    allResults.append(round(resultPercentageNumber, 2))
    print(str(num) + ": " + str(round(resultPercentageNumber, 2)) + "% " + "(" + str(countNumber) + ")")


#Function call
functionCleanNumbers()

dateRemove = filter(functionRemoveDate, cleanNumbers)
cleanNumbers = list(dateRemove)

yearRemove = filter(functionRemoveYear, cleanNumbers)
cleanNumbers = list(yearRemove)

dotNumber = filter(functionRemoveDot, cleanNumbers)
cleanNumbers = list(dotNumber)

zeroNumber = filter(functionRemoveZeroNumbers, cleanNumbers)
cleanNumbers = list(zeroNumber)

functionFirstDigits()


#Percent of one digitas
digitsCount = len(firstDigits)
if digitsCount != 0:
    percentOfOneDigit =  100 / digitsCount
else:
    percentOfOneDigit = 0


#Results
print("Claened text: " + str(' '.join(cleanNumbers)))
print("Number of all digits: " + str(digitsCount))
print("Percent for one digits: " + str(round(float(percentOfOneDigit), 2)) + "%")
for number in range(1, 10):
    functionPercentOfNumberOfAll(number)


#Create diagram
with open("diagram.txt", "wb") as text:
    pickle.dump(allResults, text)

try:
    with open("diagram.txt", "rb") as text:
        result = pickle.load(text)
except:
    print("First run count percentage program")
    exit()

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
branford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

plt.plot(digits, branford)
plt.plot(digits, result)

plt.grid(True)
plt.title("First digits distribution")
plt.ylabel("Distribution")
plt.xlabel("Digits")
plt.legend(["Brandford's law values", "Program sesults"])

randomNumber = random.randint(1, 9999)

plt.savefig('diagram' + str(randomNumber) + '.png')
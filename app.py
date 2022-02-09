#Import library
import numbers
import re
import pickle
import matplotlib.pyplot as plt
import random

from matplotlib.pyplot import close


#Input file and open
with open("data.txt", "r") as text:
    text_contents = text.read()



#Definition
numbers = re.findall('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', text_contents)
firstDigits = []
cleanNumbers = []
resultPercentageNumber = 0
countNumber = 0
results = 0

#Create function First Digit
def functionCleanNumbers(): 
    for cleanNumber in numbers:
        cleanNumbers.append(cleanNumber)

def functionFirstDigits(): 
    for firstDigit in cleanNumbers:
        firstDigits.append(firstDigit[0])

def functionRemoveZeroNumbers():
    for zeroNumber in cleanNumbers:
        if zeroNumber[0] == "0":
            cleanNumbers.remove(zeroNumber)
    while '0' in cleanNumbers:
        cleanNumbers.remove('0')

def functionRemoveDate():
    for dateNumber in cleanNumbers:
        if len(dateNumber) == 10:
            if dateNumber[2] == "." and dateNumber[5] == ".":
                cleanNumbers.remove(dateNumber)

def functionRemoveDots():
    for dot in cleanNumbers:
        if dot[0] == "." or dot[-1:] == "." or dot[-1:] == ",":
            cleanNumbers.remove(dot)

def functionRemoveYear():
    while '2014' in cleanNumbers:
        cleanNumbers.remove('2014')
    while '2015' in cleanNumbers:
        cleanNumbers.remove('2015')
    while '2016' in cleanNumbers:
        cleanNumbers.remove('2016')
    while '2017' in cleanNumbers:
        cleanNumbers.remove('2017')
    while '2018' in cleanNumbers:
        cleanNumbers.remove('2018')
    while '2019' in cleanNumbers:
        cleanNumbers.remove('2019')
    while '2020' in cleanNumbers:
        cleanNumbers.remove('2020')
    while '2021' in cleanNumbers:
        cleanNumbers.remove('2021')
    while '2022' in cleanNumbers:
        cleanNumbers.remove('2022')
 
#Create Percent Of Number Of All
def functionPercentOfNumberOfAll(num):
    countNumber = firstDigits.count(str(num))
    resultPercentageNumber = percentOfOneDigit * countNumber
    print(str(num) + ": " + str(round(resultPercentageNumber, 2)) + "% " + "(" + str(countNumber) + ")")

#Function call
functionCleanNumbers()

functionRemoveDate()
functionRemoveDate()
functionRemoveDate()
functionRemoveDate()

functionRemoveDots()
functionRemoveDots()
functionRemoveDots()
functionRemoveDots()

functionRemoveYear()
functionRemoveYear()
functionRemoveYear()
functionRemoveYear()

functionRemoveZeroNumbers()
functionRemoveZeroNumbers()
functionRemoveZeroNumbers()
functionRemoveZeroNumbers()

functionFirstDigits()

functionRemoveDots()
functionRemoveDots()
functionRemoveDots()
functionRemoveDots()


#Percent of one digitas
digitsCount = len(firstDigits)
if digitsCount != 0:
    percentOfOneDigit =  100 / digitsCount
else:
    percentOfOneDigit = 0

#Create Percent Of Number Of All
def functionPercentOfNumberOfAll(num):
    countNumber = firstDigits.count(str(num))
    resultPercentageNumber = percentOfOneDigit * countNumber
    print(str(num) + ": " + str(round(resultPercentageNumber, 2)) + "% " + "(" + str(countNumber) + ")")

allResults = []

def functionPercentOfNumberOfAll(num):
    countNumber = firstDigits.count(str(num))
    resultPercentageNumber = percentOfOneDigit * countNumber
    allResults.append(round(resultPercentageNumber, 2))
    print(str(num) + ": " + str(round(resultPercentageNumber, 2)) + "% " + "(" + str(countNumber) + ")")

#Results
print("Claened text: " + str(len(cleanNumbers)) + ":  " + str(' '.join(cleanNumbers)))
#print(firstDigits)
print("Number of all digits: " + str(digitsCount))
print("Percent for one digits: " + str(round(float(percentOfOneDigit), 2)) + "%")
for number in range(1, 10):
    functionPercentOfNumberOfAll(number)
with open("diagram.txt", "wb") as text:
    pickle.dump(allResults, text)

#Create diagram
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

close("diagram.txt")
close("deta.txt")
roman ={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
def RTD(number):
    summ =0
    digit =1
    ls1=[]
    ls2=[]
    for i in number:
        ls1.append(i)
#     print(ls1)
    for i in ls1:
        ls2.append(i.upper())
#     print(ls2)
    last =ls2[-1]
    for i in range(0,len(ls2)) :
        if last in roman:
            last = ls2[-1]
            rtd = roman[last]
            summ =summ+rtd*digit
            digit=digit*10
            ls2.pop()
        else:
            ("sorry ! Roman number not valid! ")
            break
    print(summ)       
number =input("Enter The roman number : ")
RTD(number)



tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum
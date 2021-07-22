import pyparsing
from pyparsing import Word, alphas, nums, Char, oneOf, alphanums

greeting=input("Enter a string in the word, word! format. ")
abc=[i for i in "abcdefghijklmnopqrestuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ"]
numbers=[nums, None]
variable=[]
operations=[i for i in "*/+-"]
for i in operations:
    greetlst=greeting.split(str(i))
    greeting=""
    for i in greetlst:
        greeting += i
print(greeting)
#greet=oneOf(numbers) + Char(alphas) + oneOf(operations) + Char(alphanums) + Char(alphanums) + "=" + Char(alphanums)
while True:
    #try:
    #new_greeting=greet.parseString(greeting)
    #print(new_greeting)
    quit()
    #except pyparsing.ParseException:
    #    print("try again")    
    #    greeting=input("Enter a string in the word, word! format. ")
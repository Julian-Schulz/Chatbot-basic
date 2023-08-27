import random

name = input("What is your name" )

print("Hello " +  name)

question1 = input("How was your day?")

yes_functions = [lambda: 'Thats butifull', lambda: 'That sounds great!']
no_funktions = [lambda: 'I am sorry to hear that', lambda: 'Can I help?']

question2 = input("Why?")
question1.lower()
if question2 == 'fun':
        yes = random.choice(yes_functions)
        print(yes())
        pass
if question2 == 'no':
    no == random.choice(no_funktion)
print(no())
pass

question2 = ("Why?")

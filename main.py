import random

name=input("What is your name? \n")
print("\nHello "+ name)

dayinfo=input("How was your day?\n")

goodday_funktion=("Thats goood to hear","I am happy to hear that")
badday_funktion=("Thats not so good, how can I help","I am sorry to hear that")

if dayinfo == "good":
    print(random.choice(goodday_funktion))

elif dayinfo == "bad":
        print(random.choice(badday_funktion))

highlite=input("What was your Highlite?\n")
highliteanswer=input("Why was that your Highlite?\n")
print("relatble!")

downlite=input("What was your Downlite??\n")

if downlite == "there was none" :
    print("great to hear")

else:
    print("ahh I see why!")

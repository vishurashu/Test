#Problem Statement: You have to write a Word Puzzle Game in which the user has to form
#the correct word out of a given set of characters. In the game the user has to solve this
#puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
#in random sequence. Give the user score +1 for each correct answer and give -1 for each
#wrong answer. At last print the final score. You can store any number of words in the list, but
#in each round of the game only 5 words are shown to the user.


name=input("enter you name   ")
print("good luck =",name)
#word_list=["raehtf","kabre","cyrotnu","reneg","oaerelanp"]
x=int(word=input("enter your words"))

for e in x:
    b=e.sorting()
    print(b)
print()       


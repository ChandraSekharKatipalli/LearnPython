#Functions
def tea():
    print("Boil some water")
    print("add sugur & tea leaves")
    print("add some milk")
    print("heat it for few mins")
    print()

tea()

for i in range(5):
    tea()


#Arguments / Parameters
def sheldon_knock(person):
    print("knock knock knock", person)

sheldon_knock("penny")
sheldon_knock("leonard")

#famous dialogues
def speak(charactor, dialogue):
    print("character =", charactor)
    print("Dialogue =", dialogue)

speak("joey")# gives error 
speak("joey", "how you doing?")
speak("joey", "how you doing?", 'chandler')#gives error




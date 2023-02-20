import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 250)
engine.setProperty('volume', 1)
input_val1 = int(input("Enter 1st number: "))
input_val2 = int(input("Enter 2nd number: "))
answer = input("Is %s bigger than %s ? (yes / no) \n" % (input_val1, input_val2))
if answer.lower() == "yes" and input_val1 > input_val2:
    engine.say(''' Hey, how are you so freaking smart? You should apply for Harvard university!''')
elif answer.lower() == "no" and input_val1 < input_val2:
    engine.say(''' Hey, how are you so freaking smart? You should apply for Harvard university!''')
else:
    engine.say(''' Uh, you should be ashamed. You are brainless monkey! Go study mathematics!''')
engine.runAndWait()

from pymarkovchain import MarkovChain
import time
import pyttsx


# setup voice
rate = 30
engine = pyttsx.init()
engine.setProperty('rate', rate)

voices = engine.getProperty('voices')

# Setup Markov database
mc = MarkovChain("/Markov-databases")
input = open("input_text.txt").read().replace("\n"," ")
mc.generateDatabase(input)


# Generate strings
for i in range(100):
  string = mc.generateString() + "."
  while len(string) < 120:
    string = mc.generateString() + "."
  print string
  with open("generated_strings.txt",'a+') as f:
    f.write(string + '\n')
  engine.say(string)
  time.sleep(2)
  engine.setProperty('rate', rate)
  rate += 1
  engine.runAndWait()
  i += 1


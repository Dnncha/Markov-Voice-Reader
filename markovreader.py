from pymarkovchain import MarkovChain
import time
import pyttsx
from textstat.textstat import textstat


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
  print "Readability Score: %s" % textstat.dale_chall_readability_score(string)
  with open("generated_strings.txt",'a+') as f:
    f.write(string + '\n' +'\n')
  engine.say(string)
  time.sleep(1)
  engine.setProperty('rate', rate)
  rate += 1
  engine.runAndWait()
  i += 1


#Magic8Ball.py
#Name: Brennan Wood
#Date: 1/29/25
#Assignment: Lab 2 (Magic8Ball)

#We will need random for this program, import to use this package.
import random

# Title of project:

def main():
  print("\033[92mMagic8Ball\033[0m")
if __name__ == '__main__':
    main()

  #Prompt the user for their question.

questions = ("What's on your mind? ", "What can I help you with? ", "What's the big question today? ", "What knowledge do you seek? ")
length = len(questions)
q = random.random()*length
q = int(q)
question = questions[q]
userinput = input(question)

 # answers that the Magic8Ball can respond with

easteregg_answers = [
	"The answer to life the universe and everything", 
	"the answer to life the universe and everything", 
	"The answer to life, the universe, and everything", 
	"the answer to life, the universe, and everything", 
	"The answer to life the universe and everything.", 
	"the answer to life the universe and everything.", 
	"The answer to life, the universe, and everything.", 
	"the answer to life, the universe, and everything.", 
	"The answer to life the universe and everything ", 
	"the answer to life the universe and everything ", 
	"The answer to life, the universe, and everything ", 
	"the answer to life, the universe, and everything ", 
	"The answer to life the universe and everything. ", 
	"the answer to life the universe and everything. ", 
	"The answer to life, the universe, and everything. ", 
	"the answer to life, the universe, and everything. "]

answers= (
	"As I see it, yes.", 
	"Ask again later.", 
	"Better not tell you now.", 
	"Cannot predict now.", 
	"Concentrate and ask again.",
	"Don’t count on it.", 
	"It is certain.", 
	"It is decidedly so.", 
	"Most likely.", 
	"My reply is no.", 
	"My sources say no.", 
	"Outlook not so good.", 
	"Outlook good.", 
	"Reply hazy, try again.", 
	"Signs point to yes.", 
	"Very doubtful.", 
	"Without a doubt.", 
	"Yes.", 
	"Yes - definitely.", 
	"You may rely on it.")

# function to answer the user

length = len(answers)
r = random.random() * length
r = int(r)
response = answers[r]


if userinput in easteregg_answers:
	print("\033[31m42\033[0m")
else:
	print(response)

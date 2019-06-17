# This is the story

story1 = "I once had a friend named %s."
story2 = "He was %s years old and he worked as a %s."
story3 = "One day he went up to me wearing a %s"
story4 = "and he said to me \"There's a %s on your shoe.\""
story5 = "So I scraped it off and went about my day throwing %ss at %ss"

print 'Hello and welcome to My Mad Lib.'

# Questions that fill out the mad lib

user_name = raw_input("What is your name? ")
name = raw_input("Please give me a different name: ")
age = raw_input("Give me an age number: ")
job = raw_input("Give me a job: ")
clothing = raw_input("Give me a clothing item: ")
noun1 = raw_input("Give me a noun: ")
noun2 = raw_input("Give me another noun: ")
noun3 = raw_input("One more noun, please. And then we'll be done: ")

# Results of answers

print story1 % name
print story2 % (age, job)
print story3 % clothing
print story4 % noun1
print story5 % (noun2, noun3)

# End

print 'Thank you for playing, %s!' % (user_name)
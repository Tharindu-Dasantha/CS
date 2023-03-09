import random 

# creating the list of wishes
wishes = ["It is certain",
          "It is decidedly so",
          "Yes definitely",
          "Reply hazy try again",
          "Ask again later",
          "Concentrate and ask again",
          "My reply is no",
          "Outlook not so good",
          "Very doubtful"]

print(wishes[random.randint(0, (len(wishes)-1))])
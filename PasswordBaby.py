tupPassword1 = ("MyPassword123")

badAttempts = 0
guessCorrect = False

while (badAttempts < 3):
  guess = input("Enter password: ")
  if guess == tupPassword1:
   print ("U\'re in!")
   break
  
  else:
    if badAttempts < 2:
     print ("Try again!")
    else: 
      print ("Too many attempts!")
  badAttempts += 1
 
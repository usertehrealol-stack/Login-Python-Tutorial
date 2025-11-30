# This is a comment. This won't be printed out to console. 

print("Enter a username") # prints the text 'Enter a username' to console
usr = input() # records the user's input and saves it to the variable 'usr'. <-- short for 'user'/ short for 'username'.
hshusr = hash(usr) # hashes the thing so more secure. convenient, isn't it?
print("Enter a password") # prints the text 'Enter a password' to console
pss = input() # records the user's input again and saves it to the variable 'pss' <-- short for password.
hshpss = hash(pss) # hashes the password into an obscure number so bye bye hackers i guess

# Now for login guessing time...

print("Enter your username:") # prints the text in quotation marks, as you might guess
USRGUESS = input()# variable in capitals usually highlights a constant (variable that never changes) but i just tried to emphasise it.
print("Enter your password:") # same as what you expect
PSSGUESS = input() # user's password guess.
hshuguess = hash(USRGUESS) # changes the user's guess to hash
hshpguess = hash(PSSGUESS) # changes the pass guess to hash

if hshuguess == hshusr and hshpguess == hshpss: # if the hash of the username guess is EQUAL to the hashed username and the hash of the password guess is EQUAL to the hashed password...
    print("Logged in successfully") # successful login
else:
    print("Invalid username/ password") # uh oh, fail!
    
# hash brown lesson
# i mean HASH!!

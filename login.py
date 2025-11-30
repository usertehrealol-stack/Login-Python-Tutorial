# This is a comment. This won't be printed out to console. 

print("Enter a username") # prints the text 'Enter a username' to console
usr = input() # records the user's input and saves it to the variable 'usr'. <-- short for 'user'/ short for 'username'.
print("Enter a password") # prints the text 'Enter a password' to console
pss = input() # records the user's input again and saves it to the variable 'pss' <-- short for password.

# Now for login guessing time...

print("Enter your username:") # prints the text in quottion marks, as you might guess
USRGUESS = input() # variable in capitals usually highlights a constant (variable that never changes) but i just tried to emphasise it.
print("Enter your password:") # same as what you expect
PSSGUESS = input() # user's password guess.

if USRGUESS == usr and PSSGUESS == pss: # if usrguess is EQUAL to usr and pssguess is EQUAL to pss...
    print("Logged in successfully") # successful login
else:
    print("Invalid username/ password") # uh oh, fail!
    
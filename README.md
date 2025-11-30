# Login Python Tutorial
# This is a tutorial in Python of how to create a simple login.

You want to create a simple login thing in Python but don't know how to do it?
here you go.

First, open a text editor. you can use VS Code, like me, but you can also use 
Notepad++, the normal Notepad, or any other thing that works for you.

Make a file if you haven't already. 

Rename your file to login.py. You can search up how to rename for your local text editor.
In Notepad++, I'm aware that it is File > Rename. 

This will automatically change the input language format to Python as it uses the .py
extension, however for some primitive text editors it does not.

Now, follow as i do.

====================START COPYPASTING HERE INTO LOGIN.PY=================================
# This is a comment. This won't be printed out to console. 

print("Enter a username") # prints the text 'Enter a username' to console
usr = input() # records the user's input and saves it to the variable 'usr'. <-- short for 'user'/ short for 'username'.
print("Enter a password") # prints the text 'Enter a password' to console
pss = input() # records the user's input again and saves it to the variable 'pss' <-- short for password.

# Now for login guessing time...

print("Enter your username:") # prints the text in quotation marks, as you might guess
USRGUESS = input() # variable in capitals usually highlights a constant (variable that never changes) but i just tried to emphasise it.
print("Enter your password:") # same as what you expect
PSSGUESS = input() # user's password guess.

if USRGUESS == usr and PSSGUESS == pss: # if usrguess is EQUAL to usr and pssguess is EQUAL to pss...
    print("Logged in successfully") # successful login
else:
    print("Invalid username/ password") # uh oh, fail!

==================END OF PYTHON CODE HERE=========================
    
Yay! Now you have a very barebones login in Python. To run it, install python/python3 on your pc's console and run it that way (follow tutorials online on how to install it)
at: https://www.python.org/downloads/

OR 
Run it in an online compiler.

The output should be something like this: ![output](image.png)

OR

something like this: ![output](image-1.png).

There you go! That's your first login in Python. 

More tutorials coming soon...
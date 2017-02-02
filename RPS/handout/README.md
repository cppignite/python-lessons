# Handout #1 

#### Showing Output
 
One of the most fundamental components of programming is printing to the user. In python users interact with their program via the shell window. To print you should use the following syntax:
 
`print("Hello World")`

	
> ##### output:
> Hello World

#### Variables

Were assuming most of you have taken algebra so we know you've seen variables before. In programming its a very similar concept. Variables have a value and a name.

`x = "Hello World"`

You can then use these variables throughout your program.

~~~~
x = "Hello World"
print(x)
~~~~

> ##### output:
> Hello World

#### User Input

The next important step in programming is letting the user interact with the program. Inside every shell window the user can be prompted for text. The syntax is as follows:

`result = input("What is your name?")`

> ##### output:
> What is your name?
 
 How do you think we could print the answer from the input?
 
#### Conditionals

Conditionals allow us to control the flow of the program based on a true or false statement for instance whether two words are the same. Below we compare the user's input to a couple of words in order to create a quiz:

~~~~
quiz = input("Name a programming language:")
if quiz == "python":
    print("Sounds about right!")
elif quiz == "Java":
    print("Perfect")
else 
    print("Sorry I don't know that one")
~~~~

Note how == means something different than =. In this case == is used to compare two things where  = is used to assign a value to a variable. 

Try typing up your own quiz!
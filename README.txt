Ramzi Adil
CS5700 Spring 2022
Assignment 1 Sockets

My Approach:
 - I invested a lot of my time in designing the program, making diagrams and flowcharts etc...
 - I used a recursive approach to solve the statements sent by the server
 - I made my own node class, which is a component of my binary tree class
 - Each node holds a data, left pointer, and right pointer attribute
    > the data attribute can be an operator(stored as a string) or an int
 - I built the tree by scanning the string from right to left until I
    could find the operator with the highest priority in the statement
 - I would successively build my tree layer by layer, the integer values
    would end up in the leaves of the tree and the other nodes would
    hold the operator.
 - I used a try except block to catch any zero division errors.
 - I added a lot of debug statements which I later commented out for a one line output
 - Then I worked on making functions that can make sockets and interact with the server
 - I then added functionality to take in arguments
 - At each step of the way I made JUnit tests to ensure the functionality of my methods/functions/classes
    > These test are in my test_files folder that you can see

My Challenges:
 - The biggest challenge for me was understanding sockets. I don't have a background
    in networking so understanding how they operate was my biggest challenge. That and
    learning how to create makefiles and navigating the khoury machines.





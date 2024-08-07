#!/usr/bin/env python3

## prompting the user for the name of the file to load
filename = input("Enter the name of the file to load: ")

## create file object in "r"ead mode
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

##  Counting and displaying the number of lines in the file
num_lines = len(configlist)
print(f"The file {filename} has {num_lines} lines.")


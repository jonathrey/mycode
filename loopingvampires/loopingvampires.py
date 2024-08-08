#!/usr/bin/env python3

with open("/home/student/mycode/loopingvampires/dracula.txt","r") as readfile:
    count = 0;
    with open("vampytimez.txt", "w") as writefile:
        for line in readfile: 
            if "vampire" in line.lower(): 
                print(line)
                count= count + 1
                writefile.write(line)

    print(f"{count} lines contain the word vampire")

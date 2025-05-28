
D:\>cd projects

D:\Projects>type nul >one.text

D:\Projects>echo "Hello World" > one.text

D:\Projects>type one.txt
The system cannot find the file specified.

D:\Projects>cat one.txt
cat: one.txt: No such file or directory

D:\Projects>type one.txt                 
The system cannot find the file specified.

D:\Projects>del one.text

D:\Projects>type nul >one.txt

D:\Projects>echo "Hello World" > one.txt

D:\Projects>type one.txt
"Hello World" 

D:\Projects>mkdir story

D:\Projects>move one.txt story\
        1 file(s) moved.

D:\Projects>copy story\one.txt story\two.txt
        1 file(s) copied.

D:\Projects>type one.txt
The system cannot find the file specified.

D:\Projects>type story\one.txt
"Hello World" 

D:\Projects>type story\two.txt
"Hello World" 

D:\Projects>ren story\one.txt part_one.txt

D:\Projects>ren story\two.txt part_two.txt

D:\Projects>echo "I am a junior at Becode." > story\part_two.txt

D:\Projects>type story\part_one.txt story\part_two.txt

story\part_one.txt


"Hello World"

story\part_two.txt


"I am a junior at Becode."

D:\Projects>rmdir story
The directory is not empty.

D:\Projects>rmdir /s
The syntax of the command is incorrect.

D:\Projects>rmdir /s story
story, Are you sure (Y/N)? Y

D:\Projects>
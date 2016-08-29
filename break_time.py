# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.


# import the following modules to run in python
import webbrowser
import time

#for the 'while' loop create 2 counters: one for the total number of breaks required of the task and one for the current number of breaks taken
total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
#for the sake of testing, I spaced out the time between breaks to only 10 seconds
while break_count < total_breaks:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=WgJJc0H0enU")
#you can replace the YouTube link with any YouTube link. This is just my favorite song at the moment!
	break_count = break_count + 1

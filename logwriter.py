import time as Time
import os as OS

# Create a log file with user notes. 
# Returns Bool(True on file write success)
def write_txtentry(start_time, end_time, tasks):
    title_string = Time.strftime("%d-%m-%Y.txt", Time.localtime())
    entry_date = Time.strftime("%d of %B, %Y - %A\n", Time.localtime())
    if not OS.path.exists(title_string):
        print("Creating file " + title_string)
        outfile = open(title_string, "a")
        outfile.write(entry_date)
    else:
        print("Opening file " + title_string)
        outfile = open(title_string, "a")
    outfile.write(start_time + "\n")
    for a_task in tasks:
        outfile.write("‣ " + a_task.strip() + "\n")
    outfile.write(end_time + "\n")
    outfile.write("---------------\n")
    outfile.close()
    print("File " + title_string + " written")
    return True

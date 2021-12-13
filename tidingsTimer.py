import time as Time
import os as OS

# Convert hh:mm:ss into seconds
# Args: string; Returns: int
def clock_to_seconds(input_time):
    time_strings = input_time.split(":")
    time_chunks = []
    time_format = {0:0, 1:0, 2:0} 

    for i in range(len(time_strings)-1, -1, -1): # Check if input is digit
        try:
            time_chunks.append(int(time_strings[i]))
        except ValueError:
            return None
    if len(time_chunks) > 3:
        return None # time shouldn't take a day
    for i in range(len(time_chunks)):
        time_format[i] = time_chunks[i]
        
    seconds = time_format[0]
    seconds += time_format[1] * 60
    seconds += time_format[2] * 3600
    return seconds

# Converts "XXhXXmXXs" to seconds Ex.: 1h24m30s
# Args: string; Returns: int
def hms_to_seconds(hms_input):
    hours = 0
    minutes = 0
    seconds = 0
    try:
        if hms_input.find("h"):
            hours = int(hms_input.split("h")[0])
            hms_input = hms_input.split("h")[-1]
        if hms_input.find("m"):
            minutes = int(hms_input.split("m")[0])
            hms_input = hms_input.split("m")[-1]
        seconds = int(hms_input.strip("s"))
        seconds += hours * 3600
        seconds += minutes * 60
    except (ValueError, IndexError) as e:
        print(e)
        return None
    return seconds

# Converts seconds to dictionary
# Args: int; Returns: dict
def seconds_to_clock(seconds):
    hours, seconds = divmod(seconds, 3600) # Separate hours from seconds
    minutes, seconds = divmod(seconds, 60) # Separate minutes from seconds    
    clock_time = {2:hours, 1:minutes, 0:seconds}
    return clock_time

# Create a log file with user notes. 
# Args: struct_time, struct_time, string
# Returns Bool(True on file write success)
def create_txtlog(start_time, end_time, usernotes):
    title_string = Time.strftime("%d-%m-%Y.txt", end_time)
    entry_date = Time.strftime("%d of %B, %Y - %A\n", end_time)
    start = Time.strftime("%H:%M\n", start_time)
    end =  Time.strftime("\n%H:%M\n", end_time)
    if not OS.path.exists(title_string):
        outfile = open(title_string, "a")
        outfile.write(entry_date)
    else:
        outfile = open(title_string, "a")
    outfile.write(start)
    outfile.write(usernotes)
    outfile.write(end)
    outfile.write("---------------")
    outfile.write("\n")
    outfile.close()
    return True

def countdown(seconds):
    while seconds:
        print(seconds, end="\r\n")
        Time.sleep(1)
        seconds -= 1

    print("Timer end")

class Timer:
    def __init__(self, time_string):
        # insert function to convert time_string to seconds
        self.seconds = time_string
        self.start_time = Time.time()

    def __repr__(self):
        clock_time = seconds_to_clock(self.seconds)
        out_clock = "{:02d}:{:02d}".format(clock_time[1], clock_time[0])
        if clock_time[2] > 0:
            out_clock = "{:02d}:".format(clock_time[2]) + out_clock
        return out_clock

    def __add__(self, seconds):
        self.seconds += seconds
    def __sub__(self, seconds):
        self.seconds -= seconds

    def countdown(self):
        while self.seconds >= 0:
            print(self, end="\r")
            Time.sleep(1)
            self.seconds -= 1
        return Time.time()
        
#time_str = input("Enter time: ")
#time_to_countdown = hms_to_seconds(time_str)
#countdown(time_to_countdown)
#print(seconds_to_clock(time_to_countdown))

# Testing create_txtlog
# s_time = Time.localtime(Time.time()-3600)
# e_time = Time.localtime(Time.time())
# test_str = "Example log"
# create_txtlog(s_time, e_time, test_str)

# Testing Time class
# t1 = Timer(1830)
# t2 = Timer(3621)
# print(t1)
# print(t2)
# t1 + 21
# t2 - 56
# print(t1)
# print(t2)

# Testing Time's countdown
t3 = Timer(11)
end = t3.countdown()
print(Time.ctime(end))

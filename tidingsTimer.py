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
        except ValueError as e:
            return e
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
    temp = []
    try:
        if hms_input.find("h") > -1:
            temp = hms_input.split("h")
            hours = int(temp[0])
            hms_input = ""
            for i in range(1, len(temp)):
                hms_input += str(temp[i])
        if hms_input.find("m") > -1:
            temp = hms_input.split("m")
            minutes = int(temp[0])
            hms_input = ""
            for i in range(1, len(temp)):
                hms_input += str(temp[i])
        if len(hms_input) > 0:
            seconds += int(hms_input.strip("s"))
        seconds += hours * 3600
        seconds += minutes * 60
    except (ValueError, IndexError) as e:
        print(e)
        return e
    return seconds

# Check if input string is HH:MM:SS or XXhXXmXXs
# then pass to the correct converter
def parse_timeinput(time_input):
    seconds = 0
    if time_input.find(":") > -1:
        seconds = clock_to_seconds(time_input)
    else:
        seconds = hms_to_seconds(time_input)
    return seconds

# Converts seconds to dictionary
# Args: int; Returns: dict
def seconds_to_clock(seconds):
    hours, seconds = divmod(seconds, 3600) # Separate hours from seconds
    minutes, seconds = divmod(seconds, 60) # Separate minutes from seconds    
    clock_time = {2:hours, 1:minutes, 0:seconds}
    return clock_time



class Timer:
    def __init__(self):
        self.seconds = 0

    def __repr__(self):
        clock_time = seconds_to_clock(self.seconds)
        out_clock = "{:02d}:{:02d}".format(clock_time[1], clock_time[0])
        if clock_time[2] > 0:
            out_clock = "{:02d}:".format(clock_time[2]) + out_clock
        return out_clock

    # 87-90 To expand on: Add a way to add or subtract time whilst the timer is running.
    def __add__(self, seconds):
        self.seconds += seconds
    def __sub__(self, seconds):
        self.seconds -= seconds

    def set_timer(self, time_string):
        self.seconds = parse_timeinput(time_string)

    def countdown_start(self):
        end_time = Time.time() + self.seconds # Calculate what time the timer will end
        end_time_str = Time.strftime("%H:%M", Time.localtime(end_time))
        while self.seconds >= 0:
            print("{}    \tTimer ends on: {}".format(self, end_time_str), end="\r")
            Time.sleep(1)
            self.seconds -= 1
        return Time.localtime()
        
class Logger:
    def __init__(self):
        pass
    
    # Create a log file with user notes. 
    # Returns Bool(True on file write success)
    def write_txtentry(self, start_time, end_time):
        title_string = Time.strftime("%d-%m-%Y.txt", end_time)
        entry_date = Time.strftime("%d of %B, %Y - %A\n", end_time)
        start = Time.strftime("%H:%M\n", start_time)
        end =  Time.strftime("\n%H:%M\n", end_time)
        usernotes = input("What did you do? (Separate tasks with ,)\n").split(",")
        if not OS.path.exists(title_string):
            print("Creating file " + title_string)
            outfile = open(title_string, "a")
            outfile.write(entry_date)
        else:
            print("Opening file " + title_string)
            outfile = open(title_string, "a")
        outfile.write(start + "\n")
        for a_note in usernotes:
            outfile.write("‣ " + a_note.strip() + "\n")
        outfile.write("Timer ended at: " + end + "\n")
        outfile.write("Note written at: " + Time.strftime("%H:%M",Time.localtime()))
        # 126-127 To expand on: Track the difference between timer end and note taken
        outfile.write("\n---------------\n")
        outfile.close()
        print("File " + title_string + " written")
        return True

# The run part of the program
run_again = True
rounds = 0
timer = Timer()
logger = Logger()
while run_again:
    time_length = input("Timer length: ")
    start_time = Time.localtime()
    timer.set_timer(time_length)
    end_time = timer.countdown_start() # countdown_start() returns what time it ended
    logger.write_txtentry(start_time, end_time)
    rounds += 1
    print("Round {} has ended".format(rounds))
    user_input = input("Run again? (y/n)")
    if "y" in user_input.lower():
        continue
    else:
        run_again = False



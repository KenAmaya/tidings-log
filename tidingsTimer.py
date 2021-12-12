import time as Time

# Convert hh:mm:ss into seconds
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
def seconds_to_clock(seconds):
    hours, seconds = divmod(seconds, 3600) # Separate hours from seconds
    minutes, seconds = divmod(seconds, 60) # Separate minutes from seconds    
    clock_time = {"hours":hours, "minutes":minutes, "seconds":seconds}
    return clock_time


def countdown(seconds):
    while seconds:
        print(seconds, end="\r\n")
        Time.sleep(1)
        seconds -= 1

    print("Timer end")

        
time_str = input("Enter time: ")
time_to_countdown = hms_to_seconds(time_str)
#countdown(time_to_countdown)
print(seconds_to_clock(time_to_countdown))


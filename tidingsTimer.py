import time as Time

# Convert hh:mm:ss into seconds
def parse_input_colon(input_time):
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

def countdown(seconds):
    while seconds:
        print(seconds, end="\r\n")
        Time.sleep(1)
        seconds -= 1

    print("Timer end")

        
time_str = input("Enter time: ")
time_to_countdown = parse_input_colon(time_str)
countdown(time_to_countdown)

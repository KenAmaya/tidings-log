from datetime import time as Time


def parse_input(input_time):
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
    return time_format

        
time_str = input("Enter time: ")
time_to_countdown = parse_input(time_str)
print(time_to_countdown)

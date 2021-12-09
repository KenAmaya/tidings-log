from datetime import time as Time


def parse_input(input_time):
    time_strings = input_time.split(":")
    time_chunks = []
    time_format = {2:0, 1:0, 0:0} # 3 for hours, 2 for minutes, 1 for seconds

    for a_string in time_strings: # Check if input is digit
        try:
            time_chunks.append(int(a_string))
        except ValueError:
            return None
    if len(time_chunks) <= 3: # Check in only hh:mm:ss
        for i in range(3):
            time_format[i] = time_chunk
        


        
time_str = input("Enter time: ")

from logwriter import write_txtentry

when_start = "What is the start time for this entry? (hh:mm 24hr)"
when_end = "What time did it end? (hh:mm 24hr)"
what_do = "What did you do? (Separate tasks with ',')"
time_start = input(when_start)
time_end = input(when_end)
tasks = input(what_do)
tasks = tasks.split(",")
for a_task in tasks:
    a_task = a_task.strip()

write_txtentry(time_start, time_end, tasks)



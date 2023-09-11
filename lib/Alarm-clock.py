import tkinter as tk
import time

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_time = time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        status_label.config(text="Invalid time format. Use HH:MM:SS")
        return

    current_time = time.localtime()
    time_diff = (time.mktime(alarm_time) - time.mktime(current_time))
    
    if time_diff <= 0:
        status_label.config(text="Please set a future time.")
        return

    status_label.config(text=f"Alarm set for {alarm_time.tm_hour}:{alarm_time.tm_min}:{alarm_time.tm_sec}")
    time.sleep(time_diff)
    status_label.config(text="Alarm!")

# Create a basic GUI window
root = tk.Tk()
root.title("Basic Alarm Clock")

# Label for instructions
instructions_label = tk.Label(root, text="Enter the time (HH:MM:SS):")
instructions_label.pack()

# Entry widget for time input
entry = tk.Entry(root)
entry.pack()

# Button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

# Label for displaying status and notifications
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()


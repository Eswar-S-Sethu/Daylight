# Import Required Library
from tkinter import *
import datetime
import time,random,serial
from playsound import playsound
from threading import *

ser = serial.Serial('/dev/ttyACM0', 9600)

def calculate_comfort_and_random():
    read_serial = ser.readline().decode('utf-8')  # Decode bytes to string
    values = read_serial.split()  # Split the string by whitespace

    comfort_level = None
    random_number = None

    if len(values) >= 6:  # Check if there are enough values
        humidity_str = values[1].replace("%", "")  # Remove "%" character
        temperature_str = values[3]
        distance_str = values[5]

        try:
            humidity = float(humidity_str)  # Convert to float
            temperature = float(temperature_str)  # Convert to float
            distance = float(distance_str)  # Convert to float

            # Update comfort_level and random_number based on conditions
            if temperature < 20 and humidity > 70 and distance > 200:
                comfort_level = "High"
                random_number = random.randint(10, 99)  # Two-digit random number
            elif temperature > 20 and humidity < 60:
                comfort_level = "Medium"
                random_number = random.randint(1, 9)  # One-digit random number
            else:
                comfort_level = "Low"
                random_number = random.randint(1, 4)
        except ValueError:
            print("Error: Unable to convert values to float.")
    return comfort_level,random_number

# Calculate comfort_level and random_number once
comfort_level, random_number = calculate_comfort_and_random()

# Now you can use comfort_level and random_number anywhere in your program
print("Comfort Level:", comfort_level, "Random Number:", random_number)

set_alarm_time=""

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# other GUI toplevel functions

def show_idle_window():
    idle_window = Toplevel()
    idle_window.title("Idle Window")
    idle_window.geometry("400x400")
    idle_window.attributes("-topmost", True)  # Ensure the idle window is always on top

    # Function to close the idle window when clicked
    def close_window(event):
        idle_window.destroy()

    # Bind click event to close window
    idle_window.bind("<Button-1>", close_window)

    # Add widgets for displaying current time, motivational quote, and username
    current_time_label = Label(idle_window, text="Current Time:")
    current_time_label.pack(pady=5)

    # Placeholder labels for displaying current time and motivational quote
    time_label = Label(idle_window, text="", font=("Helvetica", 14))
    time_label.pack()


    # Placeholder label for displaying username
    username_label = Label(idle_window, text="Eswar")
    username_label.pack(pady=5)

    # Placeholder for displaying username
    username_value_label = Label(idle_window, text="", font=("Helvetica", 12))
    username_value_label.pack()

    # Update the current time label every second
    def update_time():
        current_time = time.strftime("%H:%M")
        time_label.config(text=current_time)
        time_label.after(1000, update_time)  # Schedule the update after 1 second

    update_time()  # Start updating the time


def show_task_success_window():
    task_success_window = Toplevel()
    task_success_window.geometry("400x400")
    task_success_window.title("Task Success")
    task_success_window.attributes("-topmost", True)  # Ensure the task success window is always on top

    # Add widgets for displaying task success information
    heading_label = Label(task_success_window, text="Task Complete", font=("Helvetica", 18, "bold"))
    heading_label.pack(pady=10)

    greeting_label = Label(task_success_window, text="Good day mate!", font=("Helvetica", 14))
    greeting_label.pack(pady=5)

    # Schedule the task success window to close after 20 seconds
    task_success_window.after(10000, task_success_window.destroy)
    show_idle_window()

def show_task_window():
    task_window = Toplevel()
    task_window.title("Task Window")
    task_window.geometry("400x400")
    task_window.attributes("-topmost", True)  # Ensure the task window is always on top

    # Function to close the task window
    def close_window():
        task_window.destroy()

    # Add widgets for displaying task information
    task_label = Label(task_window, text="Task: Add Two Numbers", font=("Helvetica", 16, "bold"))
    task_label.pack(pady=10)

    # Generate two random numbers for the task
    num1 = random.randint(1, 100) + random_number
    num2 = random.randint(1, 100) + random_number

    num1_label = Label(task_window, text=f"Number 1: {num1}", font=("Helvetica", 14))
    num1_label.pack()

    num2_label = Label(task_window, text=f"Number 2: {num2}", font=("Helvetica", 14))
    num2_label.pack()

    sum_entry = Entry(task_window, width=10, font=("Helvetica", 14))
    sum_entry.pack(pady=10)

    # Add a timer label
    timer_label = Label(task_window, text="00:00", font=("Helvetica", 14))
    timer_label.pack(pady=5)

    # Function to update the timer
    def update_timer():
        nonlocal remaining_time
        if remaining_time > 0:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            remaining_time -= 1
            task_window.after(1000, update_timer)  # Update every second
        else:
            close_window()

    remaining_time = 15  # Timer set to 15 seconds
    update_timer()  # Start updating the timer

    done_button = Button(task_window, text="Done", command=show_task_success_window)
    done_button.pack(pady=10)

def show_alarm_window(alarm_time):
    alarm_window = Toplevel()
    alarm_window.geometry("400x400")
    alarm_window.title("Alarm Ringing")
    alarm_window.attributes("-topmost", True)  # Ensure the alarm window is always on top

    # Add widgets for displaying alarm information
    alarm_label = Label(alarm_window, text="Alarm Time:")
    alarm_label.pack(pady=5)

    alarm_time_label = Label(alarm_window, text=alarm_time, font=("Helvetica", 24))
    alarm_time_label.pack()

    move_on_button = Button(alarm_window, text="Move On", command=show_task_window)
    move_on_button.pack(pady=10)


# Function to play the sound in a loop
def play_sound_loop():
    playsound("sound.mp3")


# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
    # Infinite Loop
    while True:
        # Set Alarm 
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            show_alarm_window(set_alarm_time)
            print("Time to Wake up")
            # Playing sound
            print("going off")
            play_sound_loop()  # This line is now reachable

            

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()

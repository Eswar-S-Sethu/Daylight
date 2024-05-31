import tkinter as tk
from tkinter import ttk
import time,random,json,asyncio,threading
import python_weather as pyw
import quote as qt


# Function to add an alarm to the list and JSON file
def add_alarm():
    hours = int(hour_spinbox.get())
    minutes = int(minute_spinbox.get())
    alarm_time = f"{hours:02d}:{minutes:02d}"
    listbox.insert(tk.END, alarm_time)
    add_alarm_time_to_file(alarm_time)

    # Start an asynchronous task to manage the alarm in a separate thread
    threading.Thread(target=manage_alarm_thread, args=(alarm_time,), daemon=True).start()


# Function to manage the alarm in a separate thread
def manage_alarm_thread(alarm_time):
    asyncio.run(manage_alarm(alarm_time))


# Function to add a new alarm time to the JSON file
def add_alarm_time_to_file(alarm_time):
    try:
        # Load existing alarm times from the JSON file
        with open("alarms.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list of alarm times
        data = {"alarms": []}

    # Append the new alarm time to the list of alarm times
    data["alarms"].append(alarm_time)

    # Write the updated data back to the JSON file
    with open("alarms.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to read alarm times from the JSON file
def read_alarm_times_from_file():
    try:
        # Open the JSON file and load the data
        with open("alarms.json", "r") as file:
            data = json.load(file)
            alarm_times = data.get("alarms", [])
        return alarm_times
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

# Function to remove an alarm time from the JSON file
def remove_alarm_from_file(alarm_time):
    try:
        # Load existing alarm times from the JSON file
        with open("alarms.json", "r") as file:
            data = json.load(file)
            alarm_times = data.get("alarms", [])

        # Remove the specified alarm time from the list
        alarm_times.remove(alarm_time)

        # Update the JSON file with the modified list
        data["alarms"] = alarm_times
        with open("alarms.json", "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        pass  # File not found, nothing to remove


# Function to delete an alarm from the list and stop checking it
def delete_alarm():
    selection = listbox.curselection()
    if selection:
        alarm_time = listbox.get(selection)
        listbox.delete(selection)
        remove_alarm_from_file(alarm_time)


async def manage_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            show_alarm_window(alarm_time)
            remove_alarm_from_file(alarm_time)
            listbox.delete(listbox.get(0, tk.END).index(alarm_time))
            break
        await asyncio.sleep(60)  # Check every minute

def populate_listbox():
    # Read alarm times from the JSON file
    alarm_times = read_alarm_times_from_file()

    # Insert each alarm time into the listbox
    for alarm_time in alarm_times:
        listbox.insert(tk.END, alarm_time)

def show_alarm_window(alarm_time):
    alarm_window = tk.Toplevel()
    alarm_window.title("Alarm Ringing")
    alarm_window.attributes("-topmost", True)  # Ensure the alarm window is always on top

    # Add widgets for displaying alarm information
    alarm_label = ttk.Label(alarm_window, text="Alarm Time:")
    alarm_label.pack(pady=5)

    alarm_time_label = ttk.Label(alarm_window, text=alarm_time, font=("Helvetica", 24))
    alarm_time_label.pack()

    move_on_button = ttk.Button(alarm_window, text="Move On", command=alarm_window.destroy)
    move_on_button.pack(pady=10)

def show_task_success_window():
    task_success_window = tk.Toplevel()
    task_success_window.title("Task Success")
    task_success_window.attributes("-topmost", True)  # Ensure the task success window is always on top

    # Add widgets for displaying task success information
    heading_label = ttk.Label(task_success_window, text="Task Complete", font=("Helvetica", 18, "bold"))
    heading_label.pack(pady=10)

    greeting_label = ttk.Label(task_success_window, text="Good day mate!", font=("Helvetica", 14))
    greeting_label.pack(pady=5)

    # Schedule the task success window to close after 20 seconds
    task_success_window.after(20000, task_success_window.destroy)

def show_idle_window():
    idle_window = tk.Toplevel()
    idle_window.title("Idle Window")
    idle_window.attributes("-topmost", True)  # Ensure the idle window is always on top

    # Function to close the idle window when clicked
    def close_window(event):
        idle_window.destroy()

    # Bind click event to close window
    idle_window.bind("<Button-1>", close_window)

    # Add widgets for displaying current time, motivational quote, and username
    current_time_label = ttk.Label(idle_window, text="Current Time:")
    current_time_label.pack(pady=5)

    # Placeholder labels for displaying current time and motivational quote
    time_label = ttk.Label(idle_window, text="", font=("Helvetica", 14))
    time_label.pack()

    quote_label = ttk.Label(idle_window, text="Motivational Quote:", wraplength=300)
    quote_label.pack(pady=10)

    # Placeholder label for displaying username
    username_label = ttk.Label(idle_window, text="Username:")
    username_label.pack(pady=5)

    # Placeholder for displaying username
    username_value_label = ttk.Label(idle_window, text="", font=("Helvetica", 12))
    username_value_label.pack()

    # Update the current time label every second
    def update_time():
        current_time = time.strftime("%H:%M")
        time_label.config(text=current_time)
        time_label.after(1000, update_time)  # Schedule the update after 1 second

    update_time()  # Start updating the time

def show_task_window():
    task_window = tk.Toplevel()
    task_window.title("Task Window")
    task_window.attributes("-topmost", True)  # Ensure the task window is always on top

    # Function to close the task window
    def close_window():
        task_window.destroy()

    # Add widgets for displaying task information
    task_label = ttk.Label(task_window, text="Task: Add Two Numbers", font=("Helvetica", 16, "bold"))
    task_label.pack(pady=10)

    # Generate two random numbers for the task
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    num1_label = ttk.Label(task_window, text=f"Number 1: {num1}", font=("Helvetica", 14))
    num1_label.pack()

    num2_label = ttk.Label(task_window, text=f"Number 2: {num2}", font=("Helvetica", 14))
    num2_label.pack()

    sum_entry = ttk.Entry(task_window, width=10, font=("Helvetica", 14))
    sum_entry.pack(pady=10)

    # Add a timer label
    timer_label = ttk.Label(task_window, text="00:00", font=("Helvetica", 14))
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

    done_button = ttk.Button(task_window, text="Done", command=close_window)
    done_button.pack(pady=10)

# Function to check the alarms and show the alarm window if an alarm time matches
def check_alarms():
    current_time = time.strftime("%H:%M")
    alarm_times = read_alarm_times_from_file()

    for alarm_time in alarm_times:
        if current_time == alarm_time:
            show_alarm_window(alarm_time)
            remove_alarm_from_file(alarm_time)
            listbox.delete(listbox.get(0, tk.END).index(alarm_time))


root = tk.Tk()

root.title("Alarm List")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label = ttk.Label(frame, text="Set Alarm Time:")
label.grid(row=0, column=0, padx=5, pady=5)

hour_spinbox = ttk.Spinbox(frame, from_=0, to=23, width=2)
hour_spinbox.grid(row=0, column=1, padx=(0, 5), pady=5)

minute_spinbox = ttk.Spinbox(frame, from_=0, to=59, width=2)
minute_spinbox.grid(row=0, column=2, padx=(0, 5), pady=5)

add_button = ttk.Button(frame, text="Add Alarm", command=add_alarm)
add_button.grid(row=0, column=3, padx=5, pady=5)

delete_button = ttk.Button(frame, text="Delete Alarm", command=delete_alarm)
delete_button.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="we")

scrollbar = ttk.Scrollbar(root, orient="vertical")
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, width=30, height=5)
populate_listbox()
scrollbar.config(command=listbox.yview)

listbox.pack(padx=10, pady=(0, 10), side="top", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


root.mainloop()

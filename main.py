import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    read_serial = ser.readline().decode('utf-8')  # Decode bytes to string
    values = read_serial.split()  # Split the string by whitespace
    if len(values) >= 6:  # Check if there are enough values
        humidity = values[1]
        temperature = values[3]
        distance = values[5]
        print("Humidity:", humidity, "Temperature:", temperature, "Distance:", distance)

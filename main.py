import serial

# Set the serial port and baud rate
ser = serial.Serial('/dev/ttyACM0', 9600)  # Change '/dev/ttyACM0' to the appropriate port on your system

if ser.in_waiting > 0:
    arduino_data = ser.readline().decode().strip()

    # Split the received data into temperature, humidity, and distance
    temperature, humidity, distance = arduino_data.split(',')

    # Print the separated data
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Distance:", distance)

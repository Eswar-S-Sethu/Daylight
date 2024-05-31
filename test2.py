import asyncio

async def alarm(delay, message):
    print(f"Alarm set for {delay} seconds.")
    await asyncio.sleep(delay)
    print(f"Alarm: {message}")

async def main():
    delay = int(input("Enter the delay in seconds: "))
    message = input("Enter the alarm message: ")
    await alarm(delay, message)

# Run the main coroutine
asyncio.run(main())

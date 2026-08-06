import asyncio


async def fetch_data():
    print("Start fetching...")
    # Simulates an asynchronous network delay (non-blocking)
    await asyncio.sleep(10)
    print("Data retrieved!")
    return {"data": 123}


async def main():
    # Pauses main() until fetch_data() completes
    result = await fetch_data()
    print(f"Result: {result}")


# Starts the Event Loop and runs the main coroutine
asyncio.run(main())

import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:10000"
    async with websockets.connect(uri, ping_timeout=None) as websocket:
        while True:
            message = input("Enter message: ")
            await websocket.send(message)
            print("Message sent")
            response = await websocket.recv()
            print(f"Server says: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())

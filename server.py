import asyncio
import websockets

async def send_hello(websocket, path):
    print("Server starts! ;)")
    try:
        while True:
            name = await websocket.recv()
            print(f"{name}")
            await websocket.send(f"Hello {name}!")
            print("Превышено время ожидания приема сообщения от клиента")
    except (websockets.exceptions.ConnectionClosedError, asyncio.TimeoutError):
        print("Somthing went wrong -.-")

async def main():
    server = await websockets.serve(send_hello, "localhost", 10000, ping_interval=10)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())

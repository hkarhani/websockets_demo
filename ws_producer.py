import asyncio
import websockets
import socket

async def produce(message: str, host: str, port: int)->None: 
    async with websockets.connect(f'ws://{host}:{port}') as ws: 
        await ws.send(message)
        await ws.recv()

if __name__ == "__main__": 
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 5000
    loop = asyncio.get_event_loop()
    loop.run_until_complete(produce(message='hi', host = server_ip, port=server_port))
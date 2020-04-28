import asyncio
import websockets
import logging
import socket
from websockets import WebSocketClientProtocol

logging.basicConfig(level=logging.INFO)

async def consumer_handler(ws:WebSocketClientProtocol ) -> None: 
    async for message in ws: 
        log_message(message)

async def consume(host: str, port:int)->None: 
    ws_resource_url = f"ws://{host}:{port}"
    async with websockets.connect(ws_resource_url) as websocket:
        await consumer_handler(websocket)
            
def log_message(message:str)->None: 
    logging.info(f"Message: {message}")
    
if __name__ == "__main__": 
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 5000
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(host = server_ip, port=server_port))
    loop.run_forever()
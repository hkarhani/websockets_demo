import asyncio
import logging
import websockets
import socket
from websockets import WebSocketServerProtocol 

logging.basicConfig(level=logging.INFO) 

class Server: 
    clients = set()
    
    async def register(self, ws: WebSocketServerProtocol)->None: 
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects.')
    
    async def unregister(self, ws: WebSocketServerProtocol)->None:
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects.')
        
    async def send_to_clients(self,  message: str)->None: 
        if self.clients: 
            await asyncio.wait([client.send(message) for client in self.clients])
            
    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str)->None:
        await self.register(ws)
        try: 
            await self.distribute(ws)
        finally: 
            await self.unregister(ws)
    
    async def distribute(self, ws: WebSocketServerProtocol) ->None: 
        async for message in ws: 
            await self.send_to_clients(message)
            
            
if __name__ == "__main__": 
    
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 5000
    
    server = Server()
    start_server = websockets.serve(server.ws_handler, server_ip , server_port)
    print(f'Starting Websockets server: {server_ip}:{server_port}')
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_server)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Exception received.. shutting down..")
    
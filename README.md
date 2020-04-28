# WebSockets Python Demo 

Easiest way to test Websockets in python within a new Docker Container: 

Clone this repo: 
`git clone https://github.com/hkarhani/websockets_demo.git`

Change directory to cloned websockets_demo folder. 

Create a new Container based on built-in Dockerfile:

`docker build -t wsdemo .`

Run the Container: 

`docker run -d -p 8888:8888 wsdemo` 

Login to Jupyter Notebook via your browser at: localhost:8888. 

1. Launch first the WS Server: `python3 ws_server.py` 
2. Launch the WS Client: `python3 ws_client.py`
3. Finally using the producer to send hi message or JSON data to Server (which will be distributed to all connected clients): `python3 ws_producer.py`

Enjoy! 

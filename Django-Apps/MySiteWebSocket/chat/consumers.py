# chat/consumers.py
import json
from collections import deque

from channels.generic.websocket import AsyncWebsocketConsumer
import threading
import asyncio

# Shared message queue using a deque
message_queue = deque(maxlen=10)  # Set the maximum length as needed

# Create a set to store active WebSocket connections
# live_websockets = set()
# Start reporting when at least there is one live connection. 
# is_alive_connection = False


def print_server_info():
    # Print live threads names and IDs
    live_threads = threading.enumerate()
    print("\nLive threads:")
    for thread in live_threads:
        print(f"Name: {thread.name}, ID: {thread.ident}")

    # Print live async objects names and IDs
    live_tasks = asyncio.all_tasks()
    print("\nLive async objects:")
    for task in live_tasks:
        print(f"Name: {task.get_coro().__name__}, ID: {id(task)}")

    # Print live websockets and client IP, port
    # print("\nLive websockets:")
    # for websocket in live_websockets:
    #     print(f"channel_name: {websocket[2]}, Client IP: {websocket[0]}, Port: {websocket[1]}")


# Start the periodic printing of server information
# async def print_server_info_periodically():
#     while True:
#         print_server_info()
#         await asyncio.sleep(10)  


class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"messages": list(message_queue)}))
        print("\nmessage_queue: ", message_queue)
        print()
        print_server_info()
        # await print_server_info_periodically()

        #live_websockets.add((self.scope['client'][0], self.scope['client'][1], self.channel_name))



    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        #live_websockets.remove((self.scope['client'][0], self.scope['client'][1], self.channel_name))
        print_server_info()
        # if len(live_websockets) == 0:
        #     live_websockets = False


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # When receiving a message from the WebSocket, add it to the message queue
        message_queue.append(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
        print_server_info()



    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        print("\nmesssage: ",message)
        print()
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        print_server_info()



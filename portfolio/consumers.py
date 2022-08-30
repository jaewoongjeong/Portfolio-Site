import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

'''
    - Inheriting websocket class allows to create a handler class that takes care of websocket
    - There is only one consumer on each connection
'''
class ChatConsumer(WebsocketConsumer):
    # Called when there is a connection established with the user
    def connect(self):
        '''
            - 'self.channel_layer.group_add' adds channel to a group
            - async_to_sync() converts asynchronous function into synchronous function
        '''
        # Joins the 'room' group
        async_to_sync(self.channel_layer.group_add)(
            'details',
            self.channel_name,
        )

        # It connects the user to the websocket
        self.accept()


    # Called when the websocket connection is disconnected
    def disconnect(self, close_code):
        # Comes out from the 'room' group
        async_to_sync(self.channel_layer.group_discard)(
            'details',
            self.channel_name
        )


    # Called when the user sends a message via websocket
    def receive(self, text_data):
        # Receiving JSON file
        json_data = json.loads(text_data)

        '''
            - You can specify the event handler when sending a message by 'type'
            - In this example, the event handler is 'chat_message()'
        '''
        # Sends a message to the 'room' group
        async_to_sync(self.channel_layer.group_send)(
            'details',
            {
                'type': 'chat_message',
                'message': json_data
            }
        )


    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
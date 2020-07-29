import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from model.message import Message
from model.message_type import MessageType
import json

msg = '0;1;Deletado com sucesso!;None;Message success;success'


msg_t_c = MessageType('Message success','success')
msg_c =  Message(1,'Deletado com sucesso!',msg_t_c)

str_json = json.dumps(msg_c.__dict__)
print(str_json)
message_type = Message(**json.loads(str_json) ) 
print(message_type.message_type.name )


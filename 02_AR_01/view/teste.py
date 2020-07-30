import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from model.message import Message
from model.message_type import MessageType
import json

msg = '0;1;Deletado com sucesso!;None;Message success;success'


msg_t_c = MessageType('Message success', 'success')
msg_c =  Message(1, 'Deletado com sucesso!', msg_t_c)

str_json = json.dumps(msg_c.__dict__)
# Serialize type_message sem passar o __dict__ no message
# message_json = json.dumps(message.__dict__, default= lambda o: o.__dict__)
print(str_json)

# Problema:
# message = Message(**json.loads(str_json))
# Solucao:
message = Message.from_json(json.loads(str_json))

print(message.message_type, type(message.message_type))
print(message, type(message))

import vk_api
import time
import vk
#регестрация в вк
vk=vk_api.VkApi(token="")
vk._auth_token()

values={'out':0,'count':100,'time_offset':60}
vk.method('messages.get',values)




#отправка сообщения
def write_messg(user_id,s) :
    vk.method("messages.send",{'user_id':user_id,'message':s})

while True :
    response=vk.method('messages.get',values)
    if response['items']:
         values['last_message_id']=response['items'][0]['id']
    for item in response ['items'] :
        write_messg(item['user_id'],'Привет,создание')
    time.sleep(1)
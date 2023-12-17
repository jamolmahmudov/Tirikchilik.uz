import requests
from settings import URL
from time import sleep
from sends import send_animation,send_audio,send_contact,send_dice,send_document,send_location,send_message,send_photo,send_video,send_voice

welcome_msg = '''
Assalomu Alaykum!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar 
mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan 
turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda 
stikerpak sovg'a qilinadi :)

O'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.

Toshkent bo'ylab yetkazib berish - 20 000 so'm.
Ozbekiston bo'ylab yetkazib berish - 30 000 som.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish 
orqali buyurtma berishni boshlashingiz mumkin.'''



def get_updets(url:str):
    endpoint = "/getUpdates"
    url += endpoint
    respons = requests.get(url)
    if respons.status_code == 200:
        result = respons.json()['result']
        if len(result)!=0:
            return result[-1]
        else:
            return 404
    else:
        respons.status_code
# print(get_updets(URL))
def main(url):
    last_update_id = -1
    while True:
        curent_update = get_updets(url)
        if curent_update['update_id']!=last_update_id:
            user = curent_update['message']['from']
            dice = curent_update['message'].get("dice")
            text = curent_update['message'].get('text')
            contact = curent_update['message'].get('contact')
            photo = curent_update['message'].get('photo')
            location = curent_update['message'].get('location')
            audio = curent_update['message'].get("audio")
            document = curent_update['message'].get("document")
           
            animation = curent_update['message'].get("animation")
            if text!=None:
                send_message(url, user[id], text)
            elif text== "/start":
                send_message(url,user['id'], "kerakli bo'limni tanlang" ,reply_markup)
            elif contact!=None:
                send_contact(url,user['id'],contact['phone_number'],contact['first_name'])
            elif photo!=None:
                print(photo)
                send_photo(url=url,chat_id=user['id'],photo=photo[0]['file_id'])
            elif location!=None:
                print(location)
                send_location(url=url,chat_id=user['id'],latitude=location['latitude'],longitude=location['longitude'])
            elif audio!=None:
                send_audio(url,user['id'],audio['file_id'])
            elif document!=None:
                send_document(url,user['id'],document['file_id'])
            elif dice!=None:
                send_dice(url,user['id'],dice['emoji'])
            elif animation != None:
                print(animation)
                send_animation(url,user['id'],animation)
            last_update_id = curent_update['update_id']
        sleep(0.3)
main(URL)




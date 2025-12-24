import telebot,os
import tele
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
#from file import *
#from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '8234402485:AAFnDkdnMNZnRDbYsBT76zhUuhm1kzX9XVI'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=5794137971
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/BINAR9")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/GF_MAA/881'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
The VIP plan allows you to use all the tools and gateways in the bot without limits. You can also check cards through the file. 
━━━━━ 
VIP plan subscription prices: 
1 day = $1 
3 days = $3 
1 week = $6 
1 month = $15 
-- 
Payment methods: 
Korek and USDT 
Note: Prices are in US dollars. If you want to pay via Asiacell, multiply the amount by *2
*2.
━━━━━
To purchase from here @BINAR9</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/BINAR9")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/GF_MAA/881'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

✅ 𝐒𝐭𝐫𝐢𝐩𝐞  <code>/chk </code>

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/BINAR9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
The VIP plan allows you to use all the tools and gateways in the bot without limits. You can also check cards through the file. 
━━━━━ 
VIP plan subscription prices: 
1 day = $1 
3 days = $3 
1 week = $6 
1 month = $15 
-- 
Payment methods: 
Korek and USDT 
Note: Prices are in US dollars. If you want to pay via Asiacell, multiply the amount by *2
*2.
━━━━━
To purchase from here @BINAR9</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/BINAR9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
The VIP plan allows you to use all the tools and gateways in the bot without limits. You can also check cards through the file. 
━━━━━ 
VIP plan subscription prices: 
1 day = $1 
3 days = $3 
1 week = $6 
1 month = $15 
-- 
Payment methods: 
Korek and USDT 
Note: Prices are in US dollars. If you want to pay via Asiacell, multiply the amount by *2
*2.
━━━━━
To purchase from here @BINAR9</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/BINAR9")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"𝐒𝐭𝐫𝐢𝐩𝐞  ",callback_data='b6')

		keyboard.add(contact_button)

		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'b6')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝐒𝐭𝐫𝐢𝐩𝐞  '
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @BINAR9')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(brn6(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @BINAR9''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ Successed✅
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ STRIP AUTH		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: BINAR</b>'''
					if "Charged !✅" in last or "The card's security code is incorrect." in last or 'Payment success' in last or 'success' in last or 'Payment Completed.' in last or 'Approved' in last or 'CVV' in last or 'Success'in last or 'CHARGED' in last or 'Payment has been made' in last or 'CHARGED 1$' in last or 'successfully' in last or 'INVALID_BILLING_ADDRESS' in last or 'Your payment has already been processed' in last or 'Thank You For Donation.' in last or 'status": "succeeded' in last or 'NEED_CREDIT_CARD' in last or 'Insufficient Funds' in last or 'Payment Successful' in last or 'Charged ✅' in last or 'Insufficient funds' in last or 'Approved' in last or 'funds' in last or 'succeeded' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @BINAR9')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()

	


@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='KAHIN-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>╠═══════════════════════════╣
𓆩𝐊𝐞𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝𓆪
                       🌹💸	
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>/redeem {pas}</code>
</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
	
@bot.message_handler(commands=["users"])
def list_users(message):
    # پشکنین کا ئایا ئەو کەسێ فەرمانێ لێدەت ئەدمینە یان نە
    if message.from_user.id != admin:
        return
    
    try:
        # خواندنا فایلێ داتایان
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}

        if not data:
            bot.reply_to(message, "<b>📭 لیستا بەکارهێنەران بەتاڵە.</b>")
            return

        user_list = "<b>👥 لیستا ناسنامەیێن ئەندامان:</b>\n\n"
        count = 0
        
        for key in data:
            # پشکنین کا ئایا ئەڤ کلیلە ژمارەیە (ئەو ژمارە ناسنامەیا بەکارهێنەرییە)
            if key.isdigit():
                count += 1
                plan = data[key].get('plan', 'FREE')
                user_list += f"{count}- ID: <code>{key}</code> | Plan: {plan}\n"
        
        if count == 0:
            bot.reply_to(message, "<b>⚠️ چ بەکارهێنەرەک نەهاتە دیتن.</b>")
        else:
            user_list += f"\n<b>Total Users: {count}</b>"
            bot.reply_to(message, user_list)
            
    except Exception as e:
        bot.reply_to(message, f"<b>❌ Error: {str(e)}</b>")


@bot.message_handler(commands=["del"])
def delete_vip(message):
    # تەنێ ئەدمین دشێت ڤێ فەرمانێ بکاربینیت
    if message.from_user.id != admin:
        return
    
    try:
        # وەرگرتنا ID ژ نامەیێ
        args = message.text.split(' ')
        if len(args) < 2:
            bot.reply_to(message, "<b>⚠️ تکایە ID بنڤیسە، نموونە:\n<code>/del 12345678</code></b>")
            return
        
        target_id = args[1].strip()

        # خواندنا داتایان
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}

        # پشکنین کا ئایا ئەڤ ناسنامەیە هەیا یان نە
        if target_id in data:
            # گوهۆڕینا پلانا وی بۆ FREE و ڕەشکرنا تایمەری
            data[target_id]['plan'] = '𝗙𝗥𝗘𝗘'
            data[target_id]['timer'] = 'none'
            
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
                
            bot.reply_to(message, f"<b>✅ بەکارهێنەر <code>{target_id}</code> ب سەرکەفتیانە ژ لیستا VIP هاتە لادان.</b>")
        else:
            bot.reply_to(message, f"<b>❌ ببورە، ناسنامەیا <code>{target_id}</code> د داتابەیسێ دا نەهاتە دیتن!</b>")
            
    except Exception as e:
        bot.reply_to(message, f"<b>❌ Error: {str(e)}</b>")


# --- فەرمانا دروستکرنا کلیلێ (تەنێ بۆ ئەدمینی) ---
@bot.message_handler(commands=["gen"])
def generate_key(message):
    if message.from_user.id != admin:
        return
    try:
        args = message.text.split(' ')
        days = int(args[1]) if len(args) > 1 else 30
        chars = string.ascii_uppercase + string.digits
        random_part = "".join(random.choices(chars, k=12))
        key = f"BINAR-{random_part[0:4]}-{random_part[4:8]}-{random_part[8:12]}"
        
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except:
            data = {}

        data[key] = {"plan": "VIP", "days": days}
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        bot.reply_to(message, f"<b>✅ کلیل بۆ {days} ڕۆژان هاتە دروستکرن:\n\n<code>/redeem {key}</code></b>")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

# --- فەرمانا ئەکتیڤکرنا کلیلێ ---
@bot.message_handler(commands=["redeem"])
def redeem_handler(message):
    user_id = str(message.from_user.id)
    try:
        args = message.text.split(' ')
        if len(args) < 2:
            bot.reply_to(message, "<b>⚠️ تکایە کلیلێ بنڤیسە: <code>/redeem BINAR-XXXX</code></b>")
            return
        
        key = args[1].strip()
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except:
            data = {}

        if key in data and "plan" in data[key]:
            plan_type = data[key]["plan"]
            days = int(data[key].get("days", 30))
            expiry_date = datetime.now() + timedelta(days=days)
            timer_str = expiry_date.strftime("%Y-%m-%d %H:%M")

            data[user_id] = {"plan": plan_type, "timer": timer_str}
            del data[key] # ژێبرنا کلیلێ پشتی بکارئینانێ

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            bot.reply_to(message, f"<b>✅ ئەشتراکێ تە ئەکتیڤ بوو!\n🌟 پلان: {plan_type}\n⏳ ماوە: {days} ڕۆژ\n📅 ب سەرچوون: {timer_str}</b>")
        else:
            bot.reply_to(message, "<b>❌ ئەڤ کلیلە خەلەتە یان پێشتر هاتیە بکارئینان!</b>")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

# --- فەرمانا پشکنینا کارتی (تەنێ بۆ VIP) ---

@bot.message_handler(commands=["chk"])
def chk_handler(message):
    user_id = str(message.from_user.id)
    
    # 1. خواندنا داتایان بۆ پشکنینا VIP
    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
    except:
        json_data = {}

    user_info = json_data.get(user_id, {})
    if user_info.get('plan') != 'VIP':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="✨ BUY VIP ✨", url="https://t.me/BINAR9"))
        bot.reply_to(message, "<b>❌ ئەڤ فەرمانە تەنێ بۆ ئەندامێن VIP یە!</b>", reply_markup=keyboard)
        return

    # 2. وەرگرتنا کارتی ژ نامەیێ
    try:
        args = message.text.split(' ')
        if len(args) < 2:
            bot.reply_to(message, "<b>⚠️ نموونە: <code>/chk 400011|01|25|000</code></b>")
            return
            
        cc = args[1].strip()
        msg = bot.reply_to(message, "<b>Wait... Checking Card 💳</b>")
        
        # 3. وەرگرتنا زانیاریێن BIN (Bank, Country, Info)
        try:
            bin_res = requests.get(f"https://lookup.binlist.net/{cc[:6]}").json()
            bank = bin_res.get('bank', {}).get('name', 'Unknown')
            country = bin_res.get('country', {}).get('name', 'Unknown')
            flag = bin_res.get('country', {}).get('emoji', '🌍')
            scheme = bin_res.get('scheme', 'Unknown')
            type_card = bin_res.get('type', 'Unknown')
        except:
            bank = country = flag = scheme = type_card = "Unknown"

        # 4. پشکنینا کارتی ب ڕێکا Gateway
        start_time = time.time()
        gate_res = brn6(cc) # بانگکرنا فۆنکشنا gatet
        taken = round(time.time() - start_time, 2)

        # 5. دیارکرنا Status و نیشانان وەک وێنەی
        if "Approved" in gate_res:
            status = "Approved. !! ✅"
            response_msg = "100: Approved."
        else:
            status = "Declined ❌"
            response_msg = "Your card was declined."

        # 6. دارشتنا نامەیێ ڕێک وەک وێنەیێ تە نیشان دای
        final_msg = f"""<b>
CC : <code>{cc}</code>
Status : {status}
Response : {response_msg}
Gate : Stripe 0$

Info : {scheme.upper()} - {type_card.upper()}
Bank : {bank}
Country : {country.upper()} - [{flag}]

T/t : {taken}s
User : {message.from_user.first_name}
</b>"""
        
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=final_msg)
        
    except Exception as e:
        bot.reply_to(message, f"<b>❌ Error: {str(e)}</b>")


@bot.message_handler(commands=["broadcast"])
def broadcast(message):
    # پشکنینا ئەدمینی
    if message.from_user.id != admin:
        return

    # جوداکرنا نامەیێ ژ فەرمانێ
    msg_text = message.text.replace('/broadcast', '').strip()
    
    if not msg_text:
        bot.reply_to(message, "<b>⚠️ تکایە نامەیەکێ ل تەنشت فەرمانێ بنڤیسە.\nنموونە: <code>/broadcast سلاڤ</code></b>")
        return

    # خواندنا داتایان
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except:
        bot.reply_to(message, "<b>❌ فایلێ داتایان نەهاتە دیتن!</b>")
        return

    send_msg = bot.reply_to(message, "<b>⏳ نامە دهێتە هنارتن بۆ هەمییان...</b>")
    
    count = 0
    failed = 0
    
    for user_id in data:
        if user_id.isdigit():
            try:
                bot.send_message(user_id, f"<b>📢 ئاگەهداری ژ لایێ ئەدمینی:\n\n{msg_text}</b>")
                count += 1
                # راوەستانەکا بچویک دا بۆت لۆک نەبیت (Spam protection)
                time.sleep(0.3) 
            except:
                failed += 1
                continue

    bot.edit_message_text(chat_id=message.chat.id, message_id=send_msg.message_id, 
                         text=f"<b>✅ پرۆسە ب دوماهی هات\n\n🟢 گەهشتە: {count} کەسان\n🔴 سەرنەکەفت: {failed} (بۆت بلۆک کریە)</b>")







# --- دەستپێکرنا بۆتی ---
print("Bot Start On ✅ ")
bot.infinity_polling()
import telebot

# --- O'Z TOKENINGIZNI BU YERGA QO'YING ---
TOKEN = '8211952773:AAGMw1HOk2mjWL9RSpHpvsESUuQpjFI2UxE'
# ----------------------------------------

bot = telebot.TeleBot(TOKEN)

# /start buyrug'iga javob
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 
                     "Assalomu alaykum! Men siz yuborgan har qanday faylning (rasm, video, hujjat) "
                     "Telegram File ID'sini ko'rsatib beraman. \n\n"
                     "Iltimos, menga faylni yuboring yoki biron kanaldan Forward qiling.")

# Fayl turlarini (video, rasm, hujjat) ushlab oluvchi funksiya
@bot.message_handler(content_types=['video', 'document', 'photo', 'audio'])
def handle_file_id_request(message):
    
    file_id = None
    file_type = ""
    
    if message.video:
        file_id = message.video.file_id
        file_type = "🎬 Video File ID"
    elif message.document:
        file_id = message.document.file_id
        file_type = "📄 Hujjat (Document) File ID"
    elif message.photo:
        # Eng yuqori sifatli rasmning ID'sini olamiz
        file_id = message.photo[-1].file_id 
        file_type = "🖼️ Rasm (Photo) File ID"
    elif message.audio:
        file_id = message.audio.file_id
        file_type = "🎵 Audio File ID"

    if file_id:
        # Formatni foydalanuvchi osongina nusxalashi uchun Markdown formatida yuboramiz
        response_text = (f"✅ **{file_type}** topildi:\n\n"
                         f"**ID:** `{file_id}`\n\n"
                         "Bu IDni o'z botlaringizda bemalol ishlating.")
                         
        bot.reply_to(message, response_text, parse_mode='Markdown')
    else:
        # Barcha fayl tiplari qo'shilgan, lekin baribir xato bo'lsa
        bot.reply_to(message, "Kechirasiz, bu turdagi fayl ID'sini topa olmadim.")

# Matnli xabarlarga javob
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, "Iltimos, faqat fayl (rasm, video, hujjat) yuboring, matn emas.")

print("GetFileID Bot ishga tushirildi...")
bot.polling(none_stop=True)

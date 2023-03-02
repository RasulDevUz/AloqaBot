import logging
from aiogram import Bot, Dispatcher, executor, types
mstat=0
pstat=0

BOT_TOKEN =  "6296935998:AAFwCdwG_A1ZROBTzJI2sz8Bl_XoouIqgLY"
GROUP=-1001833070083
API_TOKEN = BOT_TOKEN
keyboard = types.InlineKeyboardMarkup(row_with=1)
keyboard.add(
    types.InlineKeyboardButton(text="Javob", callable_data="javob"))
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"<a href='tg://user?id={message.from_id}'>Assalomu alaykum👋🏻</a> Bu bot orqali Admin bilan gaplasha olasiz✅ Admin iloji boricha tezroq javob berishga harakat qiladi👌🏻", parse_mode="HTML")
@dp.message_handler(content_types=['any'])
async def aloqa(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == GROUP:
            if not message.reply_to_message:
                return
            await bot.forward_message(message.reply_to_message.forward_from.id,
                                      message.chat.id,
                                      message.message_id)
        else:
            await bot.forward_message(GROUP,message.chat.id, message.message_id)
            await message.reply("Habarizgiz yuborildi✅")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

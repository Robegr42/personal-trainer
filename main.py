from openai import OpenAI
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, ChatMember
from pyrogram.raw.types.bot_command import BotCommand

bot = pyrogram.Client('PesonalTrainerLLMBot', bot_token=open('token').read())

LM_client = OpenAI(base_url="url", api_key="api_key")

USER_PROMPT="""

"""

@bot.on_message(filters.command(['start'])) 
def send_welcome(client: Client, message: Message):
    bot.send_message(
        message.chat.id,
        '🖖 Hi! Welcome to your Personal Trainer Bot\nHow can I help you ',
        disable_web_page_preview=True
    )

@bot.on_message()
def general_answer(client: Client, message: Message):
    ans = completion = LM_client.chat.completions.create(
    model="TheBloke/stablelm-zephyr-3b-GGUF",
    messages=[
        {"role": "system", "content": USER_PROMPT},
        {"role": "user", "content": message.text}
    ],
    temperature=0.7,
    )
    bot.send_message(
        message.chat.id,
        completion.choices[0].message.content,
        disable_web_page_preview=True
    )

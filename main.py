from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random
import os

PHOTO_LINK = [
 "https://telegra.ph/file/4a842ee4ee51732835c57.jpg",
 "https://telegra.ph/file/4a842ee4ee51732835c57.jpg"
]

Muhammed=Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)


@Muhammed.on_message(filters.command("start")) 
async def start_message(bot, message):
    button = [[
            InlineKeyboardButton("Mo Tech YT", callback_data="start")
            ]]
    await message.reply_photo(
        photo=random.choice(PHOTO_LINK),
        caption=f"Hello {message.from_user.mention}   Bro Sugamano",
        reply_markup=InlineKeyboardMarkup(button)
    )


@Muhammed.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "start":
        await message.message.edit(
            text=f" hello {msg.from_user.mention}  Start Text"
        )


Muhammed.run()


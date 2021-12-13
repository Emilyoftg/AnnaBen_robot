"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from Script import script
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "എന്നെ ചീത്ത വിളിക്കു... വേണമെങ്കിൽ നല്ല ഇടി ഇടിക്കു... പക്ഷെ ഉപദേശിക്കരുത്....." 
HELP = "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ...."
REPO = "നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ..."
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)

@Client.on_message(filters.command("help"))
async def help(client, message):
        buttons = [[
            InlineKeyboardButton('Filters', callback_data='auto_manual'),
            InlineKeyboardButton('Connection', callback_data='coct'),
            InlineKeyboardButton('Misc', callback_data='info')
            ],[
            InlineKeyboardButton('Fun', callback_data='fun'),
            InlineKeyboardButton('Song', callback_data='song'),
            InlineKeyboardButton('Tgraph', callback_data='tgraph')
            ],[
            InlineKeyboardButton('PIN', callback_data='pin'),
            InlineKeyboardButton('Json', callback_data='json'),
            InlineKeyboardButton('Bans', callback_data='restric')
            ],[
            InlineKeyboardButton('Back', callback_data='start'), 
            InlineKeyboardButton('Status', callback_data='stats'),
            InlineKeyboardButton('Inactive', callback_data='zombies')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)

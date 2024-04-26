# (c) @AbirHasan2005

import asyncio
from config import Config
import pyrogram
from pyrogram import Client,filters, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(c: Client, m: Message):
    try:
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        invite_link1 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL1) if Config.UPDATES_CHANNEL1.startswith("-100") else Config.UPDATES_CHANNEL1))
        invite_link2 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL2) if Config.UPDATES_CHANNEL2.startswith("-100") else Config.UPDATES_CHANNEL2))
        invite_link3 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL3) if Config.UPDATES_CHANNEL3.startswith("-100") else Config.UPDATES_CHANNEL3))
        invite_link4 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL4) if Config.UPDATES_CHANNEL4.startswith("-100") else Config.UPDATES_CHANNEL4))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        invite_link1 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL1) if Config.UPDATES_CHANNEL1.startswith("-100") else Config.UPDATES_CHANNEL1))
        invite_link2 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL2) if Config.UPDATES_CHANNEL2.startswith("-100") else Config.UPDATES_CHANNEL2))
        invite_link3 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL3) if Config.UPDATES_CHANNEL3.startswith("-100") else Config.UPDATES_CHANNEL3))
        invite_link4 = await c.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL4) if Config.UPDATES_CHANNEL4.startswith("-100") else Config.UPDATES_CHANNEL4))
    except Exception as err:
        print(f"Unable to create invite links for channels: {Config.UPDATES_CHANNEL}, {Config.UPDATES_CHANNEL1}, {Config.UPDATES_CHANNEL2}, {Config.UPDATES_CHANNEL3}, {Config.UPDATES_CHANNEL4}\n\nError: {err}")
        await c.send_message(
            chat_id=m.from_user.id,
            text="Something went wrong. Contact my admin.",
            disable_web_page_preview=True,
            parse_mode="Markdown",
        )
        return 400
    
    try:
        user = await c.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=m.from_user.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=m.from_user.id,
                text="Sorry sir, you are banned to use me. Contact my admin for Updates Channel.",
                disable_web_page_preview=True,
                parse_mode="Markdown",
            )
            return 400
    except Exception as e:
        print(f"Error checking user status for Updates Channel: {e}")
        
    try:
        user = await c.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL1) if Config.UPDATES_CHANNEL1.startswith("-100") else Config.UPDATES_CHANNEL1), user_id=m.from_user.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=m.from_user.id,
                text="Sorry sir, you are banned to use me. Contact my admin for Updates Channel 1.",
                disable_web_page_preview=True,
                parse_mode="Markdown",
            )
            return 400
    except Exception as e:
        print(f"Error checking user status for Updates Channel 1: {e}")
        
    # Repeat the same for other channels
    
    try:
        await c.send_message(
            chat_id=m.from_user.id,
            text="**Please join my updates channels to use this bot!**\n\nOnly channel subscribers can use the bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link),
                        InlineKeyboardButton("🤖 Join Updates Channel 1", url=invite_link1.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel 2", url=invite_link2.invite_link),
                        InlineKeyboardButton("🤖 Join Updates Channel 3", url=invite_link3.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel 4", url=invite_link4.invite_link),
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshFsub")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await c.send_message(
            chat_id=m.from_user.id,
            text="Something went wrong. Contact my admin.",
            disable_web_page_preview=True,
            parse_mode="Markdown",
        )
        return 400

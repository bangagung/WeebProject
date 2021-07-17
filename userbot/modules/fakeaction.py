# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
#from userbot.utils import admin_cmd
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai Pengetikan Palsu Untuk {t} Detik.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai rekaman audio palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai Perekaman Video Palsu Untuk {t} Detik.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah Salah.`")
    await event.edit(f"`Mulai Bermain Game Palsu Untuk {t} Detik.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


CMD_HELP.update({
    "fakeaction": "✘ Pʟᴜɢɪɴ : Fake Action\
    \n\n⚡𝘾𝙈𝘿⚡: `.ftyping`\
    \n↳ : Seolah-olah Anda Sedang Mengetik Di Dalam Group, Padahal Tidak.\
    \n\n⚡𝘾𝙈𝘿⚡: `.faudio`\
    \n↳ : Seolah-olah Anda Sedang Mengirim Audio Di Dalam Group, Padahal Tidak.\
    \n\n⚡𝘾𝙈𝘿⚡: `.fvideo`\
    \n↳ : Seolah-olah Anda Sedang Mengirim Video Di Dalam Group, Padahal Tidak.\
    \n\n⚡𝘾𝙈𝘿⚡: `.fgame`\
    \n↳ : Seolah-olah Anda Sedang Memainkan Game Di Dalam Group, Padahal Tidak."})

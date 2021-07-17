import asyncio
from time import sleep

from telethon import events

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.sayang$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("I LOVEE YOUUU 💕")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💗💕")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG KAMU 💝💖💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SELAMANYA 💕")
        await e.edit("💘💘💘💘")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("I LOVE YOUUUU")
        await e.edit("MY BABY")
        await e.edit("💕💞💘💝")
        await e.edit("💘💕💞💝")
        await e.edit("SAYANG KAMU💞")


@register(outgoing=True, pattern='^\.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  *Terimakasih`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Canda   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^\.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong Hiyahiyahiya`")


@register(outgoing=True, pattern="^.dino(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`🧎🦖`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@register(outgoing=True, pattern="^.gabut$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
        await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
        await e.edit("`RAMBUUUT WARNAAA WARNII`")
        await e.edit("`BAGAI GULALI`")
        await e.edit("`IMUUUTTTTT LUCUUU`")
        await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
        await e.edit("`GW GABUUTTTT`")
        await e.edit("`EMMMM BACOTNYA`")
        await e.edit("`GABUTTTT WOI GABUT`")
        await e.edit("🙈🙈🙈🙈")
        await e.edit("🙉🙉🙉🙉")
        await e.edit("🙈🙈🙈🙈")
        await e.edit("🙉🙉🙉🙉")
        await e.edit("`CILUUUKKK BAAAAA`")
        await e.edit("🙉🙉🙉🙉")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢           🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🚶                                 🐢")
        await e.edit("`AHHH MANTAP`")
        await e.edit("🙉")
        await e.edit("🙈")
        await e.edit("🙉")
        await e.edit("🙈")
        await e.edit("🙉")
        await e.edit("😂")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢           🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢           🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢           🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("`GABUT`")


@register(outgoing=True, pattern="^.terkadang(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@register(outgoing=True, pattern="^.mf$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            f"`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You 💞`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^.gombal(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai, I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💕💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💗💞`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💝💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💟💖`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💘💓`")
    sleep(1)
    await typew.edit("`Muaacchhh`")


# Create by myself @localheart

CMD_HELP.update(
    {
        "animasi1": "`.gabut` ; `.dino`\
    \nUsage: ntahlah gabut doang.\
    \n\n`.gombal` ; `.nah` ; `.huh`\
    \nUsage: buat bercanda\
    \n\n`.ceritacinta`\
    \nUsage: lihat sendiri\
    \n\n`.cinta`\
    \nUsage: mengirim cintamu ke seseorang.\
    \n\n`.sayang`\
    \nUsage: untuk jadi buaya.\
    \n\n`.terkadang`\
    \nUsage: Auk dah iseng doang."
    }
)

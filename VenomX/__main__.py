import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VenomX import LOGGER, app, userbot
from VenomX.core.call import Ayush
from VenomX.misc import sudo
from VenomX.plugins import ALL_MODULES
from VenomX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VenomX.plugins" + all_module)
    LOGGER("VenomX.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Ayush.start()
    try:
        await Ayush.stream_call("https://te.legra.ph/file/774624c731c7b51b09a6b.mp4")
    except NoActiveGroupCall:
        LOGGER("VenomX").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Ayush.decorators()
    LOGGER("VenomX").info("ᴀɴᴊᴀʟɪ ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴏᴡ ᴇɴᴊᴏʏ")

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("VenomX").info("Stopping Anjali Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

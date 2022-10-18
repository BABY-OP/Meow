import asyncio
from pytgcalls import idle
from config import call_py, app
from config import (app, hl, TIMEZONE, LOGS_CHANNEL, MONGO_DB, SUDO_USERS, call_py )


async def main():
    print("STARTING  CLIENT")
    await app.start()
    print("STARTING PYTGCALLS CLIENT")
    await call_py.start()
    print(
        """
    ------------------------
   | Meow Actived! |
    ------------------------
"""
    )
    await idle()
    await pidle()
    print("STOPPING USERBOT")
    await app.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())







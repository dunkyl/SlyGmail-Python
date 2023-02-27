import sys, asyncio, inspect

from SlyGmail.gmail import Scope
from SlyAPI.flow import *

async def main(args: list[str]):

    match args:
        case ['grant']:
            await grant_wizard(Scope, kind='OAuth2')
        case ['scaffold']:
            scaffold_wizard(kind='OAuth2')
        case _: # help
            print(inspect.cleandoc("""
            SlyGmail command line: tool for Gmail OAuth2.
            Usage:
                SlyGmail [scaffold|grant]
                Same as SlyAPI, but scopes are listed in a menu.
            """))

if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:]))
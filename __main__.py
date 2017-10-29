#!/usr/bin/env python3
import asyncio
from reader import market_data
from periodic import Periodic

@asyncio.coroutine
async def main():
    """Main Of the Agent"""
    p = Periodic(lambda: market_data(), 1)
    try:
        print('Updating Market Data')
        await p.start()
        await asyncio.sleep(3.1)
        #await p._run()

    finally:
        print('Finally')
       # await p.stop()  # we should stop task finally


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

try:

    loop.run_until_complete(main())
    loop.run_forever()

finally:

    print('closing event loop')
    loop.close()
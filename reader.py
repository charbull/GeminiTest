#!/usr/bin/env python3
import asyncio
import json
import websockets


async def market_data():
    """Returns the latest market data"""
    async with websockets.connect('wss://api.gemini.com/v1/marketdata/ethusd') as websocket:
        var_eth_usd_price = await websocket.recv()
        data = json.loads(var_eth_usd_price)
        var_type = data["type"]
        print("{}".format(var_eth_usd_price))
        print("--\n"+var_type)

asyncio.get_event_loop().run_until_complete(market_data())

#!/usr/bin/env python3
import asyncio
import json
import datetime
import websockets


@asyncio.coroutine
async def market_data():
    """Returns the latest market data"""
    timestampms = []
    async with websockets.connect('wss://api.gemini.com/v1/marketdata/ethusd') as websocket:
        var_eth_usd_price = await websocket.recv()
        if var_eth_usd_price:
            data = json.loads(var_eth_usd_price)
            if 'timestampms' in data:
                timestampms = data["timestampms"]

            events_array = data["events"]
            if events_array:
                var_last_item = events_array[len(events_array)-1]
                var_type = var_last_item["type"]
                var_reason = var_last_item["reason"]
                var_price = var_last_item["price"]
                var_delta = var_last_item["delta"]
                var_remaining = var_last_item["remaining"]
                var_side = var_last_item["side"]
                print("====> Lastest Transaction:\n"+
                      "-- Type: "+str(var_type)+"\n"+
                      "-- Reason: "+str(var_reason)+"\n"+
                      "-- Price: "+str(var_price)+"\n"+
                      "-- Delta: "+str(var_delta)+"\n"+
                      "-- Remaining: "+str(var_remaining)+"\n"+
                      "-- Side: "+str(var_side)+"\n"+
                      "-- Trader Retrieval Time "+str(datetime.datetime.now()))
                if timestampms:
                    print("-- Gemini Time "+str(timestampms))
        else:
            print("Something went wrong while reading the marketdata")


asyncio.get_event_loop().run_until_complete(market_data())

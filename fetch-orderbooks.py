import asyncio
import ccxt
import ccxt.async_support as ccxta
import time
import os
import sys

import numpy as np


async def async_client(symbol):
    client = ccxta.binance({
        'timeout': 30000,
        'enableRateLimit': True
    })
    
    await client.load_markets()
    
    # print(len(client.symbols))
    
    if symbol not in client.symbols:
        raise Exception('binance does not support symbol ' + symbol)
    
    old_data = await client.fetch_ohlcv(symbol, '1d')
    print(np.array(old_data).shape)
    
    await client.close()


if __name__ == '__main__':

    # Consider review request rate limit in the methods you call
    symbol = 'ETH/BTC'

    asyncio.get_event_loop().run_until_complete(async_client(symbol))


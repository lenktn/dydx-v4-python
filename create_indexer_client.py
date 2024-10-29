import asyncio

from dydx_v4_client.indexer.rest.indexer_client import IndexerClient

# Инициализация клиента (создание экземпляра класса, который будет использоваться для взаимодействия с API)
host = 'https://indexer.dydx.trade'
client = IndexerClient(host)

# Получение информации о рынках
async def get_markets():
    # Получение информации о рынках
    markets_response = await client.markets.get_perpetual_markets()
    print(markets_response)

async def get_market_orderbook():
    markets_response = await client.markets.get_perpetual_markets("AVAX-USD")
    print(markets_response)

async def get_market_trades():
    markets_response = await client.markets.get_perpetual_market_trades("BTC-USD")
    print(markets_response)

async def main():
    await get_market_trades()

if __name__ == "__main__":
    asyncio.run(main())


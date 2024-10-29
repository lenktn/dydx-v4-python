import json
import asyncio
from dydx_v4_client.indexer.socket.websocket import IndexerSocket

def on_message(ws, message):
    print(f"Received message: {message}")

    # Обработка полученного сообщения (например, проверка на сделки или обновления ордербука)
    data = json.loads(message)

    if data['channel'] == 'v4_trades':
        # Обработка данных сделок
        handle_trade(data)

def handle_trade(data):
    # Логика обработки сделки
    print("Trade executed:", data)

def on_open(ws):
    print("WebSocket connection opened")

    # Подписка на канал ордербука для BTC-USD
    ws.order_book.subscribe(id='BTC-USD')
    # Подписка на канал сделок для BTC-USD
    ws.trades.subscribe(id='BTC-USD')

async def main():
    # Создание экземпляра WebSocket
    ws = IndexerSocket(
        url='wss://api.dydx.exchange/v4/ws',
        on_open=on_open,
        on_message=on_message,
    )

    # Запуск WebSocket
    try:
        await ws.connect()
    except Exception as e:
        print(f"Error connecting to WebSocket: {e}")

# Запуск основного асинхронного цикла
asyncio.run(main())

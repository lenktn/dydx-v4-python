import time
import json

from dydx_v4_client.indexer.socket.websocket import IndexerSocket

# Ваши API ключи для dYdX
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
API_PASSPHRASE = 'YOUR_API_PASSPHRASE'


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


# Создание экземпляра WebSocket
ws = IndexerSocket(
    url='wss://api.dydx.exchange/v4/ws',
    on_open=on_open,
    on_message=on_message,
)

# Запуск WebSocket
try:
    ws.connect()
except Exception as e:
    print(f"Error connecting to WebSocket: {e}")

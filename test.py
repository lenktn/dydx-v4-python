import time
from dydx_v4_client.python import Client

# Инициализация клиента
client = Client(
    host='https://api.dydx.exchange',
    api_key='YOUR_API_KEY',
    api_secret='YOUR_API_SECRET',
    passphrase='YOUR_PASSPHRASE',
    stark_private_key='YOUR_STARK_PRIVATE_KEY'
)

# Аутентификация
client.authenticate()

# Получение информации о рынках
markets = client.public.get_markets()
print(markets)

# Получение информации о текущих ордерах
orders = client.private.get_orders()
print(orders)

# Создание нового ордера
order_params = {
    'market': 'BTC-USD',
    'side': 'BUY',
    'order_type': 'LIMIT',
    'post_only': False,
    'size': '0.01',
    'price': '50000.0',
    'limit_fee': '0.015',
    'expiration_epoch_seconds': int(time.time()) + 60 * 60,
}
order = client.private.create_order(order_params)
print(order)

from typing import Optional

from .constants import DEFAULT_API_TIMEOUT
from .modules.account import AccountClient
from .modules.markets import MarketsClient
from .modules.status import StatusClient


class IndexerClient:
    """
    Client for Indexer
    """

    def __init__(self, host: str, api_timeout: Optional[float] = None):
        api_timeout = api_timeout or DEFAULT_API_TIMEOUT
        self._markets = MarketsClient(host, api_timeout)
        self._account = AccountClient(host, api_timeout)
        self._status = StatusClient(host, api_timeout)

    # Создаются три внутренних клиента: для рынков, аккаунтов и статуса системы
    @property
    def markets(self) -> MarketsClient:
        """
        Возвращает клиента для работы с публичными API (например, получение информации о рынках).
        """
        return self._markets

    @property
    def account(self) -> AccountClient:
        """
        Возвращает клиента для работы с приватными API (например, информация об аккаунте пользователя).
        """
        return self._account

    @property
    def utility(self) -> StatusClient:
        """
        Возвращает клиента для получения системной информации (например, статус сервера).
        """
        return self._status

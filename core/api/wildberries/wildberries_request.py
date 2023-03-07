from abc import ABC, abstractmethod
import aiohttp
import asyncio


class RequestMaker(ABC):

    @abstractmethod
    async def _make_request_async(self):
        raise NotImplementedError()

    @abstractmethod
    def make_request(self):
        raise NotImplementedError()


class WildberriesRequestAsync(RequestMaker):

    def __init__(self, formatted_url: str = None):
        self._url = formatted_url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, formatted_url: str):
        if isinstance(formatted_url, str):
            self._url = formatted_url
        else:
            raise ValueError('Url should be str')

    async def _make_request_async(self):
        if self.url:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, timeout=0.5) as response:
                    return await response.json()
        else:
            raise ValueError('Url cannot be None')

    def make_request(self) -> str:
        response_result = asyncio.run(self._make_request_async())

        return response_result

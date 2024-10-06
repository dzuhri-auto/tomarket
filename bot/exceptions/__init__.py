from aiohttp.client_exceptions import ClientResponseError


class InvalidSession(BaseException): ...


class CustomClientResponseError(ClientResponseError):
    def __str__(self) -> str:
        return "{}, message={!r}".format(
            self.status,
            self.message,
        )


class InvalidApiKey(BaseException):
    pass


class ExpiredApiKey(BaseException):
    pass


class MissingApiKeyException(BaseException):
    pass


class InvalidApiKeyException(BaseException):
    pass


class ExpiredApiKeyException(BaseException):
    pass

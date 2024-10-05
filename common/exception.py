from __future__ import annotations

import typing

if typing.TYPE_CHECKING:  # pragma: no cover
    SingleErrorMessage = str
    ErrorMessage = SingleErrorMessage | list[SingleErrorMessage]
    FieldName = str
    ErrorsDict = dict[FieldName, ErrorMessage]


class BusinessLogicException(Exception):
    def __init__(
            self,
            message: ErrorMessage | ErrorsDict | BusinessLogicException | Exception | None = None,
            code: str | None = None,
    ):
        if message is None:
            message = 'Что-то пошло не так, обратитесь в поддержку.'
        super().__init__(message, code)
        self.code = code
        self.message: ErrorMessage | ErrorsDict = message

    def __str__(self) -> str:
        return str(self.message)

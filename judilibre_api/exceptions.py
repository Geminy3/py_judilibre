class JudilibreInvalidRequestError(Exception):
    pass

class JudilibreInvalidCredentialsError(Exception):
    pass

class JudilibreUnauthorizedError(Exception):
    pass

class JudilibreResourceNotFoundError(Exception):
    pass

class JudilibreSuspiciousActivityError(Exception):
    pass

class JudilibreTooManyRequestError(Exception):
    pass

class JudilibreInternalError(Exception):
    pass

ERROR_CODES_TO_EXCEPTIONS = {
    400: JudilibreInvalidRequestError,
    401: JudilibreInvalidCredentialsError,
    403: JudilibreUnauthorizedError,
    404: JudilibreResourceNotFoundError,
    423: JudilibreSuspiciousActivityError,
    429: JudilibreTooManyRequestError,
    500: JudilibreInternalError,
}
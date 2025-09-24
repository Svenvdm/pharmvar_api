class PharmVarApiException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidArgumentError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoDataFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ParameterValidationError(PharmVarApiException):
    """Exception raised when parameter validation fails"""
    def __init__(self, parameter: str, value: any, message: str):
        self.parameter = parameter
        self.value = value
        self.message = message
        super().__init__(f"{message}")
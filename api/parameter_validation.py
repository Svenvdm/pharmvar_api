from functools import wraps
from enums.enums import ValidationRule
from exceptions.exceptions import ParameterValidationError

# Decorator for parameter validation
def validate_parameters(function):
    """
    Decorator to validate parameters passed to the API request.

    """
    @wraps(function)
    def wrapper(*args, **kwargs):

        # Check if 'params' is in kwargs
        if "params" not in kwargs:
            return function(*args, **kwargs)  # No params to validate, just call the function
            
        params = kwargs["params"]
        clean_params = {k: v for k, v in params.items() if v is not None}

        for param_name, param_value in clean_params.items():
            if param_name in ValidationRule.get_rule_parameters():
                rule = ValidationRule.get_rule(param_name)
                # Check against valid values list if provided
                if "valid_values" in rule and param_value not in rule["valid_values"]:
                    raise ParameterValidationError(parameter=param_name, value=param_value, message=rule["error_message"])
                
                # Run custom validator function if provided
                if "validator" in rule and param_value is not None:
                    if not rule["validator"](param_value):
                        raise ParameterValidationError(parameter=param_name, value=param_value, message=rule["error_message"])
        # Call the original function if all validations pass
        return function(*args, **kwargs)
                    
    return wrapper

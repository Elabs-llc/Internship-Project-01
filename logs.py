import time
import logging

logging.basicConfig(
    level=logging.INFO, 
    filename='logs.log', 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)
"""
Logging configuration:
This configuration sets up the logging to capture log messages at the INFO level and above.
The logs are saved in 'logs.log' in write mode (overwriting each time the program runs).
The log messages include timestamps, log levels, and message content.
"""

def log_execution_time(func):
    """
    A decorator that logs the execution time of the decorated function.

    This decorator calculates the time taken for a function to execute, logs the function's 
    name along with the execution time in seconds to the 'logs.log' file, and then returns 
    the function's result.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: A wrapper function that logs the execution time and calls the original function.
    
    Example:
        @log_execution_time
        def some_function():
            # Function code here
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def log_message(message):
    """
    A decorator factory that logs a custom message along with the result of the decorated function.

    This decorator factory allows specifying a custom message to log when the decorated 
    function is executed. It logs the message along with the function name and its return 
    value to the 'logs.log' file.

    Parameters:
    message (str): A custom message to include in the log.

    Returns:
    function: A decorator that logs the specified message, the function name, and its result.
    
    Example:
        @log_message("Processing completed")
        def some_function():
            # Function code here
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logging.info(f"{message}: Function {func.__name__} returned: {result}")
            return result
        return wrapper
    return decorator

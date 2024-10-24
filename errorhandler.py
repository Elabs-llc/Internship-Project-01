import time
import requests
from functools import wraps

def retry_on_failure(retries=3, delay=2):
    """
    A decorator to retry a function in case of a requests.RequestException.
    
    Args:
        retries (int): Number of retry attempts.
        delay (int): Delay (in seconds) between retries.

    Returns:
        Wrapper function that retries the decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    print(f"Error occurred: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempts += 1
            return None  # Return None if all attempts fail
        return wrapper
    return decorator

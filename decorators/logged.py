"""Helper to switch on and off logging of decorated functions."""

import functools

LOGGING = False


def logged(func):
    """Log with a decorator."""

    @functools.wraps(func)
    def _logged(*args, **kwargs):
        """Take the function arguments."""
        if LOGGING:
            print('logged')  # do proper logging here
        return func(*args, **kwargs)

    return _logged

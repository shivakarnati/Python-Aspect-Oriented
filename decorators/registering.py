"""A function registry."""

import functools

registry = {}


def register_at_call(name):
    """Register the decorated function at call time."""

    def _register(func):
        """Take the function."""

        @functools.wraps(func)
        def __register(*args, **kwargs):
            """Take the function arguments."""
            registry.setdefault(name, []).append(func)
            return func(*args, **kwargs)

        return __register

    return _register


def register_at_def(name):
    """Register the decorated function at definition time."""

    def _register(func):
        """Take the function."""
        registry.setdefault(name, []).append(func)

        return func

    return _register

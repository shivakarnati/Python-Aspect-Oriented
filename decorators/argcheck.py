"""Check function arguments for given type."""

import functools


def check(*argtypes):
    """Check function argument types."""

    def _check(func):
        """Take function as argument."""

        @functools.wraps(func)
        def __check(*args):
            """Take function arguments."""
            if len(args) != len(argtypes):
                msg = f'Expected {len(argtypes)} but got {len(args)} arguments'
                raise TypeError(msg)
            for arg, argtype in zip(args, argtypes):
                if not isinstance(arg, argtype):
                    msg = f'Expected {argtypes} but got '
                    msg += f'{tuple(type(arg) for arg in args)}'
                    raise TypeError(msg)
            return func(*args)

        return __check

    return _check

"""A trap to detect what code disables the loggers.

Taken from https://stackoverflow.com/q/28694540
"""

import logging
import sys


@property
def disabled(self):
    try:
        return self._disabled
    except AttributeError:
        return False


def install_disabled_with_trace():
    """Prints the stack trace of the code that disabled the logger."""

    @disabled.setter
    def disabled(self, disabled):
        if disabled:
            frame = sys._getframe(1)
            # print(
            #     f"{frame.f_code.co_filename}:{frame.f_lineno} "
            #     f"disabled the {self.name} logger"
            # )
            from traceback import print_stack

            print_stack(frame)
        self._disabled = disabled

    logging.Logger.disabled = disabled


def install_disabled_with_source():
    """Prints the calling line of code that disabled the logger."""

    @disabled.setter
    def disabled(self, disabled):
        if disabled:
            frame = sys._getframe(1)
            print(
                f"{frame.f_code.co_filename}:{frame.f_lineno} "
                f"disabled the {self.name} logger"
            )
        self._disabled = disabled

    logging.Logger.disabled = disabled

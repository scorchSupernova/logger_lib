import logging
import sys
# from logger_lib.utils import save_log_data
from datetime import datetime


class SSLogger(logging.getLoggerClass()):
    def __init__(self, name, verbose=True, log_dir=None):
        super().__init__(name)
        self.setLevel(logging.DEBUG)

        logging.addLevelName(logging.INFO, 'FRAMEWORK')

        self.verbose = verbose

        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(logging.Formatter('%(message)s'))
        self.enable_console_output()

    def local_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')



    def has_console_handler(self):
        return len([h for h in self.handlers if type(h) == logging.StreamHandler]) > 0

    def has_file_handler(self):
        return len([h for h in self.handlers if isinstance(h, logging.FileHandler)]) > 0

    def disable_console_output(self):
        if not self.has_console_handler():
            return
        self.removeHandler(self.stdout_handler)

    def enable_console_output(self):
        if self.has_console_handler():
            return
        self.addHandler(self.stdout_handler)


    def framework(self, msg, *args, **kwargs):
        return super().info(msg, *args, **kwargs)

    def _custom_log(self, func, msg, *args, **kwargs):
        if self.verbose:
            return func(msg, *args, **kwargs)

        if not self.has_file_handler():
            return

        self.disable_console_output()
        func(msg, *args, **kwargs)
        self.enable_console_output()

    def debug(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "debug")
        mod_msg = str(self.local_time()) + " | " + str(self.name) + " | " + str(msg)
        self._custom_log(super().debug, f"\033[1;35;40m{mod_msg}", *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "info")
        mod_msg = str(self.local_time()) + " | " + str(self.name) + " | " + str(msg)
        self._custom_log(super().info, f"\033[1;32;40m{mod_msg}", *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "warning")
        mod_msg = str(self.local_time()) + " | " + str(self.name) + " | " + str(msg)
        self._custom_log(super().warning, f"\033[1;33;40m{mod_msg}", *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "error")
        mod_msg = str(self.local_time()) + " | " + str(self.name) + " | " + str(msg)
        self._custom_log(super().error, f"\033[1;31;40m{mod_msg}", *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "critical")
        mod_msg = str(self.local_time()) + " | " + str(self.name) + " | " + str(msg)
        self._custom_log(super().critical, f"\033[5;31;40m{mod_msg}\033[0;31;40m", *args, **kwargs)

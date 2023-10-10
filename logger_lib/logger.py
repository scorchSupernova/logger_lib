import logging
import sys

from logger_lib.color import Color
# from logger_lib.utils import save_log_data


class SSLogger(logging.getLoggerClass()):
    def __init__(self, name, verbose=False, log_dir=None):
        super().__init__(name)
        self.setLevel(logging.DEBUG)

        logging.addLevelName(logging.INFO, 'FRAMEWORK')

        self.verbose = verbose

        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(logging.Formatter('%(message)s'))
        self.enable_console_output()



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
        self._custom_log(super().debug, f"\033[1;35;40m{msg}", *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "info")
        self._custom_log(super().info, f"\033[1;32;40m{msg}", *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "warning")
        self._custom_log(super().warning, f"\033[1;33;40m{msg}", *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "error")
        self._custom_log(super().error, f"\033[1;31;40m{msg}", *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        # save_log_data(self.name, msg, "critical")
        self._custom_log(super().critical, f"\033[5;31;40m{msg}\033[0;31;40m", *args, **kwargs)


def test_verbose():
    print('*' * 80 + '\nVerbose logging (stdout + file)\n' + '*' * 80)
    verbose_log = SSLogger('verbose', verbose=True, log_dir='logs')

    verbose_log.critical('We now log to both stdout and a file log')
    verbose_log.debug('We now log to both stdout and a file log')
    verbose_log.error('We now log to both stdout and a file log')
    verbose_log.info('We now log to both stdout and a file log')
    verbose_log.warning('We now log to both stdout and a file log')

    msg = 'Use color in a true TTY'
    if sys.stdout.isatty():
        verbose_log.info(Color.colored(Color.LIGHTYELLOW, msg))
    else:
        verbose_log.info(msg + ', but not here')

    verbose_log.framework('We now log everywhere irrespective of verbosity')


def test_quiet():
    print('*' * 80 + '\nQuiet logging (stdout: only FRAMEWORK + file: all levels)\n' + '*' * 80)
    quiet_log = SSLogger('quiet', verbose=False, log_dir='logs')
    quiet_log.debug('We now log only to a file logsss')
    # quiet_log.debug('We now log only to a file log111')
    quiet_log.framework('We now log everywhere irrespective of verbosity')


if __name__ == '__main__':
    test_verbose()
    test_quiet()
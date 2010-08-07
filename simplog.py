"""artflog.py
A little helper to set up default kinds of logging easily.

To log to console:

    Pass get_logger a name, which probably should be the __name__
    of the calling script.

        import simplog
        logger = simplog.Simplog.logger('my_name')

"""
import os
import logging

LOG_PATH = '/tmp'


class Simplog(object):
    """Set up default logging simply."""

    @classmethod
    def logger(self, name, type='console', formatter="simple",
               log_file=None, level='debug'):
        """Return a logging object fitting specified parameters"""

        # Name
        logger = logging.getLogger(name)

        # Format
        if formatter == 'simple':
            formatter = logging.Formatter("%(name)s - %(levelname)s - "
                                          "%(message)s")

        # Handler
        if (type == 'console'):
            handler = logging.StreamHandler()
        elif (type =='file'):
            if os.path.exists(DEFAULT_LOG_DIR):
                log_file = DEFAULT_LOG_DIR + '/' + name
            else:
                raise Exception("No log_file supplied, and the "
                                "default logging directory %s does not exist."
                                 % (LOG_PATH))
            handler = logging.FileHandler(log_file)
            handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Level
        if level == 'debug':
            logger.setLevel(logging.DEBUG)
        elif level == 'info':
            logger.setLevel(logging.INFO)
        elif level == 'warn':
            logger.setLevel(logging.WARN)
        elif level == 'error':
            logger.setLevel(logging.ERROR)
        elif level == 'critical':
            logger.setLevel(logging.CRITICAL)

        return logger

    @classmethod
    def test_logger(self, logger):
        """Print one of each kind of logger message"""

        logger.debug("Simplog test_logger testing debug message")
        logger.info("Simplog test_logger testing info message")
        logger.warn("Simplog test_logger testing warn message")
        logger.error("Simplog test_logger testing error message")
        logger.critical("Simplog test_logger testing critical message")


class NullHandler(logging.Handler):
    """Swallows logging output to prevent unwanted messages. See:
    http://docs.python.org/library/logging.html"""

    def emit(self, record):
        pass

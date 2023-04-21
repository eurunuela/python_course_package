import logging

LGR = logging.getLogger("GENERAL")
RepLGR = logging.getLogger("REPORT")

def setup_loggers(logname=None, repname=None, quiet=False, debug=False):
    # Set up the general logger
    log_formatter = logging.Formatter(
        "%(asctime)s\t%(module)s.%(funcName)-12s\t%(levelname)-8s\t%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    stream_formatter = logging.Formatter(
        "%(levelname)-8s %(module)s:%(funcName)s:%(lineno)d %(message)s"
    )
    # set up general logging file and open it for writing
    if logname:
        log_handler = logging.FileHandler(logname)
        log_handler.setFormatter(log_formatter)
        LGR.addHandler(log_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)
    LGR.addHandler(stream_handler)

    if quiet:
        LGR.setLevel(logging.WARNING)
    elif debug:
        LGR.setLevel(logging.DEBUG)
    else:
        LGR.setLevel(logging.INFO)

    # Loggers for report and references
    text_formatter = logging.Formatter("%(message)s")
    if repname:
        rep_handler = logging.FileHandler(repname)
        rep_handler.setFormatter(text_formatter)
        RepLGR.setLevel(logging.INFO)
        RepLGR.addHandler(rep_handler)
        RepLGR.propagate = False


def teardown_loggers():
    for local_logger in (RepLGR, LGR):
        for handler in local_logger.handlers[:]:
            handler.close()
            local_logger.removeHandler(handler)

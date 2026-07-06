import logging as lg

lg.basicConfig(
    filename='app.log',
    level = lg.WARNING,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
lg.debug('This is a debug message')
lg.info("This is information message")
lg.warning("This is warning message")
lg.error("This is error message")
lg.critical("This is critical message")

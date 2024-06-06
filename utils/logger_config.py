import logging


def configurar_logger():
    logging.basicConfig(
        filename='log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    return logger

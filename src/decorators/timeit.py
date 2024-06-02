import time
from loguru import logger

def timeit(method):
    logger.add("nogit.run.log", format="{time} {level} {message}", level="INFO")
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()
        logger.info(f" TIME-IT **{method.__name__}** took {end_time - start_time:.2f} seconds")
        return result
    return timed
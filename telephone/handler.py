import logging
import random
import string
from pydantic import BaseSettings, Field


class Config(BaseSettings):
    mutation_count: int = Field(default=2, env="mutation_count")
    log_level: str = "INFO"


config = Config()  # type: ignore Pydantic will load values for us.


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    logging.info("handle config: %s", config)

    message = req
    for i in range(config.mutation_count):
        j = random.randint(0, len(message) - 1)
        # mutate position i with a random character
        message = message[:j] + random.choice(string.ascii_letters) + message[j + 1 :]

    return f"Hello, you said: {message}"

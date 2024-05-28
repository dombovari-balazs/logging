from src.apple_tree import produce_apple
from src.dog import bark

import logging

if __name__ == '__main__':
    # try to comment this line, logging won't work.
    logging.basicConfig(level=logging.INFO)
    produce_apple()
    bark()

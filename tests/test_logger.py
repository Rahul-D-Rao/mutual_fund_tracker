import os
import sys 
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)
sys.path.append(os.path.abspath(os.path.join(current_dir, '../src', 'services')))
from logger import setup_logger


def test_logger_setup():
    log_file = "logs/test_app.log"
    logger = setup_logger(log_file)

    logger.info("Test log message.")

    # Check if log file exists
    assert os.path.exists(log_file)

    # Clean up after test
    os.remove(log_file)
import os
import logging
from tqdm import tqdm
from typing import Callable, List, Any


# Custom handler for tqdm
class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        # Format the record
        msg = self.format(record)
        # Use tqdm.write to write the message without interfering with the progress bar
        tqdm.write(msg)

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add the custom tqdm handler to the logger
tqdm_handler = TqdmLoggingHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
tqdm_handler.setFormatter(formatter)
logger.addHandler(tqdm_handler)


def get_question_id_list(path):
    """
    Takes main file folder path and returns list of question ids present in question_id_list.txt
    :param path: main file path
    :return: List[str]
    """
    try:
        with open(os.path.join(path, 'Input Data Files', 'question_id_list.txt'), 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except:
        raise ValueError(f"Question Id list not found!!!")


def run_str_function_on_multiple_data(f: Callable[[str], Any], data: List[str]) -> List[Any]:
    """
    Run a single-argument function on a list of string data.

    Parameters:
    - f: A function that takes a single string argument and performs some action.
    - data: A list of strings to be processed by the function.

    Returns:
    - results: A list of results produced by the function, if applicable.
    """
    results = []
    for value in tqdm(data, desc="Processing data"):
        try:
            result = f(value)
            results.append(result)
        except Exception as e:
            logging.error(f"Error while processing {value}: {e}")
    return results

def run_str_list_function_on_multiple_data(f: Callable[[str, list], Any], data: List[str], fixed_argument) -> List[Any]:
    """
        Run a single-argument function on a list of string data and fixed list.

        Parameters:
        - f: A function that takes a string argument and a list of string then performs some action.
        - data: A list of strings to be processed by the function.
        - fixed_argument: A list of strings which is passed to the function in each iteration.

        Returns:
        - results: A list of results produced by the function, if applicable.
        """
    results = []
    for value in tqdm(data, desc="Processing data"):
        try:
            result = f(value, fixed_argument)
            results.append(result)
        except Exception as e:
            logging.error(f"Error while processing {value}: {e}")
    return results


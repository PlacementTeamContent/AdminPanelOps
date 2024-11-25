import os
import logging
from tqdm import tqdm
from symtable import Function
from dotenv import load_dotenv
from typing import Callable, List, Any
from topin_prod.topin_prod_automation import TopinProdAutomation
from nxtwave_selenium_driver.nxtwave_selenium_driver import NxtWaveWebDriver
from nxtwave_utilities.utils import get_question_id_list, run_str_list_function_on_multiple_data

load_dotenv()

#CONSTANTS
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    username = os.getenv('TOPIN_PROD_USERNAME')
    password = os.getenv('TOPIN_PROD_PASSWORD')

    #USAGE OF AUTOMATION FUNCTION TO DELETE GIVEN TAGS FOR QUESTION
    topin_prod_agent = TopinProdAutomation(NxtWaveWebDriver.get_driver(visible=True), username, password, CURRENT_DIR_PATH)

    #REMOVING OLD RESPONSE FROM RESPONSE FILE
    topin_prod_agent.clear_response_file()


    run_str_list_function_on_multiple_data(
        topin_prod_agent.delete_specific_question_tags,
        get_question_id_list(CURRENT_DIR_PATH),
        ['TOPIC_QUANTITATIVE_NIAT_ENTRANCE_MCQ']
    )

    input()

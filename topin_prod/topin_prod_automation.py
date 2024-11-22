from time import sleep
from selenium.webdriver.common.by import By


class TopinProdAutomation:
    """
    Contains function to do automated tasks on topin prod.
    """

    def __init__(self, driver, user_name, password):
        self.DRIVER = driver
        self.USERNAME = user_name
        self.PASSWORD = password
        self.TOPIN_HOME_URL = "https://nxtwave-assessments-backend-topin-prod-apis.ccbp.in/admin/"
        self.QUESTION_TAG_URL = "https://nxtwave-assessments-backend-topin-prod-apis.ccbp.in/admin/nkb_question/questiontag/"

        self.login()

    def login(self):
        self.DRIVER.get(self.TOPIN_HOME_URL)
        # LOGGING IN FOR NEW SESSION
        self.DRIVER.find_element("id", "id_username").send_keys(self.USERNAME)
        self.DRIVER.find_element("id", "id_password").send_keys(self.PASSWORD)
        self.DRIVER.find_element("xpath", "//input[@value='Log in']").click()

    def delete_all_question_tags(self, q_id:str):
        """
        :param q_id: uuid4 id of question
        :return: none
        Deletes all question tag for the corresponding question id from topin prod
        """

        trimmed_q_id = q_id.split('-')[0]

        try:
            self.DRIVER.get(self.QUESTION_TAG_URL)
            self.DRIVER.find_element(By.ID, "searchbar").send_keys(trimmed_q_id)
            self.DRIVER.find_element(By.XPATH, "//input[@value='Search']").click()
            sleep(1)

            self.DRIVER.find_element(By.ID, "action-toggle").click()
            self.DRIVER.find_element(By.NAME, "action").send_keys("Delete selected question tags")
            self.DRIVER.find_element(By.NAME, "index").click()
            sleep(1)
            self.DRIVER.find_element(By.XPATH, "(//input)[last()]").click()
            sleep(2)
        except:
            raise ValueError(f'No Tags for Question ID: {q_id}')



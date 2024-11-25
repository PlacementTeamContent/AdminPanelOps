import os
from time import sleep
from selenium.webdriver.common.by import By


class TopinProdAutomation:
    """
    Contains function to do automated tasks on topin prod.
    """

    def __init__(self, driver, user_name, password, root_path):
        self.DRIVER = driver
        self.USERNAME = user_name
        self.PASSWORD = password
        self.ROOT_PATH = root_path
        self.TOPIN_HOME_URL = "https://nxtwave-assessments-backend-topin-prod-apis.ccbp.in/admin/"
        self.QUESTION_TAG_URL = "https://nxtwave-assessments-backend-topin-prod-apis.ccbp.in/admin/nkb_question/questiontag/"

        self.login()

    def login(self):
        self.DRIVER.get(self.TOPIN_HOME_URL)
        # LOGGING IN FOR NEW SESSION
        self.DRIVER.find_element("id", "id_username").send_keys(self.USERNAME)
        self.DRIVER.find_element("id", "id_password").send_keys(self.PASSWORD)
        self.DRIVER.find_element("xpath", "//input[@value='Log in']").click()

    def clear_response_file(self):
        response_file = open(
            os.path.join(self.ROOT_PATH, 'Output Data Files', 'topin_prod_automation_response.txt'),
            'w',
            encoding='utf-8'
        )
        response_file.close()

    def delete_all_question_tags(self, q_id:str):
        """
        :param q_id: uuid4 id of question
        :return: none
        Deletes all question tag for the corresponding question id from topin prod
        """

        response_file = open(
            os.path.join(self.ROOT_PATH, 'Output Data Files', 'topin_prod_automation_response.txt'),
            'a+',
            encoding='utf-8'
        )

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
            print(f"{q_id}: Deleted All Tags", file=response_file)
        except:
            raise ValueError(f'No Tags for Question ID: {q_id}')
        finally:
            response_file.close()

    def delete_specific_question_tags(self, q_id:str, q_tags:str):
        """
        :param q_id: uuid4 id of question
        :param q_tags: list of tag names to be deleted
        :return: none
        Deletes given question tag for the corresponding question id from topin prod
        """

        response_file = open(
            os.path.join(self.ROOT_PATH, 'Output Data Files', 'topin_prod_automation_response.txt'),
            'a+',
            encoding='utf-8'
                             )

        trimmed_q_id = q_id.split('-')[0]

        try:
            self.DRIVER.get(self.QUESTION_TAG_URL)
            self.DRIVER.find_element(By.ID, "searchbar").send_keys(trimmed_q_id)
            self.DRIVER.find_element(By.XPATH, "//input[@value='Search']").click()
            sleep(1)

            rows = self.DRIVER.find_elements(By.XPATH, "//table[@id='result_list']//tr")

            nothing_to_delete = True
            deleted_tags = []
            for row in rows:
                cells = row.find_elements(By.CLASS_NAME, "field-tag_name_enum")
                for cell in cells:
                    if str(cell.text).strip() in q_tags:
                        deleted_tags.append(str(cell.text).strip())
                        row.find_elements(By.CLASS_NAME, "action-checkbox")[0].click()
                        nothing_to_delete = False
                        break
            if nothing_to_delete:
                raise ValueError(f'Unable to find tags from the list')
            else:
                self.DRIVER.find_element(By.NAME, "action").send_keys("Delete selected question tags")
                self.DRIVER.find_element(By.NAME, "index").click()
                sleep(1)
                self.DRIVER.find_element(By.XPATH, "(//input)[last()]").click()
                sleep(2)
                print(f"{q_id}: {len(deleted_tags)}\n{deleted_tags}", file=response_file)
        except:
            raise ValueError(f'No Tags for Question ID: {q_id}')

        finally:
            response_file.close()


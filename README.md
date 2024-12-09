# AdminPanelOps

#### This `repo` contains 4 python modules.

- **learning_portal_prod** : Contains functions related to do operations on `learning portal prod backend`.
- **topin_prod** : Contains functions related to do operations on `topin  prod backend`.
- **nxtwave_selenium_driver** : Contains functions to get `webdrivers`
- **nxtwave_utilities** : Contains helper functions to stream data from file to function and to simulate function calls

#### There are 2 directories

- **Input Data Files**: Contains files which will serve as input files to functions
- **Output Data Files**: Contains files which will save responses of functions.

---

## Steps to SetUp

1. Clone the repository
2. create `.env` file, it should look like below sample:
```
TOPIN_PROD_USERNAME=""
TOPIN_PROD_PASSWORD=""
LP_PROD_USERNAME=""
LP_PROD_PASSWORD=""
```
3. Fill these key values with correct credentials.
4. Save all required inputs into corresponding files in ``Input Data Files directory``
5. Import required functions in main and use them.


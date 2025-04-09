# DataDev Quest Challenge 2025_03

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/logo.svg)

### Challenged By: 
Cristian Saavedra Desmoineaux

### Objective
Familiarize yourself with VizQL Data Service, and connect and execute a query to a published data source.

### Beginner Challenge

Link to the Challenge: https://datadevquest.com/ddq2025-03-vizql-data-service-vds-beginner/

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/2025_03_Beginner_Challenge.png)

Apply the filter in VizQL Data Service to filter the Category to keep only Furniture, and Technology.

The output:

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/2025_03_beginner_output.png)

### Intermediate Challenge

Link to the Challenge: https://datadevquest.com/ddq2025-03-vizql-data-service-vds-intermediate/

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/2025_03_Intermediate_Challenge.png)

Apply the TOP N filter and the context filter in VizQL Data Service to get the output same as the output data in Tableau Desktop.

The Output:

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/2025_03_Intermediate_output.png)

### Instructions
- You need to install Python in your local computer or following the instructions from the DataDevQuest Challenge in Postman
- Fork the repository and clone it to your local computer
- Open the Command Prompt (for Windows) and Terminal (for Mac), change the directory to the DataDevQuest_2025_03
    ```
    cd DataDevQuest_2025_03
    ```
- Install and activate the virtual environment
    ```
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```    
- Install the packages in the Command Prompt
    ```
    pip install -r requirements.txt
    ```
    It may takes a few minutes to install all packages:
    - requests
    - pandas
    - json
- Open the Le_vizql_ch_2025_03_Solution_Beginner.py file by your Text Editor and replace the credentials in the main function by your:
    - PAT_NAME
    - PAT_SECRET
    - SITE_ID
    - LUID
- Run this script for the Beginner Challenge:
    ```
    python Le_vizql_ch_2025_03_Solution_Beginner.py
    ```
- Run this script for the Intermediate Challenge:
    ```
    python Le_vizql_ch_2025_03_Solution_Intermediate.py
    ```

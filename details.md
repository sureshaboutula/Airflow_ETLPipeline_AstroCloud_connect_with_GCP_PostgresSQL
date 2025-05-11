### First Deploy the code to Astro Cloud
astro deploy
![image](https://github.com/user-attachments/assets/a7e17e4d-acdd-4824-a6b3-6750307a1cd2)

![image](https://github.com/user-attachments/assets/c266df70-d364-4575-9b11-e2f0ff2efc76)

![image](https://github.com/user-attachments/assets/46bfd263-a2a2-4135-8b2c-8d3067de9bc8)

### Launch Airflow from Astro cloud
![image](https://github.com/user-attachments/assets/e0079d60-a18a-4f82-bb1b-43a6a05d35a1)

### Add connectinos for HTTP API and Postgres SQL
![image](https://github.com/user-attachments/assets/a5f46b0d-369e-4805-a02a-5e69c681a862)

![image](https://github.com/user-attachments/assets/d3cbca86-3ceb-43ef-a047-0f589c6332dd)

### Creating Postgres SQL in GCP:
*Step 1: Create a PostgreSQL Instance in GCP*
1.	Go to the GCP Console.
2.	Click “Create Instance” → choose PostgreSQL.
3.	Fill in:
o	Instance ID: e.g., my-postgres-db
o	Password: Set a secure root password.
o	Choose a region close to your Astro Cloud deployment.
4.	Click Create.

*Step 2: Create a Database Inside the Instance*
Once the instance is created:
1.	Click the instance → Go to “Databases” tab.
2.	Click “Create database” (e.g., airflowdb).

*Step 3: Get the Connection Info (Host + Port)*
1.	Go to the “Instance Details” page.
2.	Copy:
o	Public IP address — this is your host
o	Port — usually 5432
o	Username — default is postgres
o	Password — the one you set earlier
o	Database name — from step 2 (e.g., airflowdb)

*Step 4: Allow Public IP Connections*
1.	In “Instance details”, go to “Connections”.
2.	Under Authorized networks, click “Add network”.
3.	Add this IP range for Astro Cloud: 0.0.0.0/0
4. Click Save and wait for it to update.

![image](https://github.com/user-attachments/assets/f1c8498e-cc8e-404d-b646-4b68131244e4)

![image](https://github.com/user-attachments/assets/e4d92c80-fb73-47c7-9475-5d3172c2477f)

![image](https://github.com/user-attachments/assets/ed251bcb-1e28-47b3-83c8-64684d66311e)

![image](https://github.com/user-attachments/assets/adceed97-f54a-416c-83de-e3a53d4454ae)

![image](https://github.com/user-attachments/assets/c682997d-5a22-457c-bf59-20c90ac73687)

![image](https://github.com/user-attachments/assets/118362da-5502-4b3a-8b31-317a5fda64cb)

![image](https://github.com/user-attachments/assets/2e7be40b-06f4-4f2a-aa07-03b0301cbb85)

**** Public IP should be given as Host in Airflow Postgres SQL connector

### Goto DAG tab and Trigger the Pipeline in Astro cloud
![image](https://github.com/user-attachments/assets/08828b55-0b46-4fbf-8a4e-2cb6d5ffdfbc)

![image](https://github.com/user-attachments/assets/c0e0a2ca-7176-4402-953f-4a71931af2d8)

![image](https://github.com/user-attachments/assets/0e4e7ec5-3b48-4f92-8ffe-3cce0a61ff01)

![image](https://github.com/user-attachments/assets/a1776ca5-db45-4dd2-8068-f9dc36c2089d)

![image](https://github.com/user-attachments/assets/afe9ce46-9a5d-4fbc-ba7b-399ab385ead6)

# Connect Postgres SQL to DBeaver to validate the results
![image](https://github.com/user-attachments/assets/56781989-1c80-4a0f-b0a1-765b997e52da)

![image](https://github.com/user-attachments/assets/9589d511-b566-4113-bffb-515f2e34813a)


















# from airflow.decorators import dag, task # type: ignore
# from datetime import datetime
# from airflow.providers.http.operators.http import SimpleHttpOperator # type: ignore
# from airflow.providers.postgres.hooks.postgres import PostgresHook # type: ignore
# from airflow.utils.dates import days_ago # type: ignore
# import json

# # Define the DAG
# @dag(
#     dag_id = 'nasa_apod_postgres',
#     start_date = days_ago(1),
#     schedule = "@daily",
#     catchup = False 
# )

# def etl_pipeline():

#     # Step 1: Create a table if it does not exists
#     @task
#     def create_table():
#         ## Intialize the Postgreshook
#         postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

#         ## SQL Query to create the table
#         create_table_query = """
#         CREATE TABLE IF NOT EXISTS apod_data(
#         id SERIAL PRIMARY KEY,
#         title VARCHAR(255),
#         explanation TEXT,
#         url TEXT,
#         date DATE,
#         media_type VARCHAR(50)
#         );
#         """
#         #Execute the table creation query
#         postgres_hook.run(create_table_query)

#     # Stesp 2 : Extract the NASA API Data(APOD) - Astronomy Picure of the daya - Extract Pipeline
#     # https://api.nasa.gov/
#     # https://api.nasa.gov/planetary/apod?api_key=6yNfib4U8HNodyxhfRhcKfbq63ErfNERMMnYWNUu
#     extract_apod = SimpleHttpOperator(
#         task_id='extract_apod',
#         http_conn_id='nasa_api',  ## Connecion ID defined in Airflow for NASA API
#         endpoint='planetary/apod', ## NASA APIendpoint for apod
#         method='GET',
#         data={"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"},  ## Using the API_KEY from the connection
#         response_filter=lambda response:response.json()   ## Convert response to Json
#     )


#     # Steps 3 : Transform the data (pick the information that you need to save)
#     @task
#     def transform_apod_data(response):
#         apod_data = {
#             "title": response.get('title', ''),
#             "explanation": response.get('explanation', ''),
#             "url": response.get('url', ''),
#             "date": response.get('date', ''),
#             "media_type": response.get('media_type', '')
#         }
#         return apod_data

#     # Step 4 : Load the data into Postgres SQL
#     @task
#     def load_data_to_postgres(apod_data):
#         ## Initialize the PostgresHook
#         postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

#         ## Define the SQL Insert Query
#         insert_query = """
#         INSERT INTO apod_data (title, explanation, url, date, media_type)
#         VALUES (%s, %s, %s, %s, %s)
#         """

#         ## Execute the Insert Query
#         postgres_hook.run(insert_query, parameters=(
#             apod_data['title'],
#             apod_data['explanation'],
#             apod_data['url'],
#             apod_data['date'],
#             apod_data['media_type']
#         ))

#     # Step 5: Verify the data DBViewer

#     # Step 6: Define the task dependencies
#     # Extract
#     create_table() >> extract_apod ## Ensure the table is created before extraction
#     api_response = extract_apod.output
#     # Transform
#     transformed_data = transform_apod_data(api_response)
#     # Load
#     load_data_to_postgres(transformed_data)
# etl_pipeline()

#####################################

from airflow.decorators import dag, task  # type: ignore
from datetime import datetime, timedelta
from airflow.providers.http.hooks.http import HttpHook  # ✅ Updated import
from airflow.providers.postgres.hooks.postgres import PostgresHook  # type: ignore
# from airflow.utils.dates import days_ago  # type: ignore

# Define the DAG
@dag(
    dag_id='nasa_apod_postgres',
    start_date=datetime.now() - timedelta(days=1),
    schedule="@daily",
    catchup=False,
    tags=["example"],
)
def etl_pipeline():

    # Step 1: Create the table in Postgres
    @task()
    def create_table():
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS apod_data(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """
        postgres_hook.run(create_table_query)

    # Step 2: Extract data from NASA APOD API using HttpHook
    @task()
    def extract_apod():
        hook = HttpHook(http_conn_id='nasa_api', method='GET')
        response = hook.run(
            endpoint='planetary/apod',
            data={"api_key": hook.get_connection('nasa_api').extra_dejson.get('api_key')}
        )
        return response.json()

    # Step 3: Transform the data
    @task()
    def transform_apod_data(response):
        apod_data = {
            "title": response.get('title', ''),
            "explanation": response.get('explanation', ''),
            "url": response.get('url', ''),
            "date": response.get('date', ''),
            "media_type": response.get('media_type', '')
        }
        return apod_data

    # Step 4: Load into Postgres
    @task()
    def load_data_to_postgres(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        insert_query = """
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s)
        """
        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))

    # Step 5: Verify the data DBViewer

    # Step 6: Define the task dependencies
    # Extract
    create_table_task = create_table()
    api_response = extract_apod()
    # Transform
    transformed_data = transform_apod_data(api_response)
    create_table_task >> api_response
    # Load
    load_data_to_postgres(transformed_data)


etl_pipeline()

# Spark Batch Pipeline (Applied Job 2025)

An end-to-end data engineering batch pipeline built using **PySpark** to ingest, transform, and load job application data into a **PostgreSQL** relational database.

## Technical Stack
* **Language:** Python
* **Data Processing:** PySpark (Spark SQL)
* **Database:** PostgreSQL
* **Environment Management:** 'python-dotenv'

## How to Run
1. Clone the repository.
2. Set up your local environment variables in a '.env' file ('DB_URL', 'DB_USER', 'DB_PASSWORD').
3. Run the pipeline script:
'''bash
py src/pipeline.py (or python src/pipeline.py)
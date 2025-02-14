# Memory Builder

## Getting Started

This guide will help you set up and run the Memory Builder application using Docker Compose.

### Prerequisites

* **Docker Desktop:** Ensure you have Docker Desktop installed and running on your machine. You can download it from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

### Setup and Run (Cross-Platform Instructions)

1. **Environment Configuration:**
   - Navigate to the project directory in your terminal or command prompt.
   - **Copy the environment variable template:**
     - **For macOS/Linux:**
       ```bash
       cp .env.example .env
       ```
     - **For Windows (using Command Prompt):**
       ```cmd
       copy .env.example .env
       ```
     - **For Windows (using PowerShell):**
       ```powershell
       Copy-Item .env.example .env
       ```
   - **Modify `.env` file (if needed):** Open the `.env` file with a text editor and adjust any environment variables as necessary.  This file likely contains settings for your database and application.

2. **Start the Application and Database:**
   - In your terminal or command prompt (still in the project directory), run the following command:
     ```bash
     docker compose -f docker-compose.dev.yml up --build
     ```
     This command will:
     - Read the `docker-compose.dev.yml` file which defines your application and database services.
     - Build the Docker images if they are not already built.
     - Start the containers in the background.

   - **Wait for the containers to start:**  It might take a few moments for Docker to download images and start the services. You can monitor the logs in your terminal to see when the application is ready.

### Accessing the Application and Database

* **Client Application:**
    - **Host Machine:** Access the client application in your web browser at: `http://localhost:8181`
    - **Docker Container (for debugging or development):** The application is running on port `8000` inside the container.

* **Database (PostgreSQL):**
    - **Host Machine:** You can connect to the database from your host machine using a database client (like pgAdmin, DataGrip, or DBeaver) connecting to:
        - **Host:** `localhost` or `127.0.0.1`
        - **Port:** `5401`
        - **Database credentials:**  (These are likely defined in your `.env` file - check for variables like `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`)
    - **Docker Container Access:**
        - To access the database directly within the container, use:
            ```bash
            docker compose -f docker-compose.dev.yml exec db psql -U postgres -d memory_db
            ```
            This will open a PostgreSQL interactive terminal. You can also specify a different database name if needed.
        - The database is running on port `5432` inside the container for internal container communication.

### Stopping the Application and Database

To gracefully stop the running application and database containers, run the following command in your terminal or command prompt (in the project directory):

```bash
docker compose -f docker-compose.dev.yml down
```

### Cleaning Up the System (Removing Volumes)

To completely remove the containers, networks, and **volumes** (persistent data) associated with this project, use the following command:

```bash
docker compose -f docker-compose.dev.yml down -v
```
**Warning:** This command will delete your database data if it's stored in Docker volumes. Use with caution if you need to preserve your data.


### Additional Notes to understand the code flow:

* **Ingestion Request**
  - This is served as an asynchronous request
  - On any ingestion request, calls the router, which in turn calls the corresponding knowledge ingestion request asynchronously (see `worker/ingestion_tasks.py`)
  - This will in turn call the manager to ingest text into corresponding memory layers (Reference `memory/manager.py`) 

* **Query Request**
  - This will be served synchronously
  - On any query request, it will query the manager to retrieve the corresponding list of matching nodes, 

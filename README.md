# memory-builder

## Setup

* To run the client app and the database, run the following command:
```bash
cp .env.example .env
chmod +x memory_builder/entrypoint.sh 
docker compose -f docker-compose.dev.yml up --build
```

* To stop the client app and the database, run the following command:
```bash
docker compose -f docker-compose.dev.yml down
```

* To clear the system, run the following command:
```bash
docker compose -f docker-compose.dev.yml down -v
```

* The client app will be running on port 8181 of the host machine and port 8000 of the container.
* The database will be running on port 5401 of the host machine and port 5432 of the container.

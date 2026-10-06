# Local Development

## Prerequisites

- Docker Desktop
- Git
- A modern browser

## Start the stack

From the repository root:

```bash
docker compose up --build
```

The development services are exposed at:

- Web console: `http://localhost:5173`
- API: `http://localhost:8000`
- API health: `http://localhost:8000/health`
- API docs: `http://localhost:8000/docs`

## Stop

```bash
docker compose down
```

To remove the local PostgreSQL volume as well:

```bash
docker compose down -v
```

Never place real credentials in `.env` committed to Git.

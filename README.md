## intallation

```sh
git clone https://github.com/zharuk-alex/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

```sh
docker-compose up --build
```

```sh
docker exec -it contacts-app alembic revision --autogenerate -m "Create contacts table"
docker exec -it contacts-app alembic upgrade head
```

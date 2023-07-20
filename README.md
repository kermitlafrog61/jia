## Getting Started

First, run the development server:

Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker-Compose](https://docs.docker.com/compose/install/linux/)
```bash
touch .env

cp .env-example $(pwd)/.env

docker-compose up
```

Open [http://localhost](http://0.0.0.0:80) with your browser to see the result.


### Create superuser

```bash
docker-compose exec backend bash


 ./manage.py createsuperuser

```

Open [http://localhost/admin/](http://0.0.0.0:80/admin/) with your browser to see the result admin panel.



## Deploy to server

Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker-Compose](https://docs.docker.com/compose/install/linux/)
```bash
touch .env

cp .env-example $(pwd)/.env #copy environment for production

docker-compose up -d --build
```

Open https://your_domain_name with your browser to see the result.


### Create superuser    

```bash
docker-compose exec backend bash


 ./manage.py createsuperuser

```

Open https://your_domain_name/admin/ with your browser to see the result admin panel.
up:
	docker compose up --build

down:
	docker compose down

migrate:
	docker compose up -d db
	docker compose run --rm web python manage.py migrate

makemigrations:
	docker compose run --rm web python manage.py makemigrations

createsuperuser:
	docker compose run --rm web python manage.py createsuperuser

logs:
	docker compose logs -f

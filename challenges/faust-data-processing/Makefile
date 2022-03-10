.PHONY: build
build:
	docker-compose build

.PHONY: down
down:
	@docker-compose down

.PHONY: up
up: down build
	@docker-compose up

all:
	docker build . -t cachaca_bot
	docker tag cachaca_bot:latest docker-registry.solv.tec.br/cachaca_bot:latest
	docker push docker-registry.solv.tec.br/cachaca_bot:latest

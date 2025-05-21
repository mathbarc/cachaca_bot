all:
	docker build . -t cachaca_bot
	docker tag cachaca_bot:latest docker-registry.solv.local/cachaca_bot:latest
	docker push docker-registry.solv.local/cachaca_bot:latest

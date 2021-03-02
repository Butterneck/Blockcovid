.PHONY: help

-include .env


help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Starts project using docker-compose
	docker-compose -f ./compose/docker-compose.yaml up --build

k8s-up: ## Starts project using minikube
	minikube start && minikube apply -f k8s

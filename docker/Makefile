IMAGE_NAME=local/perl_test
CONTAINER_NAME=perl_test

build:
	docker build --progress=plain -t $(IMAGE_NAME) .

run:
	docker run -d --name=$(CONTAINER_NAME) -it $(IMAGE_NAME)

bash:
	docker exec -it $(CONTAINER_NAME) bash || true

start:
	docker start $(CONTAINER_NAME)

stop:
	docker stop $(CONTAINER_NAME)

rm:	stop
	docker rm $(CONTAINER_NAME)

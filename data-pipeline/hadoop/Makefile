.PHONY: build
build:
	docker image build -t esakik/hadoop:latest .

.PHONY: run
run:
	docker container run --name esakik-hadoop -d -p 50070:50070 esakik/hadoop:latest;
	docker exec -it esakik-hadoop /bin/bash;

.PHONY: remove
remove:
	docker container stop esakik-hadoop;
	docker container rm esakik-hadoop;
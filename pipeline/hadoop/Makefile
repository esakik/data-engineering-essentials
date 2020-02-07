.PHONY: build
build:
	docker image build -t esaki01/hadoop:latest .

.PHONY: run
run:
	docker container stop esaki01-hadoop;
	docker container rm esaki01-hadoop;
	docker container run --name esaki01-hadoop -d -p 50070:50070 esaki01/hadoop:latest;
	docker exec -it esaki01-hadoop /bin/bash;
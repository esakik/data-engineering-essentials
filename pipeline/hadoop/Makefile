.PHONY: build
build:
	docker image build -t esaki01/hadoop:latest .

.PHONY: run
run:
	docker container stop esaki01-hadoop;
	docker container rm esaki01-hadoop;
	docker container run --privileged --name esaki01-hadoop -d esaki01/hadoop:latest /sbin/init;
	docker exec -it esaki01-hadoop /bin/bash;
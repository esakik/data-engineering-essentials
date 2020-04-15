.PHONY: jupyter-build
jupyter-build:
	docker image build -t esakik/jupyter jupyter

.PHONY: jupyter-run
jupyter-run:
	docker container run -v ${PWD}/jupyter/notebooks:/app/notebooks -it --rm -p 8888:8888 esakik/jupyter

.PHONY: all-build-run
all-build-run:
	docker-compose up --build

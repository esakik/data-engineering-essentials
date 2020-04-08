from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults


class HelloOperator(BaseOperator):

    @apply_defaults
    def __init__(self, name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name

    def execute(self, context):
        message = "Hello {}".format(self.name)
        print(message)
        return message

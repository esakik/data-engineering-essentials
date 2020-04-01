import datetime
import unittest

from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.utils.state import State

from dags.operators.hello_operator import HelloOperator

DEFAULT_DATE = datetime.datetime.now().utcnow()
TEST_DAG_ID = 'test_hello_operator'


class TestHelloOperator(unittest.TestCase):
    def setUp(self):
        self.dag = DAG(TEST_DAG_ID, schedule_interval='@daily', default_args={'start_date': DEFAULT_DATE})
        self.op = HelloOperator(
            dag=self.dag,
            task_id='test_hello',
            name='test_name'
        )
        self.ti = TaskInstance(task=self.op, execution_date=DEFAULT_DATE)

    def test_execute_no_trigger(self):
        self.ti.run(ignore_ti_state=True)
        self.assertEqual(self.ti.state, State.SUCCESS)

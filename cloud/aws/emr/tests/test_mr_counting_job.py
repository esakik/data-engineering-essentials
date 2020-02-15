from io import BytesIO
from unittest import TestCase

from src.mr_counting_job import MRCountingJob


class MRCountingJobTest(TestCase):

    def test_job(self):
        stdin = BytesIO(b'foo\nbar\nfoo\n')

        mr_job = MRCountingJob(['--no-conf', '-'])
        mr_job.sandbox(stdin=stdin)

        with mr_job.make_runner() as runner:
            runner.run()

            self.assertEqual(runner.counters(),
                             [{'group': {'counter_name': 3}},
                              {'group': {'counter_name': 3}},
                              {'group': {'counter_name': 3}}])

"""PCollectionの各要素（KeyとValueのペア）のKeyとValueの値を入れ替える."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_kv_swap(self):
        expected = [('Friday', 5), ('Monday', 1), ('Saturday', 6), ('Sunday', 0),
                    ('Thursday', 4), ('Tuesday', 2), ('Wednesday', 3)]

        inputs = [(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'),
                  (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.KvSwap())

            assert_that(actual, equal_to(expected))

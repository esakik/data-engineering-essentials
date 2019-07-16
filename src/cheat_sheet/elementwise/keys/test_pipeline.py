"""PCollectionの各要素（KeyとValueのペア）からKeyを抽出する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_keys(self):
        expected = [0, 1, 2, 3, 4, 5, 6]

        inputs = [(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'),
                  (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.Keys())

            assert_that(actual, equal_to(expected))

"""PCollectionの各要素（KeyとValueのペア）からValueを抽出する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_values(self):
        expected = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        inputs = [(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'),
                  (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.Values())

            assert_that(actual, equal_to(expected))

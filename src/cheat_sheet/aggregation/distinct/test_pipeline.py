"""PCollectionの要素から重複を排除する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_distinct(self):
        expected = [1, 2, 3]

        inputs = [1, 1, 2, 3]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.Distinct())

            assert_that(actual, equal_to(expected))

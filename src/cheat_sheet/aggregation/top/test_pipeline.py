"""PCollectionのすべての要素から最大（または最小）のものを数件抽出する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_top_largest(self):
        expected = [[10, 9, 8]]

        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.combiners.Top.Largest(3))

            assert_that(actual, equal_to(expected))

    def test_top_smallest(self):
        expected = [[1, 2, 3]]

        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.combiners.Top.Smallest(3))

            assert_that(actual, equal_to(expected))

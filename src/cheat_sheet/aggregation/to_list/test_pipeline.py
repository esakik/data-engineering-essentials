"""PCollectionのすべての要素を1つのリストに格納する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_to_list(self):
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.combiners.ToList())

            assert_that(actual, equal_to(expected))

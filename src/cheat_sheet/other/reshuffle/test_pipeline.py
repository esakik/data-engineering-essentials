"""PCollectionの要素をワーカー間で再分配する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_reshuffle(self):
        expected = ['A', 'B', 'C']

        inputs = ['A', 'B', 'C']

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.Reshuffle())

            assert_that(actual, equal_to(expected))

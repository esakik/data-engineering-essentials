"""PCollectionの要素をフィルタリングする."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_filter(self):
        expected = ['A']

        inputs = ['A', 'B', 'C']

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.Filter(lambda element: element.startswith('A')))

            assert_that(actual, equal_to(expected))

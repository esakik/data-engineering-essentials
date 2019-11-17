"""PCollectionの各要素に関数を適用する（1対多）."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_flat_map(self):
        expected = [5, 3, 7, 7, 5]

        inputs = [['Alice', 'Bob'], ['Cameron', 'Daniele', 'Ellen']]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.FlatMap(lambda element: [len(e) for e in element]))

            assert_that(actual, equal_to(expected))

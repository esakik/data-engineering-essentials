"""PCollectionの各要素を考慮し、何らかの処理（DoFn）を実行する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class ComputeWordLength(beam.DoFn):

    def __init__(self):
        super(ComputeWordLength, self).__init__()

    def process(self, element):
        yield len(element)


class PipelineTest(TestCase):

    def test_par_do(self):
        expected = [5, 3, 7, 7, 5]

        inputs = ['Alice', 'Bob', 'Cameron', 'Daniele', 'Ellen']

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.ParDo(ComputeWordLength()))

            assert_that(actual, equal_to(expected))

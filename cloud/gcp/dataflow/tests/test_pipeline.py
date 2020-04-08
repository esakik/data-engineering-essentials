from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

from src.pipeline import ComputeWordLength


class ComputeWordLengthTest(TestCase):

    def test_compute_word_length(self):
        expected = [
            13,
            15,
            13
        ]

        inputs = [
            'good morning.',
            'good afternoon.',
            'good evening.'
        ]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.ParDo(ComputeWordLength()))

            assert_that(actual, equal_to(expected))

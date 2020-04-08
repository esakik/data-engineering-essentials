"""PCollectionのすべての要素（KeyとValueのペア）を1つの辞書型に格納する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_to_dict(self):
        expected = [{'A': 2, 'B': 1}]  # Keyが被る場合はどちらか一方のValueが選択される

        inputs = [('A', 1), ('A', 2), ('B', 1)]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.combiners.ToDict())

            assert_that(actual, equal_to(expected))

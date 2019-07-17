"""PCollectionの各要素（KeyとValueのペア）をKeyによって集約する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_group_by_key(self):
        expected = [('cat', ['tama', 'mike']), ('dog', ['pochi'])]

        inputs = [('cat', 'tama'), ('cat', 'mike'), ('dog', 'pochi')]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.GroupByKey())

            assert_that(actual, equal_to(expected))

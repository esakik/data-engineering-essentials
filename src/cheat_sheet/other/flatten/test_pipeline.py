"""複数のPCollectionを単一のPCollectionに結合する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_flatten(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        inputs1 = [1, 2, 3, 4, 5]
        inputs2 = [6, 7, 8, 9, 10]

        with TestPipeline() as p:
            pcol1 = p | 'create pcol1' >> beam.Create(inputs1)
            pcol2 = p | 'create pcol2' >> beam.Create(inputs2)

            actual = (pcol1, pcol2) | beam.Flatten()

            assert_that(actual, equal_to(expected))

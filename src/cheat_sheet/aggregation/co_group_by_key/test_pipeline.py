"""複数のPCollectionの各要素（KeyとValueのペア）をKeyによって集約する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_co_group_by_key(self):
        expected = [
            ('amy', (['amy@example.com'], ['111-222-3333', '333-444-5555'])),
            ('julia', (['julia@example.com'], []))
        ]

        inputs1 = [('amy', 'amy@example.com'), ('julia', 'julia@example.com')]
        inputs2 = [('amy', '111-222-3333'), ('amy', '333-444-5555')]

        with TestPipeline() as p:
            pcol1 = p | 'create pcol1' >> beam.Create(inputs1)
            pcol2 = p | 'create pcol2' >> beam.Create(inputs2)

            actual = ((pcol1, pcol2)
                      | beam.CoGroupByKey())

            assert_that(actual, equal_to(expected))

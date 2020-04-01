"""PCollection のすべての要素を文字列に変換する."""
from unittest import TestCase

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to


class PipelineTest(TestCase):

    def test_to_string_kvs(self):
        """Key, Value を , 区切りの文字列に."""
        expected = ['A,B', 'C,D']

        inputs = [('A', 'B'), ('C', 'D')]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.ToString.Kvs())

            assert_that(actual, equal_to(expected))

    def test_to_string_element(self):
        """各要素を文字列に."""
        expected = ["A", "['A', 'B']", "['C', 'D', 'E']"]

        inputs = ['A', ['A', 'B'], ['C', 'D', 'E']]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.ToString.Element())

            assert_that(actual, equal_to(expected))

    def test_to_string_iterables(self):
        """イテラブルなオブジェクトを文字列に."""
        expected = ['A,B', 'C,D,E']

        inputs = [['A', 'B'], ['C', 'D', 'E']]

        with TestPipeline() as p:
            actual = (p
                      | beam.Create(inputs)
                      | beam.ToString.Iterables())

            assert_that(actual, equal_to(expected))

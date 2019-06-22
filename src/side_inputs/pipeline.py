# coding=utf-8
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import pvalue


class FilterAboveMeanLengthFn(beam.DoFn):
    """平均以上の文字数を持つ文字列をフィルタリングする."""

    def __init__(self):
        super(FilterAboveMeanLengthFn, self).__init__()

    def process(self, element, mean_word_length):
        if element >= mean_word_length:
            yield element


if __name__ == '__main__':
    p = beam.Pipeline(options=PipelineOptions())

    inputs = ["good morning.", "good afternoon.", "good evening."]

    # 主入力
    word_lengths = (p
                    | 'create inputs' >> beam.Create(inputs)
                    | 'compute word length' >> beam.Map(lambda element: len(element)))

    # 副入力
    mean_word_length = word_lengths | 'compute mean word length' >> beam.CombineGlobally(beam.combiners.MeanCombineFn())

    (word_lengths
     | 'filter above mean length' >> beam.ParDo(FilterAboveMeanLengthFn(), pvalue.AsSingleton(mean_word_length))
     | 'write to text' >> beam.io.WriteToText("./output.txt"))

    p.run().wait_until_finish()

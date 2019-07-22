# coding=utf-8
import apache_beam as beam
from apache_beam import pvalue
from apache_beam.options.pipeline_options import PipelineOptions


class JudgeEvenOrOddFn(beam.DoFn):
    """偶数か奇数かを判断する."""

    def process(self, element):
        if element % 2 == 0:
            yield pvalue.TaggedOutput('even', element)
        else:
            yield pvalue.TaggedOutput('odd', element)


if __name__ == '__main__':
    p = beam.Pipeline(options=PipelineOptions())

    inputs = ["good", "normal", "bad"]

    outputs = (p
               | 'create inputs' >> beam.Create(inputs)
               | 'compute word length' >> beam.Map(lambda element: len(element))
               | 'judge even or odd' >> beam.ParDo(JudgeEvenOrOddFn()).with_outputs())

    # 主出力
    outputs['even'] | 'write to even.txt' >> beam.io.WriteToText("./even", file_name_suffix=".txt")

    # 追加出力
    outputs.odd | 'write to odd.txt' >> beam.io.WriteToText("./odd", file_name_suffix=".txt")

    p.run().wait_until_finish()

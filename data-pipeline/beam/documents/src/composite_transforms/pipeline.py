# coding=utf-8
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class ComputeWordCount(beam.PTransform):
    def __init__(self):
        super().__init__()

    """単語数を数えるTransform."""
    def expand(self, pcoll):
        return (pcoll
                | 'split with half space' >> beam.Map(lambda element: element.split(' '))
                | 'compute array size' >> beam.Map(lambda element: len(element)))


if __name__ == '__main__':
    p = beam.Pipeline(options=PipelineOptions())

    inputs = ["There is no time like the present.", "Time is money."]

    (p
     | 'create inputs' >> beam.Create(inputs)
     | 'compute word count' >> ComputeWordCount()
     | 'write to text' >> beam.io.WriteToText("./output.txt"))

    p.run().wait_until_finish()

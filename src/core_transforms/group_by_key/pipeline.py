# coding=utf-8
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--input',
            default='./input.txt',
            help='Input for the pipeline')

        parser.add_argument(
            '--output',
            default='./output.txt',
            help='Output for the pipeline')


def _format_text_fn(element):
    key, value = element.split(',')
    return key, int(value)


if __name__ == '__main__':
    options = MyOptions()
    options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DirectRunner'

    p = beam.Pipeline(options=options)

    (p
     | 'read from text' >> beam.io.ReadFromText(options.input)
     | 'format text' >> beam.Map(_format_text_fn)
     | 'group by key' >> beam.GroupByKey()
     | 'write to text' >> beam.io.WriteToText(options.output, shard_name_template=""))

    p.run().wait_until_finish()

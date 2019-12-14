# coding=utf-8
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--output',
            default='./output.txt',
            help='Output for the pipeline')


if __name__ == '__main__':
    options = MyOptions()
    options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DirectRunner'

    p = beam.Pipeline(options=options)

    emails_list = [
        ('amy', 'amy@example.com'),
        ('carl', 'carl@example.com'),
        ('julia', 'julia@example.com'),
        ('carl', 'carl@email.com'),
    ]

    phones_list = [
        ('amy', '111-222-3333'),
        ('james', '222-333-4444'),
        ('amy', '333-444-5555'),
        ('carl', '444-555-6666'),
    ]

    emails = p | 'CreateEmails' >> beam.Create(emails_list)
    phones = p | 'CreatePhones' >> beam.Create(phones_list)

    ({'emails': emails, 'phones': phones}  # ここは辞書型だけでなくリストやタプルでも大丈夫
     | 'group by key' >> beam.CoGroupByKey()
     | 'write to text' >> beam.io.WriteToText(options.output, shard_name_template=""))

    p.run().wait_until_finish()

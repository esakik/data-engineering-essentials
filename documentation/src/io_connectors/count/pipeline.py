import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from src.io_connectors.count.countio import ReadFromCountingSource

if __name__ == '__main__':
    with beam.Pipeline(options=PipelineOptions()) as p:
        (p
         | 'produce numbers' >> ReadFromCountingSource(10)
         | 'write numbers to text' >> beam.io.WriteToText('count/output.txt', shard_name_template=''))

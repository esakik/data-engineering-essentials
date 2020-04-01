import apache_beam as beam
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import WorkerOptions


GCP_PROJECT_ID = 'gcp-quick-start-261613'
GCS_BUCKET_NAME = 'gs://dataflow-01'
JOB_NAME = 'compute-word-length'


class MyOptions(PipelineOptions):
    """カスタムオプション."""
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--input',
            default='{}/input.txt'.format(GCS_BUCKET_NAME),  # GCS に input.txt を置く
            help='Input for the pipeline')

        parser.add_argument(
            '--output',
            default='{}/output.txt'.format(GCS_BUCKET_NAME),  # GCS に出力する
            help='Output for the pipeline')


class ComputeWordLength(beam.DoFn):
    """文字数を求める変換処理."""

    def __init__(self):
        pass

    def process(self, element):
        yield len(element)


def run():
    options = MyOptions()

    # GCP オプション
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = GCP_PROJECT_ID  # プロジェクトID
    google_cloud_options.job_name = JOB_NAME  # 任意のジョブ名
    google_cloud_options.staging_location = '{}/binaries'.format(GCS_BUCKET_NAME)  # ファイルをステージングするための GCS パス
    google_cloud_options.temp_location = '{}/temp'.format(GCS_BUCKET_NAME)  # 一時ファイルの GCS パス

    # ワーカーオプション
    options.view_as(WorkerOptions).autoscaling_algorithm = 'THROUGHPUT_BASED'  # 自動スケーリングを有効化する

    # 標準オプション
    options.view_as(StandardOptions).runner = 'DataflowRunner'  # Dataflow ランナーを指定

    p = beam.Pipeline(options=options)

    (p
     | 'ReadFromText' >> beam.io.ReadFromText(options.input)
     | 'ComputeWordLength' >> beam.ParDo(ComputeWordLength())
     | 'WriteToText' >> beam.io.WriteToText(options.output, shard_name_template=""))

    p.run()
    # p.run().wait_until_finish()  # パイプラインの完了までブロックする


if __name__ == '__main__':
    run()

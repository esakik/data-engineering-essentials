import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import java.io.IOException;
import java.util.StringTokenizer;

public class WordCount extends Configured implements Tool {
    /**
     * Mapper<入力キーの型, 入力バリューの型, 出力キーの型, 出力バリューの型> を継承したクラス.
     */
    public static class TokenizerMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        @Override
        public void setup(Context context) throws IOException, InterruptedException {
            // 初期化処理
        }

        /**
         * Map 処理を記述する.
         *
         * @param key その行が先頭から何バイト目の位置にあるかというバイトオフセット値（通常は利用しない）
         * @param value 1行分のデータ
         * @param context Context を通してジョブの設定や入出力データにアクセス可能
         */
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }

        @Override
        public void cleanup(Context context) throws IOException, InterruptedException {
            // クリーンナップ処理
        }
    }

    /**
     * Reducer<入力キーの型, 入力バリューの型, 出力キーの型, 出力バリューの型> を継承したクラス.
     */
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        @Override
        public void setup(Context context) throws IOException, InterruptedException {
            // 初期化処理
        }

        /**
         * Reduce 処理を記述する.
         *
         * @param key Map 処理の出力（キー）
         * @param values Map 処理の出力（バリューのイテラブル）
         * @param context Context
         */
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }

        @Override
        public void cleanup(Context context) throws IOException, InterruptedException {
            // クリーンナップ処理
        }
    }

    public int run(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: wordcount <in> <out>");
            System.exit(2);
        }

        // JobTracker に対してジョブを投入する
        Job job = Job.getInstance(getConf(), "WordCount");

        // 入力データに応じて自動的に数が決まるMapタスクとは異なり、Reduceタスクの数は自分で指定する必要がある
        job.setNumReduceTasks(2);

        // jarファイルに格納されたクラスのうちの１つを指定する
        job.setJarByClass(WordCount.class);

        // Mapper、Combiner、Reducer としてどのクラスを利用するか指定する
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // テキストファイルからデータの入出力を行う
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);

        // 入出力用のディレクトリのパス
        TextInputFormat.addInputPath(job, new Path(args[0]));
        TextOutputFormat.setOutputPath(job, new Path(args[1]));

        // ジョブの完了を待つ
        return (job.waitForCompletion(true) ? 0 : 1);
    }

    public static void main(String[] args) throws Exception {
        int res = ToolRunner.run(new Configuration(), new WordCount(), args);
        System.exit(res);
    }
}

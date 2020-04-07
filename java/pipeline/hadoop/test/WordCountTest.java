import junit.framework.TestCase;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrunit.mapreduce.MapDriver;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;

public class WordCountTest extends TestCase {

    private WordCount.TokenizerMapper mapper;
    private MapDriver driver;

    @Before
    public void setUp() {
        mapper = new WordCount.TokenizerMapper();
        driver = new MapDriver(mapper);
    }

    @Test
    public void testWordCountMapper() throws IOException {
        driver.withInput(new LongWritable(0), new Text("this is a pen"))
                .withOutput(new Text("this"), new IntWritable(1))
                .withOutput(new Text("is"), new IntWritable(1))
                .withOutput(new Text("a"), new IntWritable(1))
                .withOutput(new Text("pen"), new IntWritable(1))
                .runTest();
    }
}

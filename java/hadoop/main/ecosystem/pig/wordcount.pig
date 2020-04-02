records = LOAD 'input' AS (line:chararray);
words = FOREACH records GENERATE flatten(TOKENIZE(line)) as word;
word_group = GROUP words by word;
word_count = FOREACH word_group GENERATE group AS word, COUNT(words) as count;
word_count  = ORDER word_count by word;
STORE word_count INTO 'sample_pig_batch/output';

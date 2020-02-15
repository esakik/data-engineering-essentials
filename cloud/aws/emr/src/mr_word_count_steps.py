import re

from mrjob.job import MRJob
from mrjob.step import MRStep

WORD_RE = re.compile(r"[\w']+")


class MRWordCountSteps(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
        ]

    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner_count_words(self, word, counts):
        yield word, sum(counts)

    def reducer_count_words(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordCountSteps.run()

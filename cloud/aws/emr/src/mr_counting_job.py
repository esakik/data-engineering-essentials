from mrjob.job import MRJob
from mrjob.step import MRStep


class MRCountingJob(MRJob):

    def steps(self):
        # 3 steps so we can check behavior of counters for multiple steps
        return [MRStep(mapper=self.mapper),
                MRStep(mapper=self.mapper),
                MRStep(mapper=self.mapper)]

    def mapper(self, _, value):
        self.increment_counter('group', 'counter_name', 1)
        yield _, value


if __name__ == '__main__':
    MRCountingJob.run()

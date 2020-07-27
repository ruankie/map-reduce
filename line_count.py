from mrjob.job import MRJob
import sys

class MRWordCount(MRJob):

    def mapper(self, _, line):
        if inp_word in line:
            yield inp_word, 1

    def reducer(self, word, count):
        yield word, sum(count)


if __name__ == '__main__':
    inp_word = sys.argv[2]
    del sys.argv[2]
    MRWordCount.run()

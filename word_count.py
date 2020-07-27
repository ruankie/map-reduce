from mrjob.job import MRJob
import sys

class MRWordCount(MRJob):

    def mapper(self, _, line):
        yield inp_word, line.split().count(inp_word)

    def reducer(self, word, count):
        yield word, sum(count)


if __name__ == '__main__':
    inp_word = sys.argv[2]
    del sys.argv[2]
    MRWordCount.run()

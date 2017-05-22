import os
import timeit
from multiprocessing import *
import multiprocessing
import time

# def stopwatch(seconds, p):
#     start = time.time()
#     time.clock()
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)
#         time.sleep(1)
#     p.terminate()
#
# def download():
#     os.system("youtube-dl --yes-playlist --playlist-start 6 -f 135+140 https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq")
#
#
# if __name__=='__main__':
#     p1 = multiprocessing.Process(target=download())
#
#     p2 = multiprocessing.Process(target=stopwatch(5,p1))
#     p1.start()
#     p2.start()
#     # os._exit(1)
#     p1.join()
#     p2.join()

os.system("youtube-dl --yes-playlist --playlist-start 7 -f 135+140 https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v")
#os.system("youtube-dl  -f 135+140 https://www.youtube.com/watch?v=jG3bu0tjFbk")



'''
from multiprocessing import Process

# def func1():
#   print 'func1: starting'
#   for i in xrange(10000000): pass
#   print 'func1: finishing'
#
# def func2():
#   print 'func2: starting'
#   for i in xrange(10000000): pass
#   print 'func2: finishing'
#
# if __name__ == '__main__':
#   p1 = Process(target=func1)
#   p1.start()
#   p2 = Process(target=func2)
#   p2.start()
#   p1.join()
#   p2.join()

'''
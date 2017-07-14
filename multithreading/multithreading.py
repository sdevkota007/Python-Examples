# from multiprocessing import Process
#
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
# # if __name__ == '__main__':
# #   p1 = Process(target=func1)
# #   p1.start()
# #   p2 = Process(target=func2)
# #   p2.start()
# #   p1.join()
# #   p2.join()
# # The mechanics of starting/joining child processes can easily be encapsulated into a function along the lines of your runBothFunc:
#
# def runInParallel(*fns):
#   proc = []
#   for fn in fns:
#     p = Process(target=fn)
#     p.start()
#     proc.append(p)
#   for p in proc:
#     p.join()
#
# runInParallel(func1, func2)
#


import threading
import time

def timed_output(name, delay, run_event):
    while run_event.is_set():
        time.sleep(delay)
        print name, ": New Message!"


def main():
    run_event = threading.Event()
    run_event.set()
    d1 = 1
    t1 = threading.Thread(target = timed_output, args = ("bob",d1,run_event))

    d2 = 2
    t2 = threading.Thread(target = timed_output, args = ("paul",d2,run_event))

    t1.start()
    time.sleep(.5)
    t2.start()

    try:
        while 1:
            time.sleep(.1)
            pass
    except KeyboardInterrupt:
        print "attempting to close threads. Max wait =",max(d1,d2)
        run_event.clear()
        t1.join()
        t2.join()
        print "threads successfully closed"

if __name__ == '__main__':
    main()
from multiprocessing import Process
import os


def foo():
    print('child process', os.getpid())  # PID값
    print('my parent is', os.getppid())  # 부모프로세스의 PID값


# 자식프로세스는 얼마든지 생성 가능
if __name__ == '__main__':  # 여기서부터 실행해
    print('parent process', os.getpid())  # parent process 35976
    child1 = Process(target=foo).start()  # foo라는 프로세스를 만들어서 실행해
    # child process 43276 / my parent is 35976
    child2 = Process(target=foo).start()
    # child process 40584 / my parent is 35976
    child3 = Process(target=foo).start()
    # child process 43352 / my parent is 35976


def foo():
    print('This is foo', os.getpid())


def bar():
    print('This is bar', os.getpid())


def baz():
    print('This is baz', os.getpid())


# 각기 다른 작업의 자식프로세스
if __name__ == '__main__':  # 여기서부터 실행하라
    print('parent process', os.getpid())  # parent process 43932
    child1 = Process(target=foo).start()  # This is foo 42304
    child2 = Process(target=bar).start()  # This is bar 43796
    child3 = Process(target=baz).start()  # This is baz 43152

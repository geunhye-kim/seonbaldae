import threading
import os


def foo():
    print('process id', os.getpid())
    print('thread id', threading.get_native_id())


# 같은 작업을 하는 스레드 생성
if __name__ == '__main__':
    print('process id', os.getpid())  # process id 42088
    thread1 = threading.Thread(target=foo).start()  # 스레드를 만드는 함수
    # process id 42088 / thread id 40008
    thread2 = threading.Thread(target=foo).start()
    # process id 42088 / thread id 33148
    thread3 = threading.Thread(target=foo).start()
    # process id 42088 / thread id 44052


def foo():
    print('This is foo', os.getpid())


def bar():
    print('This is bar', os.getpid())


def baz():
    print('This is baz', os.getpid())


# 다른 작업을 하는 스레드 생성 (PID값은 같음)
if __name__ == '__main__':
    print('process id', os.getpid())  # process id 19020
    thread1 = threading.Thread(target=foo).start()  # This is foo 19020
    thread2 = threading.Thread(target=bar).start()  # This is bar 19020
    thread3 = threading.Thread(target=baz).start()  # This is baz 19020

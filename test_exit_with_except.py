import time, sys, os
from threading import Thread, Event


def hello(event=None):
    while True:
        print(".", end="")
        time.sleep(1)
        if isinstance(event, Event):
            if not event.isSet():
                break
    return


if __name__ == "__main__":
    try:
        ev = Event()
        hello()
        Thread(target=hello, args=(ev, )).start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            ev.set()
            print("event set for leave")
            sys.exit(0)
        except SystemExit:
            print("os exit")
            os._exit(0)

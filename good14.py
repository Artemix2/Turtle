import sys
import time


print("  \n\n\n\n  ")
def main():
    a = 0  
    for x in range (0,5):  
        a = a + 1  
        b = ("hi" + "." * a)
        # \r prints a carriage return first, so `b` is printed on top of the previous line.
        sys.stdout.write('\r'+b)

        time.sleep(0.5)
        

def main3():
    d=("GOOD MORNING, Hava a nice Day.")
    sys.stdout.write('\r'+d)
    time.sleep(2)

def main4():
    d=("If you do not change direction, ")
    e=("you may end up where you are heading.")
    f=("Let me fall if I must fall.          ")
    g=("The one I become will catch me.      ")
    h=("Talent wins games,              ")
    i=("but teamwork and intelligence wins championships.")
    j=("Attitude is a little thing that makes a big difference.")
    k=("Life is unpredictable.                                  ")
    l=(" Don’t close your minds to possibilities.               ")
    sys.stdout.write('\r'+d)
    
    time.sleep(2)
    sys.stdout.write('\r'+e)
    time.sleep(2)
    sys.stdout.write('\r'+f)
    time.sleep(2.5)
    sys.stdout.write('\r'+g)
    time.sleep(2.5)
    sys.stdout.write('\r'+h)
    time.sleep(2.5)
    sys.stdout.write('\r'+i)
    time.sleep(2.5)
    sys.stdout.write('\r'+j)
    time.sleep(3)
    sys.stdout.write('\r'+k)
    time.sleep(2.5)
    sys.stdout.write('\r'+l)
    time.sleep(3)
    


def main1():
    #sys.stdout.write('\rloading ')
    main()
    main3()
    main4()
    sys.stdout.flush()
    time.sleep(3)
    sys.stdout.write('\rBye.. C You Soon                                                    \n \n\n')
    sys.stdout.write('\rThank You for watching..... \n\n\n\n\n\n\n   ')

main1()
print('i love Python'[::-1])






import sys
import time
from time import sleep
import itertools
import threading

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rThank you for watching \n\n\n   ')


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True







from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading with context manager..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Loading with object...", "That was fast!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()


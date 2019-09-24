# Python Bruteforce Tool
# Author: Pierelucas
# Date: 24.09.2019

# Module
import zipfile, time, sys, collections

class PyBrute:

    def __init__(self):
        self.zip = ()
        self.pwd = []
        self.exit = False

    def __str__(self):
        return "Your Password for the file: " + self.zip + \
                + "is: " + self.pwd

    def eingabe(self):
        try:
            print("Insert some Passwords: ")
            self.inp = input()
            self.inpset = set(self.inp)
            self.inpcount = len(self.inpset)
            self.inpdeq = collections.deque(self.inp)

            print("Insert Path of your zip file")
            self.zip = input()
        except KeyboardInterrupt:
            print("You pressed Ctrl+c")
            sys.exit()

    def exiten(self):
        while not self.exit:
            if self.exit:
                print("-" * 60)
                print("Pybrute Closed!")
                sys.exit()
            continue

    def crack(self):
        self.i = self.inpcount
        while self.i > 0:
            self.pwd = self.inpdeq[0]
            try:
                self.zip.extractall(pwd=self.pwd)
                print(self.__str__)
                self.exit = True

            except KeyboardInterrupt:
                print("You pressed Ctrl+c")
                sys.exit()
            except RuntimeError:
                print("Error")
                sys.exit()
            except ValueError:
                print("Wrong Value")
                sys.exit()
            except:
                self.inpdeq.popleft()
                self.i -= 1

# Objekt
pybrute = PyBrute()

# Hauptprogramm
pybrute.eingabe()
pybrute.crack()
pybrute.exiten()

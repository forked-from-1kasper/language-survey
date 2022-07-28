from random import shuffle
import sys, tty, termios

head = lambda xs: xs[0]
tail = lambda xs: xs[1:]

languages = [
    "C", "C++", "FreeBASIC", "Go", "Rust", "JavaScript", "Java", "C#", "Scala",
    "Common Lisp", "Agda", "Lean", "Coq", "Idris", "Haskell", "OCaml",
    "Standard ML", "Erlang", "Elixir", "Clojure", "Scheme", "Pascal", "PHP",
    "Forth", "Objective-C", "Ruby", "Perl", "Perl 6", "D", "Kotlin", "Swift",
    "Visual Basic .NET", "F#", "Fortran", "R", "Lua", "Prolog", "COBOL", "Python", "Ada"
]
shuffle(languages)

rating = {}

def ask(i, s1, s2):
    sys.stdout.write("%d. (1) %s or (2) %s? " % (i, s1, s2))
    sys.stdout.flush()

    s = sys.stdin.read(1)
    sys.stdout.write("%s\n" % s)
    sys.stdout.flush()

    if s == "1":
        return False
    elif s == "2":
        return True
    else:
        return ask(i, s1, s2)

num = 0
def le(s1, s2):
    if s1 == s2:
        return True
    elif (s1, s2) in rating:
        return rating[(s1, s2)]
    elif (s2, s1) in rating:
        return not rating[(s2, s1)]
    else:
        global num
        num += 1

        b = ask(num, s1, s2)
        rating[(s1, s2)] = b
        return b

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if le(array[i], array[begin]):
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

fd    = sys.stdin.fileno()
attrs = termios.tcgetattr(fd)

try:
   tty.setcbreak(fd)
   quicksort(languages)
finally:
   termios.tcsetattr(fd, termios.TCSADRAIN, attrs)

print(" < ".join(languages))

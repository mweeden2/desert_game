# import classes as c
import gen_methods as gm
# import an_methods as am

import sys

WIDTH = 120
HEIGHT = 30
TIMEOUT = 100


def main():

    # play with debug mode on if any other argument is given
    if len(sys.argv) > 1:
        player = gm.createPlayer("Matt")
        play(player, True)

    else:
        gm.printIntro()

        uname = gm.getUname()
        player = gm.createPlayer(uname)

        gm.printIntro1(player)

        play(player)


def play(p1, debug=False):
    while (True):
        command = raw_input("\nEnter a command: ")
        if command in ['q', 'quit', 'exit']:
            break

        elif command in ['walk']:
            print 'here'
            p1.update('walk')
            print 'you\'ve walked forward'

        elif command in ['status']:
            p1.prettyPrint()

if __name__ == "__main__":
    main()

# import classes as c
import gen_methods as gm
# import an_methods as am
import walk_texts as ws
import sys



WIDTH = 120
HEIGHT = 30
TIMEOUT = 100

WT_SET = list(ws.walk_text)

COMMAND_D = {
        "quit": ["quit", "q", "exit"],
        "status": ["status", "s"],
        "walk": ["walk", "w"],
        "help": ["help", "h"]
}


HELP_MESSAGE = """
  Commands:
    w   walk
    s   status
    h   help
    q   quit"""


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
        if command in COMMAND_D['quit']:
            break

        elif command in COMMAND_D["help"]:
            print HELP_MESSAGE

        elif command in COMMAND_D['walk']:
            if p1.r.randint(0, 9) == 0:
                wt = p1.r.choice(WT_SET)
                WT_SET.remove(wt)
            p1.update('walk')

        elif command in COMMAND_D['status']:
            p1.prettyPrint()

if __name__ == "__main__":
    main()

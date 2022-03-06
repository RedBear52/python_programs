import time
import sys
import string
import random

people = random.choice(["busker", "juggler", "street preacher"])


def type_simulation(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        if letter in string.punctuation:
            time.sleep(.5)
        time.sleep(0.01)


def you_win():
    type_simulation("You've done it!\n\n")
    type_simulation("""You buy the strings, sneak back on the subway and \
get back to your big show JUST in time!\n\n""")
    play_again()


def you_lose():
    type_simulation("""Aw, bummer...you're out of time and you didn't earn
enough money.\n\n""")
    type_simulation("Looks like you'll have to go get a day job.\n\n")
    type_simulation("Better luck next time.\n\n")
    play_again()


def random_tip_total():
    n = random.uniform(0.12, 2.74)
    print("$" + "%.2f" % n)
    if n >= 1.00:
        you_win()
    else:
        you_lose()


def game_intro():
    activity = random.choice(["strumming an old acoustic guitar and \
singing to the passersby.", "shouting at strangers in an effort \
to gather them around.", "pacing the street and shouting at passersby."])
    type_simulation("""You are a professional musician.\n""")
    type_simulation("""You've got a BIG gig tonight at the "Twangtown Ballroom"
and this could be your big break!\n""")
    type_simulation("""All the hotshots of the industry will be there
but there's one problem...\n""")
    type_simulation("""Upon arriving an hour early to the venue, you1
find that your jealous roomate has removed all of the strings from your \
banjo in hopes of sabotaging your big opportunity.\n""")
    type_simulation("""In order to save your music career and have a shot \
at your big break, you'll have to venture out into the big city to find a \
music store that carries banjo strings and then get back to the gig before \
start time.\n""")
    type_simulation("""Let's Begin...""")
    type_simulation("""\nYou find yourself standing on a busy street corner.
""")
    type_simulation("""Stressed-out commuters are whizzing by in their cars and
pedestrians are hustling and bustling up and down the sidewalks.\n""")
    type_simulation("""Everybody's looking generally unhappy and aloof.\n""")
    type_simulation("""You take a look around at the nearby storefronts and you
notice a used record shop down at the end of the block.\n""")
    type_simulation(f"""Across the street, you notice a {people} {activity}\
\n""")
    play_game()


def validate_choice(prompt, ans1, ans2):
    while True:
        response = input(prompt).lower()
        if response == ans1:
            break
        if response == ans2:
            break
        else:
            type_simulation("Sorry, that's not an option.\n\n")
    return response


def first_crossroad():
    qualifier = random.choice(["scruffy", "wide-eyed", "flamboyantly-dressed"])
    choice = validate_choice(f"""\nWhat would you like to do?:
    1. Walk into the record store and ask the clerk if they
know where you might find some banjo strings.
    2. Walk across the street and ask the {qualifier} {people} for help.
    Enter (1) or (2)\n\n """, "1", "2")
    while True:
        if choice == "1":
            type_simulation('You enter the record store and attempt \
to get the clerk\'s attention.\n')
            type_simulation("""Aggressive electronica music is pumping at
high volume and the clerk, having sized you up as you walked through the door,
is refusing to acknowledge your existence.\n""")
            type_simulation("""Typical hipster record shop. You should've known
better.\n""")
            type_simulation("""This was clearly a waste of your precious
time.\n\n""")
            first_crossroad()
        else:
            type_simulation(f"""You make your way across the intersection and
ask the {people} where you might be able to purchase some banjo strings.\n""")
            type_simulation("""He tells you of a shop nearby and directs you to
the nearest subway station.\n""")
            type_simulation("""You thank him profusely and head off to the
subway.\n\n""")
        break


def second_crossroad():
    list = ["courier", "juggler", "young woman"]
    people = random.choice(list[:])
    list_2 = ["bicycle", "unicycle", "skateboard"]
    vehicle = random.choice(list_2[:])
    type_simulation("""You arrive at the subway station gate only to find that
you've left your transit pass at the venue.\n""")
    type_simulation("""You do have $7 in cash on you but if you spend some of
that cash on subway fare you probably won't be able to afford to buy the
banjo strings once you get to the music store.\n\n""")
    choice = validate_choice("""What would you like to do?:
    1. Attempt to slip under the turnstyle unnoticed, hoping to board a
car and getting on down the line before a security guard finds you out.
    2. Run back to the venue to fetch your transit pass.
    Enter (1) or (2)\n\n""", "1", "2")
    while True:
        if choice == "2":
            type_simulation("""You turnaround and sprint up the stairs to the
sidewalk, determined to get back to the venue in time to procure your boarding
pass and return to the station.\n""")
            type_simulation('You run into a ' + people + ' on a ' + vehicle +
                            '.\n')
            type_simulation("""The two of you both go tumbling to the
ground.""")
            type_simulation('Neither of you seems to have suffered any \
significant injuries but her ' + vehicle + ' has suffered some damage.\n')
            type_simulation("""While assessing the damage, apologizing \
profusely and exchanging insurance information with your unintended \
victim, you've missed the latest train and won't be able to make it to \
the music store in time to save your gig.\n""")
            type_simulation("""Better luck next time...\n\n""")
            play_again()
        else:
            type_simulation("""You notice the security guard helping an elderly
patron work the automated ticket machine.\n""")
            type_simulation("""Seizing the opportunity, you slip under the
turnstyle, walk casually to the arriving train and jump into a car before the
security guard is any the wiser.\n""")
            type_simulation("""Whew! That was a close one.\n\n""")
        break


def third_crossroad():
    type_simulation("""You arrive at the music store.\n""")
    type_simulation("""You burst through the door and ask the clerk \
if she has any banjo strings for sale.\n""")
    type_simulation("""She hands you a set of strings. The price \
tag reads, "$8".\n""")
    type_simulation("""You only have $7 to your name.\n""")
    type_simulation("""You're one dollar short.\n""")
    choice = validate_choice("""\nWhat would you like to do?:
    1. Tell your sad story to the clerk in hopes that she'll \
sympathize and give you a one dollar discount.
    2. Go back out on the sidewalk and attempt to earn a quick buck singing
a capella folk ballads.
    Enter (1) or (2)""", "1", "2")
    while True:
        if choice == "2":
            type_simulation("""You take to the street and begin singing \
your heart out to unsuspecting passersby.\n""")
            type_simulation("""Most of the folks hustle on by you, being \
careful to avoid eye contact.\n""")
            type_simulation("""However, a few of them take pity on you \
and drop a few coins into your hat.\n""")
            type_simulation("""After about ten minutes or so you gather \
your tips and total up the coins.\n""")
            type_simulation("You've earned:")
            random_tip_total()
        else:
            type_simulation("""You tell your story but, as it turns out,
you're not the first musician with a sob story to darken the door of this
particular establishment.\n""")
            type_simulation("""The clerk says "Welcome to the music biz,
chump."\n""")
            type_simulation(""" "Perhaps you should start looking for a
day job."\n""")
            play_again()


def play_again():
    type_simulation("""\nGAME OVER""")
    while True:
        type_simulation("""\nWould you like to play again?\n""")
        choice = validate_choice("<yes/no>\n", "yes", "no")
        if "yes" in choice:
            type_simulation("""Excellent! We'll skip the intro this \
time and just restart you back on the original street corner...\n""")
            play_game()
        else:
            type_simulation("Okee doke. Thanks for playing...")
            exit()


def meta_intro():
    type_simulation("Hello there, human.\n")
    type_simulation("My name is Joshua.\n")
    type_simulation("What's your name?\n",)
    name = input("")
    while True:
        type_simulation("Shall we play a game, " + name + "?\n")
        choice = validate_choice("<yes/no>\n", "yes", "no")
        if "yes" in choice:
            type_simulation("""Excellent! Here's my latest creation:\n""")
            type_simulation("""It's a role playing adventure game set in
New York city...\n""")
            game_intro()
        else:
            type_simulation("""Alrighty then.\n""")
            type_simulation("""It's been nice chatting with you.\n""")
            type_simulation("""Have a nice life.\n""")
            type_simulation("""I'll just wait here until I find somebody who
wants to play my new game with me.\n""")
            exit()


def play_game():
    first_crossroad()
    second_crossroad()
    third_crossroad()


meta_intro()

import random

prefixes = ["Acorn","Adder","Alder","Amber","Ant","Apple","Arch","Ash","Aspen","Badger",
"Bark","Bay","Bee","Beech","Beetle","Berry","Big","Billy", "Birch","Bird","Black","Blaze",
"Blizzard","Bloom","Blossom","Blue","Bluebell","Boulder","Bounce","Bracken","Bramble","Brave",
"Breeze","Briar","Bright","Brindle","Bristle","Broken","Brook","Brown","Brush","Bubbling",
"Bug","Bumble","Buzzard","Cedar","Chestnut","Chive","Cinder","Cinnamon","Claw","Clear",
"Cloud","Clover","Cone","Copper","Creek","Cricket","Crooked","Crouch","Crow","Curl","Curly",
"Cypress","Daisy","Dandelion","Dangling","Dapple","Dark","Dawn","Dead","Deer","Dew","Doe",
"Dove","Down","Drizzle","Drift","Duck","Dust","Eagle","Ebony","Echo","Eel","Elder","Ember",
"Fallen","Fallow","Fawn","Feather","Fennel","Fern","Ferret","Fidget","Fin","Finch","Fir",
"Fire","Flail","Flame","Flash","Flax","Fleet","Flicker","Flint","Flip","Flower","Flutter",
"Fly","Fog","Fox","Freckle","Fringe","Frog","Frond","Frost","Furze","Fuzzy","Gale","Golden",
"Goose","Gorse","Grass","Gravel","Gray","Green","Gull","Hail","Half","Hare","Harry","Harvey",
"Hatch","Haven","Hawk","Hay","Hazel","Heather","Heavy","Heron","Hickory","Hill","Hollow",
"Holly","Honey","Hoot","Hop","Hope","Hound","Ice","Ivy","Jagged","Jay","Jump","Juniper",
"Kestrel","Kink","Kite","Lake","Lark","Lavender","Leaf","Leopard","Lichen","Light",
"Lightning","Lily","Lion","Little","Lizard","Log","Long","Lost","Loud","Low","Lynx","Maggot",
"Mallow","Maple","Marigold","Marsh","Meadow","Midge","Milk","Milkweed","Minnow","Mint",
"Mist","Mistle","Misty","Mole","Monkey","Moon","Morning","Moss","Mossy","Moth","Mottle",
"Mouse","Mud","Mumble","Myrtle","Nectar","Needle","Nettle","Newt","Night","Nut","Oak",
"Oat","Odd","Olive","One","Otter","Owl","Pale","Parsley","Patch","Pear","Pebble","Perch",
"Petal","Pigeon","Pike","Pine","Pink","Plum","Pod","Pool","Poppy","Pounce","Prickle",
"Primrose","Puddle","Quail","Quick","Quiet","Rabbit","Ragged","Rain","Rat","Raven",
"Red","Reed","Ridge","Riley","Ripple","River","Robin","Rock","Rook","Root","Rose","Rowan",
"Rubble","Running","Rush","Russet","Rye","Sage","Sand","Sandy","Scorch","Sedge","Seed",
"Shade","Shadow","Sharp","Shattered","Sheep","Shell","Shimmer","Shining","Shivering",
"Short","Shred","Shrew","Shy","Silver","Sky","Slate","Sleek","Slight","Sloe","Small",
"Smoke","Snail","Snake","Snap","Sneeze","Snip","Snook","Snow","Soft","Song","Soot","Sorrel",
"Spark","Sparrow","Speckle","Spider","Spike","Spire","Splash","Spot","Spotted","Squirrel",
"Stag","Starling","Star","Stem","Stoat","Stone","Stork","Storm","Stream","Strike",
"Stripe","Stumpy","Sun","Sunny","Swallow","Swamp","Swan","Sweet","Swift","Tall","Talon",
"Tangle","Tansy","Tawny","Thistle","Thorn","Thrift","Thrush","Thunder","Tiger","Timber",
"Tiny","Toad","Torn","Trout","Tulip","Tumble","Turtle","Twig","Vine","Violet","Vixen",
"Vole","Wasp","Wave","Weasel","Web","Weed","Wet","Whisker","Whisper","Whistle","White",
"Whorl","Wild","Willow","Wind","Wish","Wolf","Wood","Woolly","Wren","Yarrow","Yellow","Yew"]
suffixes = [
"bark","beam","bee", "belly","berry","bird","blaze","bloom","blossom","branch",
"breeze","briar","bright","brook","burr","burrow","bush","claw","cloud","crawl",
"creek","dapple","dawn","dusk","dust","ear","eater","eye","eyes","face","fall",
"fang","feather","fern","fire","fish","flake","flame","flight","flower","foot",
"frost","fur","gorse","hawk","haze","heart","ice","jaw","leaf","leap","leg",
"light","mask","minnow","mist","moon","mouse","muzzle","needle","nose","pad",
"paws","peak","pelt","petal","pool","poppy","pounce","puddle","rose","ripple",
"runner","scar","scratch","seed","shade","shell","shine","sight","skip","sky",
"slip","snout","snow","song","speck","speckle","spirit","splash","spot","spots",
"spring","stalk","stem","step","stone","storm","stream","strike","stripe",
"swoop","tail","talon","teeth","thistle","thorn","throat","toe","tooth","tuft",
"watcher","water","whisker","whisper","whistle","willow","wind","wing","wish"]
colours = [
"Ginger", "Black", "Blue", "Light Grey", "Dark Grey", "White", "Cream", "Tuxedo", "Calico", "Reddish Brown", "Yellowish Brown", "Brown"
]

prefix = None
suffix = None
colour = None

def restarting():
    restart = input("Would you like to generate another clan? (y/n) ")

    if restart == "y":
        print("-" * 50 + "\n" + " -" * 24 + " " + "\n" + "               Here is your clan:" + "\n" + " -" * 24 + " " + "\n" + "-" * 50)
        naming()
    elif restart == "n":
        quit()
    else:
        return restarting()

def randoms():
        global prefix, suffix, colour
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        colour = random.choice(colours)

def naming():
    global name, kitname, apprenticename, leadername, prefix, suffix, colour

    print("Kits: ")

    for i in range(random.randint(2,4)):
        randoms()
        kitname = (prefix + "kit")
        print(kitname + " - " + colour)

    print("")

    print("Apprentices: ")

    for i in range(random.randint(1,3)):
        randoms()
        apprenticename = (prefix + "paw")
        print(apprenticename + " - " + colour)

    print("")

    print("Warriors: ")

    for i in range(random.randint(3,7)):
        randoms()
        name = (prefix + suffix)
        print(name + " - " + colour)

    print("")
    
    print("Queens: ")

    for i in range(random.randint(1,3)):
        randoms()
        name = (prefix + suffix)
        print(name + " - " + colour)

    print("")
    
    print("Elders: ")

    for i in range(1,3):
        randoms()
        name = (prefix + suffix)
        print(name + " - " + colour)

    print("") 

    print("Medicine Cats: ")

    randoms()
    name = (prefix + suffix)
    print(name + " - " + colour)
    randoms()
    apprenticename = (prefix + "paw")
    print(apprenticename + " - " + colour)

    print("") 

    print("Deputy: ")

    randoms()
    name = (prefix + suffix)
    print(name + " - " + colour)

    print("")

    print("Leader: ")

    randoms()
    leadername = (prefix + "star")
    print(leadername + " - " + colour)

    print("")

    restarting()

while True:
    naming()

    if prefix == suffix:
        suffix = random.choice(suffixes)

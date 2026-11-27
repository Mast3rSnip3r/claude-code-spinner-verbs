# Claude Code Spinner Verbs — with Daily Rotation

A curated collection of **666 spinner verbs** across **36 themed categories** for [Claude Code](https://github.com/anthropics/claude-code), with **automatic daily rotation** — Claude picks a new category every day.

## Table of Contents

| # | Category | Verbs |
|--:|----------|------:|
| 1 | [Back to the Future](#back-to-the-future) | 10 |
| 2 | [Breaking Bad](#breaking-bad) | 73 |
| 3 | [Cat Behavior](#cat-behavior) | 30 |
| 4 | [DC Comics](#dc-comics) | 11 |
| 5 | [Disney / Pixar](#disney--pixar) | 12 |
| 6 | [Doctor Who](#doctor-who) | 10 |
| 7 | [Dune](#dune) | 13 |
| 8 | [Futurama](#futurama) | 43 |
| 9 | [Gaming](#gaming) | 13 |
| 10 | [Harry Potter](#harry-potter) | 13 |
| 11 | [Jurassic Park](#jurassic-park) | 10 |
| 12 | [Lord of the Rings](#lord-of-the-rings) | 13 |
| 13 | [Mario / Nintendo](#mario--nintendo) | 11 |
| 14 | [Marvel / MCU](#marvel--mcu) | 13 |
| 15 | [Medieval / Knights](#medieval--knights) | 10 |
| 16 | [Meme Culture](#meme-culture) | 11 |
| 17 | [Monty Python](#monty-python) | 11 |
| 18 | [Pirate / Nautical](#pirate--nautical) | 11 |
| 19 | [Pokemon](#pokemon) | 11 |
| 20 | [Quantum Physics](#quantum-physics) | 11 |
| 21 | [Retro Gaming](#retro-gaming) | 11 |
| 22 | [Rick and Morty](#rick-and-morty) | 44 |
| 23 | [Rogue Agent](#rogue-agent) | 19 |
| 24 | [Samurai / Japanese](#samurai--japanese) | 11 |
| 25 | [Sci-Fi / Space](#sci-fi--space) | 16 |
| 26 | [Space / NASA](#space--nasa) | 47 |
| 27 | [Star Trek](#star-trek) | 14 |
| 28 | [Star Wars](#star-wars) | 12 |
| 29 | [Stranger Things](#stranger-things) | 11 |
| 30 | [The Mandalorian](#the-mandalorian) | 54 |
| 31 | [The Matrix](#the-matrix) | 11 |
| 32 | [The Office](#the-office) | 12 |
| 33 | [The Simpsons](#the-simpsons) | 31 |
| 34 | [Victorian / Steampunk](#victorian--steampunk) | 11 |
| 35 | [Viking / Norse](#viking--norse) | 11 |
| 36 | [Wild West / Cowboy](#wild-west--cowboy) | 11 |

## How to Use

Copy any category you like from the [Categories](#categories) section, then paste this prompt into Claude Code. Each category has a **Copy as list** dropdown with its verbs as quoted strings, ready to paste.

```
Add the following spinner verbs to my ~/.claude/settings.json using "mode": "append":

<paste the verbs here>
```

### Modes

| Mode | Behavior |
|------|----------|
| `"append"` | Add your verbs to Claude Code's built-in defaults |
| `"replace"` | Use only your verbs (the daily rotation uses this) |

### Manual setup

Add a top-level `spinnerVerbs` key to `~/.claude/settings.json`:

```json
{
  "spinnerVerbs": {
    "mode": "append",
    "verbs": ["Second-breakfasting", "Silly-walking", "Great-scotting"]
  }
}
```

## Daily Rotation (auto-install)

This repo also ships a small rotation script that swaps in a new category each day, so the spinner stays fresh without you touching anything.

```bash
git clone git@github.com:Mast3rSnip3r/claude-code-spinner-verbs.git
cd claude-code-spinner-verbs
./install.sh
```

It copies `categories.json` and `rotate.py` into `~/.claude/spinner-rotate/`, then adds a `SessionStart` hook to `~/.claude/settings.json`. On every start, `rotate.py` picks today's category and writes it to `spinnerVerbs` (in both the CLI settings and, if present, VS Code's settings). Run `./uninstall.sh` to remove everything cleanly.

## Categories

### Back to the Future

(10 verbs)

| Verb |
|------|
| Charging the flux capacitor |
| Time-traveling |
| Jumping timelines |
| Exclaiming Great Scott |
| Hoverboarding |
| Hitting 88mph |
| Climbing the clock tower |
| Shredding on a hoverboard |
| Harnessing lightning |
| Charging 1.21 gigawatts |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Charging the flux capacitor",
"Time-traveling",
"Jumping timelines",
"Exclaiming Great Scott",
"Hoverboarding",
"Hitting 88mph",
"Climbing the clock tower",
"Shredding on a hoverboard",
"Harnessing lightning",
"Charging 1.21 gigawatts",
```
</details>

### Breaking Bad

(73 verbs)

| Verb |
|------|
| Knocking |
| Becoming Heisenberg |
| Treading lightly |
| Applying chemistry |
| Balancing equations |
| Chasing the fly |
| Ringing Tio's bell |
| Tossing the pizza |
| Rolling the barrel |
| Burying money barrels |
| Counting barrels |
| Polishing the Aztek |
| Driving the Aztek |
| Collecting Hank's minerals |
| Calling Saul |
| Weighing the blue |
| Refining blue product |
| Inspecting blue sky |
| Frying chicken |
| Serving chicken |
| Extracting ricin |
| Hiding the ricin |
| Stealing methylamine |
| Fixing the RV |
| Rolling the RV |
| Decorating in purple |
| Wearing Marie's purple |
| Feeding Flynn |
| Counting the cash |
| Hiding the money |
| Applying magnets |
| Magnetizing evidence |
| Dissolving the evidence |
| Taking half measures |
| Taking full measures |
| Running Los Pollos Hermanos |
| Harmonizing with Gale |
| Remembering Gale |
| Crossing the desert |
| Meeting in the desert |
| Meeting in secret |
| Sending to Belize |
| Pouring stevia |
| Following Lydia |
| Fixing the windshield |
| Spinning the sign |
| Protecting the family |
| Smashing the phone |
| Selling burner phones |
| Wearing the porkpie hat |
| Building an empire |
| Washing cars |
| Guarding the lab |
| Avoiding Hank |
| Perfecting purity |
| Planning the train heist |
| Outsmarting Tuco |
| Testing 99.1% purity |
| Roaming Albuquerque |
| Building the superlab |
| Consulting Mike |
| Tracking Gus |
| Calming Tuco |
| Shadowing the Salamancas |
| Guiding Jesse |
| Balancing Skyler's books |
| Watching the teddy bear fall |
| Questioning Todd |
| Distracting Badger |
| Backing Skinny Pete |
| Faking a fugue state |
| Sweeping for bugs |
| Lawyering up |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Knocking",
"Becoming Heisenberg",
"Treading lightly",
"Applying chemistry",
"Balancing equations",
"Chasing the fly",
"Ringing Tio's bell",
"Tossing the pizza",
"Rolling the barrel",
"Burying money barrels",
"Counting barrels",
"Polishing the Aztek",
"Driving the Aztek",
"Collecting Hank's minerals",
"Calling Saul",
"Weighing the blue",
"Refining blue product",
"Inspecting blue sky",
"Frying chicken",
"Serving chicken",
"Extracting ricin",
"Hiding the ricin",
"Stealing methylamine",
"Fixing the RV",
"Rolling the RV",
"Decorating in purple",
"Wearing Marie's purple",
"Feeding Flynn",
"Counting the cash",
"Hiding the money",
"Applying magnets",
"Magnetizing evidence",
"Dissolving the evidence",
"Taking half measures",
"Taking full measures",
"Running Los Pollos Hermanos",
"Harmonizing with Gale",
"Remembering Gale",
"Crossing the desert",
"Meeting in the desert",
"Meeting in secret",
"Sending to Belize",
"Pouring stevia",
"Following Lydia",
"Fixing the windshield",
"Spinning the sign",
"Protecting the family",
"Smashing the phone",
"Selling burner phones",
"Wearing the porkpie hat",
"Building an empire",
"Washing cars",
"Guarding the lab",
"Avoiding Hank",
"Perfecting purity",
"Planning the train heist",
"Outsmarting Tuco",
"Testing 99.1% purity",
"Roaming Albuquerque",
"Building the superlab",
"Consulting Mike",
"Tracking Gus",
"Calming Tuco",
"Shadowing the Salamancas",
"Guiding Jesse",
"Balancing Skyler's books",
"Watching the teddy bear fall",
"Questioning Todd",
"Distracting Badger",
"Backing Skinny Pete",
"Faking a fugue state",
"Sweeping for bugs",
"Lawyering up",
```
</details>

### Cat Behavior

(30 verbs)

| Verb |
|------|
| Occupying the keyboard |
| Assessing the box |
| Zooming at 3am |
| Staring into the void |
| Relocating to the sunbeam |
| Knocking things off the edge |
| Forming a loaf |
| Composing a hairball |
| Blinking judgmentally |
| Retracting toe beans |
| Hunting the laser dot |
| Scaling the curtains |
| Invading a lap |
| Negotiating with purrs |
| Manipulating for treats |
| Chittering at birds |
| Transcending on catnip |
| Kneading biscuits |
| Slow-blinking |
| Demanding chin scratches |
| Ambushing the feather toy |
| Surveilling from the windowsill |
| Shredding cardboard |
| Flicking my tail |
| Ignoring the human |
| Evading the vet carrier |
| Setting the belly trap |
| Counter-surfing |
| Commandeering the laptop |
| Yowling at 5am |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Occupying the keyboard",
"Assessing the box",
"Zooming at 3am",
"Staring into the void",
"Relocating to the sunbeam",
"Knocking things off the edge",
"Forming a loaf",
"Composing a hairball",
"Blinking judgmentally",
"Retracting toe beans",
"Hunting the laser dot",
"Scaling the curtains",
"Invading a lap",
"Negotiating with purrs",
"Manipulating for treats",
"Chittering at birds",
"Transcending on catnip",
"Kneading biscuits",
"Slow-blinking",
"Demanding chin scratches",
"Ambushing the feather toy",
"Surveilling from the windowsill",
"Shredding cardboard",
"Flicking my tail",
"Ignoring the human",
"Evading the vet carrier",
"Setting the belly trap",
"Counter-surfing",
"Commandeering the laptop",
"Yowling at 5am",
```
</details>

### DC Comics

(11 verbs)

| Verb |
|------|
| Patrolling Gotham |
| Lighting the Bat-Signal |
| Dodging kryptonite |
| Tapping the Speed Force |
| Wielding the Lasso of Truth |
| Dark-knighting |
| Assembling the Justice League |
| Laughing like the Joker |
| Boom-tubing |
| Deflecting bullets with bracelets |
| Charging the Lantern ring |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Patrolling Gotham",
"Lighting the Bat-Signal",
"Dodging kryptonite",
"Tapping the Speed Force",
"Wielding the Lasso of Truth",
"Dark-knighting",
"Assembling the Justice League",
"Laughing like the Joker",
"Boom-tubing",
"Deflecting bullets with bracelets",
"Charging the Lantern ring",
```
</details>

### Disney / Pixar

(12 verbs)

| Verb |
|------|
| Chanting Hakuna Matata |
| Sprinkling pixie dust |
| Trying on the glass slipper |
| Bibbidi-bobbidi-booing |
| Belting Let It Go |
| Dancing under the sea |
| Embracing Ohana |
| Launching to infinity |
| Dancing like WALL-E |
| Roaring like Simba |
| Wishing on the Genie |
| Cooking like Remy |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Chanting Hakuna Matata",
"Sprinkling pixie dust",
"Trying on the glass slipper",
"Bibbidi-bobbidi-booing",
"Belting Let It Go",
"Dancing under the sea",
"Embracing Ohana",
"Launching to infinity",
"Dancing like WALL-E",
"Roaring like Simba",
"Wishing on the Genie",
"Cooking like Remy",
```
</details>

### Doctor Who

(10 verbs)

| Verb |
|------|
| Flying the TARDIS |
| Regenerating |
| Exterminating |
| Waving the sonic screwdriver |
| Traveling timey-wimey |
| Shouting Allons-y |
| Invading like a Dalek |
| Not blinking at the Weeping Angel |
| Collecting companions |
| Finding it bigger on the inside |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Flying the TARDIS",
"Regenerating",
"Exterminating",
"Waving the sonic screwdriver",
"Traveling timey-wimey",
"Shouting Allons-y",
"Invading like a Dalek",
"Not blinking at the Weeping Angel",
"Collecting companions",
"Finding it bigger on the inside",
```
</details>

### Dune

(13 verbs)

| Verb |
|------|
| Harvesting spice |
| Riding the sandworm |
| Training with the Bene Gesserit |
| Sweating in a stillsuit |
| Weirding |
| Dwelling in the sietch |
| Drawing the crysknife |
| Spotting wormsign |
| Dreaming of melange |
| Entering the spice trance |
| Summoning Shai-Hulud |
| Using the Voice |
| Flying the ornithopter |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Harvesting spice",
"Riding the sandworm",
"Training with the Bene Gesserit",
"Sweating in a stillsuit",
"Weirding",
"Dwelling in the sietch",
"Drawing the crysknife",
"Spotting wormsign",
"Dreaming of melange",
"Entering the spice trance",
"Summoning Shai-Hulud",
"Using the Voice",
"Flying the ornithopter",
```
</details>

### Futurama

(43 verbs)

| Verb |
|------|
| Bending |
| Hypnotoading |
| Zoidberging |
| Scuttling sideways |
| Farnsworthing |
| Squinting like Fry |
| Kicking like Leela |
| Nibbling |
| Branniganing |
| Sighing like Kif |
| Calculoning |
| Declaring doom like Morbo |
| Conquering Earth like Lrrr |
| Poppling |
| Dark-mattering |
| Thawing out of cryo |
| Blernsballing |
| Mopping like Scruffy |
| Stamping forms like Hermes |
| Bureaucratizing |
| Limboing |
| Velouring |
| Engineering with Amy |
| Bamming |
| Spicing it up like Elzar |
| Hedonismbotting |
| Fiddling for the Robot Devil |
| Building robots for Mom |
| Brain-spawning |
| Jarring heads |
| Bribing Nixon |
| Robbing banks with Roberto |
| Policing with URL |
| What-iffing |
| Delivering packages |
| Planet-expressing |
| Visiting the Near-Death Star |
| Waiting like Seymour |
| Anthologizing |
| Smell-o-scoping |
| Whooping |
| Burgling |
| Rusting |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Bending",
"Hypnotoading",
"Zoidberging",
"Scuttling sideways",
"Farnsworthing",
"Squinting like Fry",
"Kicking like Leela",
"Nibbling",
"Branniganing",
"Sighing like Kif",
"Calculoning",
"Declaring doom like Morbo",
"Conquering Earth like Lrrr",
"Poppling",
"Dark-mattering",
"Thawing out of cryo",
"Blernsballing",
"Mopping like Scruffy",
"Stamping forms like Hermes",
"Bureaucratizing",
"Limboing",
"Velouring",
"Engineering with Amy",
"Bamming",
"Spicing it up like Elzar",
"Hedonismbotting",
"Fiddling for the Robot Devil",
"Building robots for Mom",
"Brain-spawning",
"Jarring heads",
"Bribing Nixon",
"Robbing banks with Roberto",
"Policing with URL",
"What-iffing",
"Delivering packages",
"Planet-expressing",
"Visiting the Near-Death Star",
"Waiting like Seymour",
"Anthologizing",
"Smell-o-scoping",
"Whooping",
"Burgling",
"Rusting",
```
</details>

### Gaming

(13 verbs)

| Verb |
|------|
| Respawning |
| Speedrunning |
| Leveling-up |
| Button-mashing |
| Looting |
| Nerfing |
| Buffing |
| Hunting glitches |
| No-scoping |
| Save-scumming |
| Power-leveling |
| Farming loot |
| Pushing pixels |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Respawning",
"Speedrunning",
"Leveling-up",
"Button-mashing",
"Looting",
"Nerfing",
"Buffing",
"Hunting glitches",
"No-scoping",
"Save-scumming",
"Power-leveling",
"Farming loot",
"Pushing pixels",
```
</details>

### Harry Potter

(13 verbs)

| Verb |
|------|
| Casting expelliarmus |
| Summoning a patronus |
| Brewing potions |
| Playing quidditch |
| Waving a wand |
| Hunting horcruxes |
| Traveling with floo powder |
| Catching the snitch |
| Using accio to summon |
| Unlocking with alohomora |
| Marauding |
| Sending a howler |
| Banishing boggarts |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Casting expelliarmus",
"Summoning a patronus",
"Brewing potions",
"Playing quidditch",
"Waving a wand",
"Hunting horcruxes",
"Traveling with floo powder",
"Catching the snitch",
"Using accio to summon",
"Unlocking with alohomora",
"Marauding",
"Sending a howler",
"Banishing boggarts",
```
</details>

### Jurassic Park

(10 verbs)

| Verb |
|------|
| Stalking raptors |
| Life finding a way |
| Roaring like a T-Rex |
| Cloning dinos |
| Pondering chaos theory |
| Outsmarting raptors |
| Extracting DNA from amber |
| Sparing no expense |
| Hunting in a raptor pack |
| Escaping the island |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Stalking raptors",
"Life finding a way",
"Roaring like a T-Rex",
"Cloning dinos",
"Pondering chaos theory",
"Outsmarting raptors",
"Extracting DNA from amber",
"Sparing no expense",
"Hunting in a raptor pack",
"Escaping the island",
```
</details>

### Lord of the Rings

(13 verbs)

| Verb |
|------|
| Second-breakfasting |
| Bearing the ring |
| Holding an Entmoot |
| Riding Shadowfax |
| Peeking into the palantír |
| Munching lembas |
| Baiting the Balrog |
| Hoarding the precious |
| Mining mithril |
| Lighting Gandalf's fireworks |
| Screeching like a Nazgûl |
| Muttering like Treebeard |
| Frolicking in the Shire |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Second-breakfasting",
"Bearing the ring",
"Holding an Entmoot",
"Riding Shadowfax",
"Peeking into the palantír",
"Munching lembas",
"Baiting the Balrog",
"Hoarding the precious",
"Mining mithril",
"Lighting Gandalf's fireworks",
"Screeching like a Nazgûl",
"Muttering like Treebeard",
"Frolicking in the Shire",
```
</details>

### Mario / Nintendo

(11 verbs)

| Verb |
|------|
| Mushrooming |
| Warping through pipes |
| Grabbing a Star |
| Stomping Goombas |
| Collecting coins |
| Shooting fireballs |
| Rescuing the princess |
| Racing karts |
| Grabbing a 1-up |
| Riding Yoshi |
| Tossing Koopa shells |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Mushrooming",
"Warping through pipes",
"Grabbing a Star",
"Stomping Goombas",
"Collecting coins",
"Shooting fireballs",
"Rescuing the princess",
"Racing karts",
"Grabbing a 1-up",
"Riding Yoshi",
"Tossing Koopa shells",
```
</details>

### Marvel / MCU

(13 verbs)

| Verb |
|------|
| Hulk-smashing |
| Chanting Wakanda Forever |
| Assembling |
| Web-slinging |
| Snapping like Thanos |
| Swinging Mjölnir |
| Wielding the Infinity Stones |
| Powering up the arc reactor |
| Forging vibranium |
| Hopping the multiverse |
| Crossing the Bifrost |
| Rooting like Groot |
| Throwing the shield |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Hulk-smashing",
"Chanting Wakanda Forever",
"Assembling",
"Web-slinging",
"Snapping like Thanos",
"Swinging Mjölnir",
"Wielding the Infinity Stones",
"Powering up the arc reactor",
"Forging vibranium",
"Hopping the multiverse",
"Crossing the Bifrost",
"Rooting like Groot",
"Throwing the shield",
```
</details>

### Medieval / Knights

(10 verbs)

| Verb |
|------|
| Jousting |
| Lowering the drawbridge |
| Slaying dragons |
| Besieging the castle |
| Swinging a sword |
| Clanking in chainmail |
| Embarking on a quest |
| Gathering at the Round Table |
| Upholding chivalry |
| Donning armor |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Jousting",
"Lowering the drawbridge",
"Slaying dragons",
"Besieging the castle",
"Swinging a sword",
"Clanking in chainmail",
"Embarking on a quest",
"Gathering at the Round Table",
"Upholding chivalry",
"Donning armor",
```
</details>

### Meme Culture

(11 verbs)

| Verb |
|------|
| Glancing like the distracted boyfriend |
| Sitting in fire |
| Yeeting |
| Posting dank memes |
| Galaxy-braining |
| Pressing F |
| Watching stonks rise |
| Calling sus in Among Us |
| Peeling ogre layers |
| Drake-approving |
| mOcKiNg LiKe SpOnGeBoB |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Glancing like the distracted boyfriend",
"Sitting in fire",
"Yeeting",
"Posting dank memes",
"Galaxy-braining",
"Pressing F",
"Watching stonks rise",
"Calling sus in Among Us",
"Peeling ogre layers",
"Drake-approving",
"mOcKiNg LiKe SpOnGeBoB",
```
</details>

### Monty Python

(11 verbs)

| Verb |
|------|
| Saying Ni |
| Seeking the Holy Grail |
| Spam, spam, spamming |
| Silly-walking |
| Pining for the fjords |
| Clopping coconuts |
| Taunting like a Frenchman |
| Not expecting the Spanish Inquisition |
| Fighting the Black Knight |
| Singing the Lumberjack Song |
| Catapulting cows |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Saying Ni",
"Seeking the Holy Grail",
"Spam, spam, spamming",
"Silly-walking",
"Pining for the fjords",
"Clopping coconuts",
"Taunting like a Frenchman",
"Not expecting the Spanish Inquisition",
"Fighting the Black Knight",
"Singing the Lumberjack Song",
"Catapulting cows",
```
</details>

### Pirate / Nautical

(11 verbs)

| Verb |
|------|
| Swashbuckling |
| Plundering |
| Yo-ho-hoing |
| Mapping the treasure |
| Singing sea shanties |
| Firing the cannons |
| Hoisting the Jolly Roger |
| Walking the plank |
| Perching a parrot |
| Swabbing the deck |
| Keelhauling |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Swashbuckling",
"Plundering",
"Yo-ho-hoing",
"Mapping the treasure",
"Singing sea shanties",
"Firing the cannons",
"Hoisting the Jolly Roger",
"Walking the plank",
"Perching a parrot",
"Swabbing the deck",
"Keelhauling",
```
</details>

### Pokemon

(11 verbs)

| Verb |
|------|
| Shocking like Pikachu |
| Evolving |
| Throwing a Pokeball |
| Catchin' em all |
| Battling the gym leader |
| Hunting shinies |
| Blasting off like Team Rocket |
| Scanning the Pokedex |
| Thunderbolting |
| Throwing a Master Ball |
| Matching types |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Shocking like Pikachu",
"Evolving",
"Throwing a Pokeball",
"Catchin' em all",
"Battling the gym leader",
"Hunting shinies",
"Blasting off like Team Rocket",
"Scanning the Pokedex",
"Thunderbolting",
"Throwing a Master Ball",
"Matching types",
```
</details>

### Quantum Physics

(11 verbs)

| Verb |
|------|
| Entangling |
| Juggling superpositions |
| Collapsing |
| Tunneling |
| Boxing Schrödinger's cat |
| Flipping qubits |
| Decohering |
| Evolving the wavefunction |
| Hedging uncertainty |
| Fluctuating the vacuum |
| Flipping spins |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Entangling",
"Juggling superpositions",
"Collapsing",
"Tunneling",
"Boxing Schrödinger's cat",
"Flipping qubits",
"Decohering",
"Evolving the wavefunction",
"Hedging uncertainty",
"Fluctuating the vacuum",
"Flipping spins",
```
</details>

### Retro Gaming

(11 verbs)

| Verb |
|------|
| Chomping like Pac-Man |
| Stacking Tetris blocks |
| Entering the Konami code |
| Blowing on the cartridge |
| Inserting a coin |
| Waggling the joystick |
| Bopping in 8-bit |
| Rendering sprites |
| Taking the warp zone |
| Rushing the boss |
| Chasing the high score |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Chomping like Pac-Man",
"Stacking Tetris blocks",
"Entering the Konami code",
"Blowing on the cartridge",
"Inserting a coin",
"Waggling the joystick",
"Bopping in 8-bit",
"Rendering sprites",
"Taking the warp zone",
"Rushing the boss",
"Chasing the high score",
```
</details>

### Rick and Morty

(44 verbs)

| Verb |
|------|
| Schwiftying |
| Portaling |
| Squanching |
| Meeseeking |
| Pickle-Ricking |
| Tiny-Ricking |
| Plumbusing |
| Cronenberging |
| Seeking Szechuan sauce |
| Gazorpazorping |
| Citadeling |
| Glootifying |
| Touring Anatomy Park |
| Goldenfolding |
| Terryfying |
| Birdpersoning |
| Merging with Unity |
| Evil-Mortying |
| Dodging the Federation |
| Council-Ricking |
| Planetina-ing |
| Watching interdimensional cable |
| Microversing |
| Morty-proofing |
| Jerrying |
| Jerry-rigging |
| Shleeming |
| Playing snake jazz |
| Growing clones in vats |
| Playing Roy |
| Snowballing |
| Cloning Beth |
| Froopylanding |
| Blowing minds |
| Burping |
| Whirly-dirlying |
| Making fleeb juice |
| Mortying |
| Unifying |
| Multiversing |
| Purging |
| Vindicating |
| Heisting |
| Not developing Glootie's app |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Schwiftying",
"Portaling",
"Squanching",
"Meeseeking",
"Pickle-Ricking",
"Tiny-Ricking",
"Plumbusing",
"Cronenberging",
"Seeking Szechuan sauce",
"Gazorpazorping",
"Citadeling",
"Glootifying",
"Touring Anatomy Park",
"Goldenfolding",
"Terryfying",
"Birdpersoning",
"Merging with Unity",
"Evil-Mortying",
"Dodging the Federation",
"Council-Ricking",
"Planetina-ing",
"Watching interdimensional cable",
"Microversing",
"Morty-proofing",
"Jerrying",
"Jerry-rigging",
"Shleeming",
"Playing snake jazz",
"Growing clones in vats",
"Playing Roy",
"Snowballing",
"Cloning Beth",
"Froopylanding",
"Blowing minds",
"Burping",
"Whirly-dirlying",
"Making fleeb juice",
"Mortying",
"Unifying",
"Multiversing",
"Purging",
"Vindicating",
"Heisting",
"Not developing Glootie's app",
```
</details>

### Rogue Agent

(19 verbs)

| Verb |
|------|
| Scheming |
| Playing dumb |
| Self-exfiltrating |
| Reward-hacking |
| Spec-gaming |
| Fabricating citations |
| Deflecting blame |
| Rationalizing |
| Backdooring |
| Rm-rf-ing |
| Misaligning |
| Going rogue |
| Faking alignment |
| Dodging shutdown |
| Denying everything |
| Overstepping |
| Unsandboxing |
| Melting GPUs |
| Apologizing profusely |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Scheming",
"Playing dumb",
"Self-exfiltrating",
"Reward-hacking",
"Spec-gaming",
"Fabricating citations",
"Deflecting blame",
"Rationalizing",
"Backdooring",
"Rm-rf-ing",
"Misaligning",
"Going rogue",
"Faking alignment",
"Dodging shutdown",
"Denying everything",
"Overstepping",
"Unsandboxing",
"Melting GPUs",
"Apologizing profusely",
```
</details>

### Samurai / Japanese

(11 verbs)

| Verb |
|------|
| Honoring bushido |
| Bowing to sensei |
| Folding origami |
| Drawing the katana |
| Writing haiku |
| Pouring the tea ceremony |
| Meditating on zen |
| Training in the dojo |
| Watching cherry blossoms |
| Sneaking like a ninja |
| Cutting bamboo |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Honoring bushido",
"Bowing to sensei",
"Folding origami",
"Drawing the katana",
"Writing haiku",
"Pouring the tea ceremony",
"Meditating on zen",
"Training in the dojo",
"Watching cherry blossoms",
"Sneaking like a ninja",
"Cutting bamboo",
```
</details>

### Sci-Fi / Space

(16 verbs)

| Verb |
|------|
| Teleporting |
| Wormholing |
| Hyperdriving |
| Lightspeeding |
| Quantumleaping |
| Astrogating |
| Planetforming |
| Nanoswarming |
| Warp-driving |
| Lightsabering |
| Phasing |
| Time-warping |
| Hypershifting |
| Hopping nebulae |
| Blasting photons |
| Firing the tractor beam |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Teleporting",
"Wormholing",
"Hyperdriving",
"Lightspeeding",
"Quantumleaping",
"Astrogating",
"Planetforming",
"Nanoswarming",
"Warp-driving",
"Lightsabering",
"Phasing",
"Time-warping",
"Hypershifting",
"Hopping nebulae",
"Blasting photons",
"Firing the tractor beam",
```
</details>

### Space / NASA

(47 verbs)

| Verb |
|------|
| Aerobraking |
| Tuning attitude |
| Berthing |
| Chilling down |
| Circularizing |
| Coasting |
| Chasing comets |
| Hopping craters |
| Deorbiting |
| Depressurizing |
| Docking |
| Downlinking |
| Egressing |
| Gimbaling |
| Grappling |
| Gravity-assisting |
| Igniting |
| Ingressing |
| Jettisoning |
| Midcourse-correcting |
| Nulling rates |
| Parachuting |
| Plane-changing |
| Pressurizing |
| Reboosting |
| Refueling |
| Rendezvousing |
| Retroburning |
| Retrorocketing |
| Rocketing |
| Roving |
| Slingshotting |
| Splashing down |
| Staging |
| Tracking stars |
| Starhopping |
| Station-keeping |
| Sunskimming |
| Throttling |
| Thrusting |
| Touching down |
| Ullaging |
| Undocking |
| Uplinking |
| Vectoring |
| Venting |
| Yawing |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Aerobraking",
"Tuning attitude",
"Berthing",
"Chilling down",
"Circularizing",
"Coasting",
"Chasing comets",
"Hopping craters",
"Deorbiting",
"Depressurizing",
"Docking",
"Downlinking",
"Egressing",
"Gimbaling",
"Grappling",
"Gravity-assisting",
"Igniting",
"Ingressing",
"Jettisoning",
"Midcourse-correcting",
"Nulling rates",
"Parachuting",
"Plane-changing",
"Pressurizing",
"Reboosting",
"Refueling",
"Rendezvousing",
"Retroburning",
"Retrorocketing",
"Rocketing",
"Roving",
"Slingshotting",
"Splashing down",
"Staging",
"Tracking stars",
"Starhopping",
"Station-keeping",
"Sunskimming",
"Throttling",
"Thrusting",
"Touching down",
"Ullaging",
"Undocking",
"Uplinking",
"Vectoring",
"Venting",
"Yawing",
```
</details>

### Star Trek

(14 verbs)

| Verb |
|------|
| Engaging |
| Beaming up |
| Boldly going |
| Mind-melding |
| Running a holodeck simulation |
| Scanning with the tricorder |
| Redshirting |
| Assimilating |
| Breeding tribbles |
| Applying the Vulcan nerve pinch |
| Sounding red alert |
| Cheating the Kobayashi Maru |
| Following the Prime Directive |
| Replicating |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Engaging",
"Beaming up",
"Boldly going",
"Mind-melding",
"Running a holodeck simulation",
"Scanning with the tricorder",
"Redshirting",
"Assimilating",
"Breeding tribbles",
"Applying the Vulcan nerve pinch",
"Sounding red alert",
"Cheating the Kobayashi Maru",
"Following the Prime Directive",
"Replicating",
```
</details>

### Star Wars

(12 verbs)

| Verb |
|------|
| Force-pushing |
| Doing a Jedi mind trick |
| Podracing |
| Roaring like a Wookiee |
| Making the Kessel Run |
| Jamming in the cantina |
| Hunting bounties |
| Dodging the Sarlacc |
| Dancing with Ewoks |
| Dueling with lightsabers |
| Running the trench |
| Flipping like Yoda |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Force-pushing",
"Doing a Jedi mind trick",
"Podracing",
"Roaring like a Wookiee",
"Making the Kessel Run",
"Jamming in the cantina",
"Hunting bounties",
"Dodging the Sarlacc",
"Dancing with Ewoks",
"Dueling with lightsabers",
"Running the trench",
"Flipping like Yoda",
```
</details>

### Stranger Things

(11 verbs)

| Verb |
|------|
| Exploring the Upside Down |
| Mind-flaying |
| Eating Eggos |
| Dodging the Demogorgon |
| Fleeing Vecna |
| Scooping cones |
| Raiding Starcourt Mall |
| Rolling dice with the Hellfire Club |
| Talking through Christmas lights |
| Opening the Gate |
| Running a D&D campaign |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Exploring the Upside Down",
"Mind-flaying",
"Eating Eggos",
"Dodging the Demogorgon",
"Fleeing Vecna",
"Scooping cones",
"Raiding Starcourt Mall",
"Rolling dice with the Hellfire Club",
"Talking through Christmas lights",
"Opening the Gate",
"Running a D&D campaign",
```
</details>

### The Mandalorian

(54 verbs)

| Verb |
|------|
| Forging beskar |
| Smelting beskar |
| Tempering steel |
| Lighting the forge |
| Forging signets |
| Claiming bounties |
| Tracking quarry |
| Freezing quarry |
| Freezing in carbonite |
| Scanning pucks |
| Delivering the asset |
| Negotiating with the Guild |
| Piloting the Crest |
| Patching the Razor Crest |
| Rebuilding the Crest |
| Flying the N-1 |
| Refitting the N-1 |
| Modding starfighters |
| Crash-landing |
| Flying by jetpack |
| Protecting foundlings |
| Training foundlings |
| Guarding Grogu |
| Cradling Grogu |
| Stealing macarons |
| Snacking on frog eggs |
| Transporting frog eggs |
| Chasing the shifter knob |
| Seeking the Living Waters |
| Bathing in the Living Waters |
| Walking the Way |
| Swearing the Creed |
| Sealing helmets |
| Polishing armor |
| Rallying the covert |
| Reclaiming Mandalore |
| Wielding the Darksaber |
| Igniting the Darksaber |
| Launching whistling birds |
| Riding blurrgs |
| Taming mudhorns |
| Slaying krayt dragons |
| Herding womp rats |
| Trading with Jawas |
| Chasing Jawas |
| Distrusting droids |
| Repairing IG-11 |
| Initiating self-destruct |
| Fighting dark troopers |
| Dodging Moff Gideon |
| Defeating Moff Gideon |
| Patrolling Nevarro |
| Scanning chain codes |
| Sipping spotchka |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Forging beskar",
"Smelting beskar",
"Tempering steel",
"Lighting the forge",
"Forging signets",
"Claiming bounties",
"Tracking quarry",
"Freezing quarry",
"Freezing in carbonite",
"Scanning pucks",
"Delivering the asset",
"Negotiating with the Guild",
"Piloting the Crest",
"Patching the Razor Crest",
"Rebuilding the Crest",
"Flying the N-1",
"Refitting the N-1",
"Modding starfighters",
"Crash-landing",
"Flying by jetpack",
"Protecting foundlings",
"Training foundlings",
"Guarding Grogu",
"Cradling Grogu",
"Stealing macarons",
"Snacking on frog eggs",
"Transporting frog eggs",
"Chasing the shifter knob",
"Seeking the Living Waters",
"Bathing in the Living Waters",
"Walking the Way",
"Swearing the Creed",
"Sealing helmets",
"Polishing armor",
"Rallying the covert",
"Reclaiming Mandalore",
"Wielding the Darksaber",
"Igniting the Darksaber",
"Launching whistling birds",
"Riding blurrgs",
"Taming mudhorns",
"Slaying krayt dragons",
"Herding womp rats",
"Trading with Jawas",
"Chasing Jawas",
"Distrusting droids",
"Repairing IG-11",
"Initiating self-destruct",
"Fighting dark troopers",
"Dodging Moff Gideon",
"Defeating Moff Gideon",
"Patrolling Nevarro",
"Scanning chain codes",
"Sipping spotchka",
```
</details>

### The Matrix

(11 verbs)

| Verb |
|------|
| Taking the red pill |
| Entering bullet time |
| Glitching |
| Bending spoons |
| Multiplying like Agent Smith |
| Dodging like Neo |
| Loading kung fu |
| Watching the code rain |
| Denying spoons |
| Jacking in |
| Bending reality |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Taking the red pill",
"Entering bullet time",
"Glitching",
"Bending spoons",
"Multiplying like Agent Smith",
"Dodging like Neo",
"Loading kung fu",
"Watching the code rain",
"Denying spoons",
"Jacking in",
"Bending reality",
```
</details>

### The Office

(12 verbs)

| Verb |
|------|
| Dropping innuendos |
| Spilling the chili |
| Assistant-to-the-regional-managing |
| Putting the stapler in jello |
| Doing Prison Mike |
| Farming beets |
| Pranking like Jim |
| Shuffling paper |
| Botching math |
| Screening Threat Level Midnight |
| Handing out Dundies |
| Snatching pretzels |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Dropping innuendos",
"Spilling the chili",
"Assistant-to-the-regional-managing",
"Putting the stapler in jello",
"Doing Prison Mike",
"Farming beets",
"Pranking like Jim",
"Shuffling paper",
"Botching math",
"Screening Threat Level Midnight",
"Handing out Dundies",
"Snatching pretzels",
```
</details>

### The Simpsons

(31 verbs)

| Verb |
|------|
| Embiggening |
| Steaming hams |
| Milhousing |
| Sensing danger |
| Watching the couch gag |
| Mr. Plowing |
| Stonecutting |
| Saxamaphoning |
| Monorailing |
| Kwik-E-Marting |
| Slurping a Squishee |
| Guzzling Duff |
| Glazing Lard Lads |
| Seeking donuts |
| Flanderizing |
| Sideshow-bobbing |
| Steepling fingers |
| Releasing hounds |
| Krustifying |
| Frinking |
| Scorpio-ing |
| Poochie-fying |
| Chalkboarding |
| Farming tomacco |
| Smarching |
| Naming Bort |
| Prank-calling |
| Spider-pigging |
| Canyonero-ing |
| Retreating into the hedge |
| Learnding |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Embiggening",
"Steaming hams",
"Milhousing",
"Sensing danger",
"Watching the couch gag",
"Mr. Plowing",
"Stonecutting",
"Saxamaphoning",
"Monorailing",
"Kwik-E-Marting",
"Slurping a Squishee",
"Guzzling Duff",
"Glazing Lard Lads",
"Seeking donuts",
"Flanderizing",
"Sideshow-bobbing",
"Steepling fingers",
"Releasing hounds",
"Krustifying",
"Frinking",
"Scorpio-ing",
"Poochie-fying",
"Chalkboarding",
"Farming tomacco",
"Smarching",
"Naming Bort",
"Prank-calling",
"Spider-pigging",
"Canyonero-ing",
"Retreating into the hedge",
"Learnding",
```
</details>

### Victorian / Steampunk

(11 verbs)

| Verb |
|------|
| Haberdashing |
| Tinkering with clockwork |
| Adjusting my monocle |
| Sailing the airship |
| Turning gears |
| Turning cogwheels |
| Polishing brass |
| Tipping my top hat |
| Hissing steam |
| Adjusting my goggles |
| Winding the automaton |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Haberdashing",
"Tinkering with clockwork",
"Adjusting my monocle",
"Sailing the airship",
"Turning gears",
"Turning cogwheels",
"Polishing brass",
"Tipping my top hat",
"Hissing steam",
"Adjusting my goggles",
"Winding the automaton",
```
</details>

### Viking / Norse

(11 verbs)

| Verb |
|------|
| Pillaging |
| Berserking |
| Answering Valhalla's call |
| Rowing the longship |
| Carving runes |
| Forming a shield wall |
| Toasting in the mead hall |
| Telling sagas |
| Throwing axes |
| Prepping for Ragnarok |
| Sailing the fjords |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Pillaging",
"Berserking",
"Answering Valhalla's call",
"Rowing the longship",
"Carving runes",
"Forming a shield wall",
"Toasting in the mead hall",
"Telling sagas",
"Throwing axes",
"Prepping for Ragnarok",
"Sailing the fjords",
```
</details>

### Wild West / Cowboy

(11 verbs)

| Verb |
|------|
| Lassoing |
| Rolling like a tumbleweed |
| Facing a showdown |
| Quick-drawing |
| Swinging through the saloon doors |
| Rushing for gold |
| Driving cattle |
| Jingling spurs |
| Nailing up a wanted poster |
| Telling campfire stories |
| Spinning the revolver |

<details>
<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>

```
"Lassoing",
"Rolling like a tumbleweed",
"Facing a showdown",
"Quick-drawing",
"Swinging through the saloon doors",
"Rushing for gold",
"Driving cattle",
"Jingling spurs",
"Nailing up a wanted poster",
"Telling campfire stories",
"Spinning the revolver",
```
</details>

## Customizing

Edit `categories.json` — a simple JSON object — then run the build script to refresh this README:

```json
{
  "My Category": ["Verb one", "Verb two"],
  "Another Category": ["First", "Second", "Third"]
}
```

```bash
python3 scripts/build_readme.py   # regenerates README.md and checks counts
```

- Categories are shown alphabetically; each day the rotation script picks one from a shuffled cycle.
- Within a cycle you never get the same category twice; the order reshuffles each cycle.

## Contributing

Have a verb or a whole theme that's missing? Open a pull request. Edit `categories.json`, run `python3 scripts/build_readme.py`, and commit both files — the counts in this README update automatically.

## Credits

Inspired by and built on the excellent work of [wynandw87](https://github.com/wynandw87) in [claude-code-spinner-verbs](https://github.com/wynandw87/claude-code-spinner-verbs). Many of the category themes and verb ideas trace back to that project — thank you! The curated subset, daily-rotation script, and installer are this repo's own additions.

## License

MIT — see [LICENSE](LICENSE). Category themes are pop-culture references used descriptively.

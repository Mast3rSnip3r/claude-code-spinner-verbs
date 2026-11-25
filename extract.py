import re, sys, json
readme, out = sys.argv[1], sys.argv[2]
want = """Back to the Future (10)
Breaking Bad (73)
Cat Behavior (30)
DC Comics (11)
Disney / Pixar (12)
Doctor Who (10)
Dune (13)
Futurama (43)
Gaming (13)
Harry Potter (13)
Jurassic Park (10)
Lord of the Rings (13)
The Mandalorian (54)
Mario / Nintendo (11)
Marvel / MCU (13)
The Matrix (11)
Medieval / Knights (10)
Meme Culture (11)
Monty Python (11)
The Office (12)
Pirate / Nautical (11)
Pokemon (11)
Quantum Physics (11)
Retro Gaming (11)
Rick and Morty (44)
Rogue Agent (19)
Samurai / Japanese (11)
Sci-Fi / Space (16)
The Simpsons (31)
Space / NASA (47)
Star Trek (14)
Star Wars (12)
Stranger Things (11)
Victorian / Steampunk (11)
Viking / Norse (11)
Wild West / Cowboy (11)""".splitlines()
text = open(readme, encoding="utf-8").read()
secs = re.split(r'^### ', text, flags=re.M)[1:]
by = {}
for s in secs:
    head, _, body = s.partition("\n")
    if "| Verb |" not in body.split("<details>")[0]:
        continue
    rows = re.findall(r'^\| (.+?) \|$', body.split("<details>")[0], flags=re.M)
    rows = [r for r in rows if r != "Verb"]
    by.setdefault(head.strip(), rows)
cats = {}
for w in want:
    name = re.sub(r' \(\d+\)$', '', w); n = int(re.search(r'\((\d+)\)$', w).group(1))
    rows = by.get(w)
    if rows is None: print("MISSING", w); continue
    if len(rows) != n: print("COUNT MISMATCH", w, len(rows))
    cats[name] = rows
json.dump(cats, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(cats), "categories,", sum(map(len, cats.values())), "verbs")
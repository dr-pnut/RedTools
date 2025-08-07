adjectives = [line.strip() for line in open("adjectives.txt")]
nouns = [line.strip() for line in open("nouns.txt")]

total = len(adjectives) * len(nouns) * 1000
count = 0

with open("SpectrumDictionary.txt", "w") as f:
    for adj in adjectives:
        for noun in nouns:
            for i in range(1000):
                password = f"{adj}{noun}{i:03d}"
                f.write(password + "\n")
                count += 1
                if count % 10000 == 0 or count == total:
                    print(f"[{count} / {total}] passwords written")

print("Done.")

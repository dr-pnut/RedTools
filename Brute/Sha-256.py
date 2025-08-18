import hashlib

target = input("Enter target hash: ").strip()

src = input("Is the target from a (f)ile or (s)tring? [f/s]: ").lower()
if src == 'f':
    with open(input("Enter path to hash file: "), encoding="utf-8") as f:
        target = f.readline().strip()

dict_path = input("Enter path to dictionary file: ")

for line in open(dict_path, encoding="utf-8"):
    pwd = line.strip()
    if hashlib.sha256(pwd.encode()).hexdigest() == target:
        print(f"Password found: {pwd}")
        with open("cracked", "w", encoding="utf-8") as out:
            out.write(pwd + "\n")
        break
else:
    print("Password not found.")

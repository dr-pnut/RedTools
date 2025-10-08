# Spectrum Wi-Fi Dictionary Generator

This Python script generates a wordlist of possible Spectrum Wi-Fi passwords using the common format:

    {adjective}{noun}###

For example:
    cooldog042
    fastcloud999
    brightcar007

This format is often used by Spectrum routers by default, so this generator can help for educational or authorized testing purposes.

---

How It Works

1. Loads adjectives from adjectives.txt
2. Loads nouns from nouns.txt
3. Combines each adjective + noun + a number from 000 to 999
4. Writes all combinations to SpectrumDictionary.txt

Progress updates will print every 10,000 combinations to the terminal.

---

Usage Instructions

1. Ensure you have Python 3 installed on your computer.
2. Place the script file, adjectives.txt, and nouns.txt all in the same folder.
3. Run the script from a terminal or command prompt:

    python spectrum_generator.py

4. Wait for the script to finish. The full wordlist will be saved in SpectrumDictionary.txt in the same folder.

---

Customizing the Wordlists

You can edit adjectives.txt and nouns.txt to add or remove words.

Each file should have one word per line. For example:

adjectives.txt:
    quick
    bright
    silent

nouns.txt:
    tiger
    cloud
    guitar

The total number of generated passwords will be:

    number_of_adjectives × number_of_nouns × 1000

So, with 100 adjectives and 100 nouns, you will get 10,000,000 combinations.

---

Example Output

    quicktiger000
    quicktiger001
    ...
    silentguitar999

---

Intended Use

This script is designed for educational purposes, such as:

- Learning about common Wi-Fi password patterns
- Generating custom wordlists for authorized security testing
- Understanding password generation schemes

Please use responsibly and only on networks where you have permission to test.

---

Acknowledgments

Special thanks to user [nova-sec](https://github.com/nova-sec) and their project [SpectrumSniper](https://github.com/nova-sec/SpectrumSniper) for providing the nouns.txt and adjectives.txt files used in this script.

import math
import mmh3
from bitarray import bitarray


class BloomFilter:

    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(
            self.size, items_count
        )

        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    @staticmethod
    def get_size(n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def get_hash_count(m, n):
        k = (m / n) * math.log(2)
        return int(k)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            if self.bit_array[digest] == 0:
                return False

        return True


# Main program
if __name__ == "__main__":

    words_to_add = [
        "war", "gloomy", "humanity", "abundant", "bloom",
        "coherent", "cohesive", "bluff", "bolster", "hate",
        "racism", "bonus", "abounds", "genial",
        "geeksforgeeks", "nuke", "hurt", "twitter",
        "cheater", "generosity", "facebook", "abundance"
    ]

    test_words = [
        "war", "gloomy", "humanity", "abundant", "bloom",
        "coherent", "cohesive", "bluff", "bolster", "hate",
        "racism", "bonus", "abounds", "genial",
        "geeksforgeeks", "nuke", "hurt", "twitter",
        "cheater", "generosity", "facebook", "abundance"
    ]

    bloom = BloomFilter(items_count=100, fp_prob=0.05)

    print(f"Size of bit array: {bloom.size}")
    print(f"False positive probability: {bloom.fp_prob}")
    print(f"Number of hash functions: {bloom.hash_count}")

    # Add words to the Bloom Filter
    for word in words_to_add:
        bloom.add(word)

    # Check words
    print("\nChecking words:")

    for word in test_words:
        result = bloom.check(word)

        if result:
            print(f"'{word}' is probably present!")
        else:
            print(f"'{word}' is definitely not present!")

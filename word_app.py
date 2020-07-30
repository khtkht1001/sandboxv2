"""Counting words"""

def main():
    print(count_words("A fox jumps over a ledge and falls flat"))

def count_words(phrase):
    words = phrase.split()
    return len(words)

if __name__ == '__main__':
    main()
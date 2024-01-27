def main():
    a = open("words.txt", encoding="utf-8"); word = a.read().split(); print(min(word), max(word))


if __name__ == "__main__":
    main()
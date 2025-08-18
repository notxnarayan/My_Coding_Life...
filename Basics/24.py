
def printsent(*args):
    sent = ""
    for i in args:
        print(i)

        sent += i
        sent += " "
    print(str(sent))

words = []
while True:
    word = input("Enter the word (exit to quit): ")
    if "exit" in word:
        break
    words.append(word)
    print(words)

printsent(*words)

import time

ascii_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

def encode(key, message):
    encodMess = ''

    for i in range(len(message)):
        letM = message[i]
        letK = key[i % len(key)]
        encodLet = ascii_letters.index(letM) + ascii_letters.index(letK)
        if encodLet > 25: encodLet -= 26
        encodMess += ascii_letters[encodLet]

    with open('encodedMessage.txt', 'w') as f:
        f.write(encodMess)

def decode(key, encodMess):
    decodMess = ''

    for i in range(len(encodMess)):
        letM = encodMess[i]
        letK = key[i % len(key)]
        decodLet = ascii_letters.index(letM) - ascii_letters.index(letK)
        if decodLet < 0: decodLet += 26
        decodMess += ascii_letters[decodLet]

    with open('decodedMessage.txt', 'w') as f:
        f.write(decodMess)


if __name__ == '__main__':
    with open('message.txt') as f:
        message = f.read()

    start = time.time()
    message = message.lower().replace(' ','').replace(',','').replace('.','').replace('-','').replace('?','').replace('?','')

    encode('dog', message)
    end = time.time()
    runtime = end - start
    print(f"Час шифрування: {runtime} с")

    with open('encodedMessage.txt') as f:
        message = f.read()

    start = time.time()
    decode('dog', message)
    end = time.time()
    runtime = end - start
    print(f"Час розшифрування: {runtime} с")








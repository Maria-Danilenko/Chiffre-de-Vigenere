import time

ascii_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encode(key, message):
    encodMess = ''

    for i in range(len(message)):
        letM = message[i]
        letK = key[i % len(key)]
        encodLet = ascii_letters.index(letM) + ascii_letters.index(letK)
        if encodLet > 26: encodLet -= 27
        encodMess += ascii_letters[encodLet]

    print(f'Зашифроване повідомлення: {encodMess}')
    return encodMess

def decode(key, encodMess):
    decodMess = ''

    for i in range(len(encodMess)):
        letM = encodMess[i]
        letK = key[i % len(key)]
        decodLet = ascii_letters.index(letM) - ascii_letters.index(letK)
        if decodLet < 0: decodLet += 27
        decodMess += ascii_letters[decodLet]
      
    print(f'Розшифроване повідомлення: {decodMess}')


if __name__ == '__main__':
    with open('message.txt') as f:
        message = f.read()

    print(f'Початковий вигляд повідомлення: {message}')

    start = time.time()
    message = message.lower().replace(',','').replace('.','').replace('-','').replace('?','').replace('?','')

    encodMess = encode('dog', message)
    end = time.time()
    runtime1 = end - start

    start = time.time()
    decode('dog', encodMess)
    end = time.time()
    runtime2 = end - start

    print(f"Час шифрування: {runtime1} с")
    print(f"Час розшифрування: {runtime2} с")

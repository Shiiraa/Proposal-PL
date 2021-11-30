import Newbies

while True:
    text = input('newbie > ')
    result, error = Newbies.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
import dict

sw = True
while sw:
    mode = input("choose encode or decode morse:")
    words = input("Type word:").upper()
    output = ''
    if mode == "decode":
        for word in words:
            output += dict.decode[word]
            output += ' '
    else:
        for word in words:
            output += dict.encode[word]
            output += ' '
    print(f"result:{output}")
    conti = input("type ok to continue:")
    if conti == 'ok':
        sw = True
    else:
        sw = False

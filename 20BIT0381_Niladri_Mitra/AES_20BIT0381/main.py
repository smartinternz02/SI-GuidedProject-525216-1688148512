if __name__ == '__main__':

    import os
    import time

    import aes128
    
    print('Step 1:')
    while True:
        print('Press 1 for Encryption smth and 2 for Decryption:')
        way = input()
        if way not in ['1', '2']:
            print('Action denied')
            continue
        else:
            break
    print()

    print('Step 2:')
    while True:
        print('Enter the full name of file:')
        input_path = os.path.abspath(input())

        if os.path.isfile(input_path):
            break
        else:
            print('This is not a file!')
            continue
    print()

    print('Step 3:')
    while True:
        print('Enter your key for Encryption/Decryption(it should be less than 16 symbols):')
        key = input()
        
        if len(key) > 16:
            print('Invalid Key! Use less than 16 symbols')
            continue
        
        for symbol in key:
            if ord(symbol) > 0xff:
                print('Invalid Key! Use only latin alphabet and numbers')
                continue
        
        break
    print('\r\nPlease wait...')

    time_before = time.time()

    # Input data
    with open(input_path, 'rb') as f:
        data = f.read()    

    if way == '1':
        crypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)
                del temp[:]
        else:
    

            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)

        out_path = os.path.join(os.path.dirname(input_path) , 'crypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(crypted_data))

    else: # if way == '2'
        decrypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                decrypted_part = aes128.decrypt(temp, key)
                decrypted_data.extend(decrypted_part)
                del temp[:] 
        else:
             
            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                decrypted_part = aes128.encrypt(temp, key)
                decrypted_data.extend(crypted_part) 

        out_path = os.path.join(os.path.dirname(input_path) , 'decrypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(decrypted_data))

    time_after = time.time()
    
print('Encryption Sucessful! Encrypted file: ', out_path, '--', time_after - time_before, ' seconds')
print('In case of error review the entered password and try again!')
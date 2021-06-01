import time
import PySimpleGUI as sg

sg.theme('reddit')

def simpleEncrypt( plainText, key ):
    columns = [''] * key
    chPos = 0
    textLength = len(plainText)
    while chPos < textLength:
        for i in range(key):
            if chPos < textLength:
                columns[i] = columns[i] + plainText[chPos]
                chPos += 1
            else:
                columns[i] += ' '
    cipherText = ''
    for strs in columns:
        cipherText += strs
    return cipherText

def simpleDecrypt( cipherText, key ):
    plainText = ''
    rows = int(len(cipherText) / key)
    for i in range(rows):
        for j in range(key):
            position = i + rows * j
            plainText += cipherText[position]
    return plainText

homeLO = [
            [sg.Text('Welcome to the Transposition Cypher', font='Courier 10')],   
            [sg.Button('Create'),sg.Button('Read'), sg.Exit()]
        ] 

homeWindow = sg.Window('Transposition Cyphers', homeLO, size=(400,100))

while True: # The Event Loop
    event, values = homeWindow.read() 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    elif event == 'Create':
        # create new window for creating encrypted files
        createLO = [
                    [sg.Text('Filename:', font='Courier 10'),sg.Input(key='-FN-')],      
                    [sg.Text('Plaintext:', font='Courier 10'),sg.Input(key='-PT-')],
                    [sg.Text('Key (>1):', font='Courier 10'),sg.Input(key='-PK-')],      
                    [sg.Button('Create'), sg.Button('Exit')],
                    [sg.Text('Waiting.',key='-SB-',font='Courier 10',size=(42,1))]
                ]
        createWindow = sg.Window('Create your file.', createLO)

        while True: # The Event Loop
            event, values = createWindow.read() 
            # print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                createWindow.close()
                break
            elif event == 'Create':
                # TO DO - Hash function to allow string keys
                try:
                    pk = int(values['-PK-'])
                    if pk > 1:
                        cipherText = simpleEncrypt( values['-PT-'], int(values['-PK-']) )
                        newFile = open(values['-FN-']+".txt","w")
                        newFile.write(cipherText)
                        newFile.close()
                        createWindow['-SB-'].update("File created. Exit or create another file.")
                    else:
                        createWindow['-SB-'].update("Key needs to be larger than 1.")
                except:
                    createWindow['-SB-'].update("Key needs to be a number greater than 1.")

    elif event == 'Read':
        # create new window for reading encrypted files
        readLO = [
                    [sg.Text('Decrypt or Encrypt a text file on your PC', font='Courier 10')],
                    [sg.Text('Filename:', font='Courier 10'),sg.Input(key='-FN-')],
                    [sg.Text('Key:', font='Courier 10'),sg.Input(key='-PK-')],      
                    [sg.Button('Decrypt'), sg.Button('Encrypt'), sg.Button('Exit')],
                    [sg.Text('Waiting.',key='-SB-',font='Courier 10',size=(42,1))]
                ]

        readWindow = sg.Window('Read your files.', readLO)
        
        while True: # The Event Loop
            event, values = readWindow.read() 
            # print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                readWindow.close()
                break
            elif event == 'Decrypt':
                # TO DO - Add decrypt file functionality.
                try:
                    pk = int(values['-PK-'])
                    if pk > 1:
                        fname = values['-FN-']
                        readFile = open(fname+".txt","r")
                        cipherText = readFile.read()
                        plainText = simpleDecrypt( cipherText, pk )
                        newFile = open(fname+"-dec.txt","w")
                        newFile.write(plainText)
                        newFile.close()
                        readWindow['-SB-'].update("Decryption done. Exit or try again.")
                    else:
                        readWindow['-SB-'].update("Key needs to be larger than 1.")
                except:
                    readWindow['-SB-'].update("Key needs to be a number greater than 1.")
            
            elif event == 'Encrypt':
                # TO DO - Add create encrypted file functionality.
                try:
                    pk = int(values['-PK-'])
                    if pk > 1:
                        fname = values['-FN-']
                        readFile = open(fname+".txt","r")
                        plainText = readFile.read()
                        readFile.close()
                        cipherText = simpleEncrypt( plainText, pk )
                        # Write the cipherText to a file.
                        newFile = open(fname+"-enc.txt","w")
                        newFile.write(cipherText)
                        newFile.close()
                        readWindow['-SB-'].update("Encryption done. Exit or encrypt again.")
                    else:
                        readWindow['-SB-'].update("Key needs to be larger than 1.")
                except:
                    readWindow['-SB-'].update("Key needs to be a number greater than 1.")

homeWindow.close()


        
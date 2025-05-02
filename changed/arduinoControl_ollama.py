import time


import serial
from ollama import chat
from ollama import ChatResponse


def f(text):
    response: ChatResponse = chat(model='llama3.2',         messages=[
            {"role": "system", "content": "to turn the servo you have to give me only a number from 0 to 180 and there should be no other characters"},
            {"role": "user", "content": text},
        ])

    s=response.message.content
    print(s)
    try:
        a=int(s)
    except:
        a=-1
    return a

ser = serial.Serial(port='COM3', baudrate=9600) # відкрити порт COM
time.sleep(2)
print(ser.portstr) # перевірити чи порт використовується


while True:
    text = input("Enter a command (e.g., 'Move servo to 90 degrees'): ")
    
    if text == 'exit' or text == 'Exit':
        ser.close()
        exit(0)
    
    a=f(text)
    if a!=-1:
        print(a)
        ser.write(str(a).encode()+b"\n")
        time.sleep(1)

    
ser.close() # закрити порт
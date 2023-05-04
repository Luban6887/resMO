import serial
import psutil

portCNT = 0 
ardStart = False
while True: #Finding Connected Port Of Arduino
    try:
        print("Connecting To Hardware...")
        portName = "COM"+str(portCNT)
        AP = serial.Serial(str(portName),timeout=1)
        if AP.isOpen():
            print(f"Connected To The {portName} Port")
            ardStart = True
            break
    except:
        portCNT += 1
        if portCNT == 100:
            print("Please Sure That Device is Connected")
            print("Try Again")
            break

if ardStart == True:
    while True:
        try:
            ram_usg = psutil.virtual_memory()[2]
            ram_usg = int(ram_usg)
            ram_usg = str(ram_usg)
            if len(ram_usg) == 1:
                ram_usg = "00"+ram_usg
            if len(ram_usg) == 1:
                ram_usg = "00"+ram_usg

            cpu_usg = psutil.cpu_percent(1)
            cpu_usg =int(cpu_usg)
            
            x = str(ram_usg)+" "+str(cpu_usg)
            x1 = len(x)
            y = 32-x1
            z = x + ' '*y
            
            AP.write(str.encode(z))
        except:
            break
#Mandatory Libraries
import soundfile as sf
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft

fileToProcess = "myTel.wav"

def numSearch(array, number): #Function for searching numbers in a dictionary
    offset = 5
    for i in range(number - offset, number + offset):
        if i in array:
            return True
    return False

#Storing DTMF table in a Dictionary
DTMF_TABLE = {
    '1': [1209, 697],
    '2': [1336, 697],
    '3': [1477, 697],
    'A': [1633, 697],

    '4': [1209, 770],
    '5': [1336, 770],
    '6': [1477, 770],
    'B': [1633, 770],

    '7': [1209, 852],
    '8': [1336, 852],
    '9': [1477, 852],
    'C': [1633, 852],

    '*': [1209, 941],
    '0': [1336, 941],
    '#': [1477, 941],
    'D': [1633, 941],
} 

n = 11
numResult = []

###########################
#PLOTTING THE WHOLE NUMBER#
###########################
tel, fs= sf.read(fileToProcess)
time = np.linspace(
    0,
    len(tel) / fs,
    num = len(tel)
)

plt.clf()
plt.title(fileToProcess + " Total Plot")
plt.xlabel("Time")
plt.plot(time, tel)
plt.show()

plt.clf()
plt.title(fileToProcess + " Total Stem")
plt.xlabel("Time")
plt.stem(time, tel)
plt.show()
  
def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]

d = math.floor(len(tel)/n)
telSplitted = list(divide_chunks(tel, d)) #Splitting the buttons into different arrays

#Confirming the last item of the list is not an excess
nI = len(telSplitted)-1
if len(telSplitted[nI]) != len(telSplitted[nI-1]):
    telSplitted.pop(nI)
else:
    pass

flag = 1
for i in telSplitted:
    fourier = np.fft.fft(i, 8000)#Fourier Transform at samplerate 8000
    for j in range(len(fourier)):
        fourier[j] = int(np.absolute(fourier[j]))

    #Lower Bound for filtering
    lower = 20*np.average(fourier)

    #filtering fourier transformed data
    filtered = []
    for j in range(len(fourier)):
        if (fourier[j] > lower):
            filtered.append(j)

    #What is the Pressed Button?
    for num,freq in DTMF_TABLE.items():
        if (numSearch(filtered, freq[0]) and numSearch(filtered, freq[1])):
            numResult.append(num)
    
    time = np.linspace(
        0,
        len(i) / fs,
        num = len(i)
    )
    if flag == 1:
        print("1" + "st dialled button is: " + numResult[flag-1])
    elif flag == 2:
        print("2" + "nd dialled button is: " + numResult[flag-1])
    elif flag == 3:
        print("3" + "rd dialled button is: " + numResult[flag-1])
    else:
        print(str(flag) + "th dialled button is: " + numResult[flag-1])

    
        
    
    plt.clf()
    plt.title(str(flag) + ". Dialled Button")
    plt.xlabel("Time")
    plt.plot(time, i)
    plt.show()
    flag = flag + 1
    
    

print("Whole Dialled Number: ")
print("".join(numResult))


#mandatory libraries for audio recording and convolution
from matplotlib.colors import same_color
import pyaudio
import numpy as np
from scipy.signal.signaltools import convolve
import sounddevice as sd
import matplotlib.pyplot as plt

########################################
#my convolution function (1st QUESTION)#
########################################

def myconv(x,n,y,m):
    len_conv = n + m - 1
    rev_y = y[::-1].copy() #reversing the 2nd array for the flip and shift
    resultArr = np.zeros(len_conv)
    if n>=m: #selecting the shortest signal to shift
        dummy = np.zeros(n)
        for i in range(m):
            dummy[0] = rev_y[(m-1)-i] #using a temporary list to shift
            resultArr[i] = np.dot(x, dummy) #using numpy.dot() function to get product of vectors faster
            if i != m-1:
                dummy = np.roll(dummy,1)
        if m != n:
            for i in range(n-m):
                dummy = np.roll(dummy,1)
                resultArr[i+m] = np.dot(x, dummy)
        for i in range(m-1):
            dummy = np.roll(dummy,1)
            dummy[0] = 0
            resultArr[len_conv-m+1+i] = np.dot(x, dummy)
    else:
        dummy = np.zeros(m)
        for i in range(n):
            dummy[0] = rev_y[(n-1)-i]
            resultArr[i] = np.dot(y, dummy)
            if i != n-1:
                dummy = np.roll(dummy,1)
        if m != n:
            for i in range(m-n):
                dummy = np.roll(dummy,1)
                resultArr[i+n] = np.dot(y, dummy)
        for i in range(n-1):
            dummy = np.roll(dummy,1)
            dummy[0] = 0
            resultArr[len_conv-n+1+i] = np.dot(y, dummy)

    return resultArr, len_conv

#########################
#Plotting (2nd QUESTION)#
#########################

my_convArr, len_conv = myconv([1,5,3,7,4], 5, [3,1,5,7,3], 5)
plt.plot(my_convArr, label = "x(n) * y(m)")
plt.plot([1,5,3,7,4], label = "x(n)")
plt.plot([3,1,5,7,3], label = "y(m)")
plt.xlim(0, len_conv)
plt.title("myconv() Function on 1st Dataset")
plt.legend()
plt.show()
print("Outputs of myconv() function, example 1: ")
print("x(n):")
print("[1,5,3,7,4]")
print("y(m):")
print("[3,1,5,7,3]")
print("x(n)*y(m):")
print(my_convArr)
input("Please press enter to proceed to the SciPy convolve() function example of this dataset:")

print("------------------------------------------------------------------------------------------")

my_convArr = convolve([1,5,3,7,4], [3,1,5,7,3], mode = 'full')
plt.clf()
plt.plot(my_convArr, label = "x(n) * y(m)")
plt.plot([1,5,3,7,4], label = "x(n)")
plt.plot([3,1,5,7,3], label = "y(m)")
plt.xlim(0, len_conv)
plt.title("scipy.signal.convolve() Function on 1st Dataset")
plt.legend()
plt.show()
print("Outputs of scipy.signal.convolve() function, example 1: ")
print("x(n):")
print("[1,5,3,7,4]")
print("y(m):")
print("[3,1,5,7,3]")
print("x(n)*y(m):")
print(my_convArr)
input("Please press enter to proceed to the 2nd example:")

print("------------------------------------------------------------------------------------------")

my_convArr, len_conv = myconv([-3,2,7,-6,2], 5, [-6,2,2,-3,-6], 5)
plt.clf()
plt.grid()
plt.plot(my_convArr, label = "x(n) * y(m)")
plt.plot([-3,2,7,-6,2], label = "x(n)")
plt.plot([-6,2,2,-3,-6], label = "y(m)")
plt.xlim(0, len_conv)
plt.title("myconv() Function on 2nd Dataset")
plt.legend()
plt.show()
print("Outputs of myconv() function, example 1: ")
print("x(n):")
print("[-3,2,7,-6,2]")
print("y(m):")
print("[-6,2,2,-3,-6]")
print("x(n)*y(m):")
print(my_convArr)
input("Please press enter to proceed to the SciPy convolve() function example of this dataset:")

print("-----------------------------------------------------------------------------------------")

my_convArr = convolve([-3,2,7,-6,2], [-6,2,2,-3,-6], mode = 'full')
plt.clf()
plt.plot(my_convArr, label = "x(n) * y(m)")
plt.plot([-3,2,7,-6,2], label = "x(n)")
plt.plot([-6,2,2,-3,-6], label = "y(m)")
plt.xlim(0, len_conv)
plt.title("scipy.signal.convolve() Function on 1st Dataset")
plt.legend()
plt.show()
print("Outputs of scipy.signal.convolve() function, example 1: ")
print("x(n):")
print("[-3,2,7,-6,2]")
print("y(m):")
print("[-6,2,2,-3,-6]")
print("x(n)*y(m):")
print(my_convArr)
input("Please press enter to proceed to the sound recording section:")

##########################
#Recording (3rd QUESTION)#
##########################

samplerate = 8000 #hertz
duration1 = 5 #seconds
duration2 = 10 #seconds
X1 = []
X2 = []

input("Please press 'Return' whenever you are ready to record the 1st audio")
print("Recording the 5 secs audio")
myAudio1 = sd.rec(int(samplerate * duration1), samplerate=samplerate, channels=1, blocking=True)
print("Finished Recording")

for i in range(len(myAudio1)):
    X1.append(myAudio1[i][0]) #converting the 2d numpy array to 1d python list, to make the convolution process quicker

input("Please press 'Return' whenever you are ready to record the 2nd audio")
print("Recording the 10 secs audio")
myAudio2 = sd.rec(int(samplerate * duration2), samplerate=samplerate, channels=1, blocking=True)
print("Finished Recording")

for i in range(len(myAudio2)):
    X2.append(myAudio2[i][0])

#################################
#Audio Processing (4th Question)#
#################################
def impulse(audio):
    audioArr = []
    for i in range(len(audio)):
        audioArr.append(audio[i])
        if i-400 >= 1:
            audioArr[i] = audioArr[i] + (0.4*audio[i-400])
        if i-800 >= 1:
            audioArr[i] = audioArr[i] + (0.4*audio[i-800])
    return audioArr

impulse_X1 = impulse(X1)
impulse_X2 = impulse(X2)

My_Y1 = myconv(X1, len(X1), impulse_X1, len(impulse_X1))
My_Y2 = myconv(X2, len(X2), impulse_X2, len(impulse_X2)) #THIS MAY TAKE A WHILE

Y1 = convolve(X1, impulse_X1, mode = 'full')
Y2 = convolve(X2, impulse_X2, mode = 'full')

##############################
#Audio Playing (5th QUESTION)#
##############################

print("Playing X1 Audio:")
sd.play(X1, samplerate)
sd.wait()
print("Playing X2 Audio:")
sd.play(X2, samplerate)
sd.wait()
print("Playing My_Y1 Audio:")
sd.play(My_Y1, samplerate)
sd.wait()
print("Playing My_Y2 Audio:")
sd.play(My_Y2, samplerate)
sd.wait()
print("Playing Y1 Audio:")
sd.play(Y1, samplerate)
sd.wait()
print("Playing Y2 Audio:")
sd.play(Y2, samplerate)
sd.wait()

input("Please press Enter to exit the program...")




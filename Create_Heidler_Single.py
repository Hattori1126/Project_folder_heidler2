import matplotlib.pyplot as plt
import numpy as np
import os


# Set parameter of date
datasize = 100000  # Sampling value

# Set parameters of waveshapes
Imax = 100  # Unit: A

Tmax = [350, 200, 100]  # Unit: μs

k = 0.93  # 10/350, 1/200, 0.25/100

T1 = [10, 1, 0.25]  # 10/350, 1/200, 0.25/100 Unit: μs
T2 = [350, 200, 100]  # 10/350, 1/200, 0.25/100 Unit: μs

# Set parameters of name
title_name = ["10/350μs", "1/200μs", "0.25/100μs"]

file_name = ["10_350μs", "1_200μs", "0.25_100μs"]

# Create or check data folders
# png data
figurepath = os.getcwd() + '/png/'
# figurepath = '/home/pi/Project_folder' + '/png/'
print(figurepath)

if not os.path.exists(figurepath):
    os.mkdir(figurepath)

print(os.path.exists(figurepath))

# csv data
csvpath = os.getcwd() + '/csv_original/'
# csvpath = '/home/pi/Project_folder' + '/csv_original/'
print(csvpath)

if not os.path.exists(csvpath):
    os.mkdir(csvpath)

print(os.path.exists(csvpath))


# Definite heidler function
def LPL(I, k, t, T1, T2):
    h1 = (I / k)
    h2 = ((t / T1) ** 10) / (1 + (t / T1) ** 10)
    h3 = np.exp(-t / T2)
    h = h1 * h2 * h3
    return h


# Create figures one by one
for n in range(0, 3, 1):
    fig = plt.figure(figsize=(7, 5), dpi=300)
    ax = fig.add_subplot()

    ax.grid(color='k', alpha=0.5)

    ax.set_xlabel('time[μs]', fontsize=15)
    ax.set_ylabel('current[kA]', fontsize=15)
    ax.set_title(title_name[n], fontsize=20)

    ax.set_xlim([0, Tmax[n]])
    ax.set_ylim([0, 120])

    t = np.linspace(0, Tmax[n], datasize)  # Unit: μs
    i = LPL(Imax, k, t, T1[n], T2[n])  # Unit: kA

    ax.plot(t, i, linewidth=2, color='r')

    plt.show()
    dataname = file_name[n] + '_Tmax' + str(Tmax[n]) + '_N' + str(datasize)

    # Save png file
    fig.savefig(figurepath + dataname + '.png', dpi=300)

    # Save CSV file
    file = np.stack([t, i], 1)
    np.savetxt(csvpath + dataname + '.csv', file)


print('finish')
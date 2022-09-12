import numpy as np
import glob
import os
import scipy
from scipy import interpolate


def get_filename_list(folderpath):
    filelist = glob.glob(folderpath + '/*' + Search_data_from)

    filenamelist = []
    for f in filelist:
        filenamelist = filenamelist + [os.path.splitext(os.path.basename(f))[0]]

    # Use natsort to sort filename like Windows Explorer
    return filelist, filenamelist


def read_datafile(filepath):
    return np.loadtxt(filepath)


resampling_size = 1000

# Choose data from
Search_data_from = '.csv'

# Choose path of data
datapath = 'D:\PyCharm\Project_folder_heidler\Create_Heidler_Single\csv_original'   # Windows
# datapath = '/home/pi/Project_folder/csv_original'                                                # Raspi

# print(get_filename_list(datapath))
filelist, filenamelist = get_filename_list(datapath)
# print(filelist)
# print(filenamelist)

# Resampling  data
if not filelist:
    print('Not exist file')

else:
    print('exist file')

    # Create csv_resampling folder
    csvpath = 'D:\PyCharm\Project_folder_heidler' + '/csv_resampling/'           # Windows
    # csvpath = '/home/pi/Project_folder' + '/csv_resampling/'                     # Raspi

    if not os.path.exists(csvpath):
        os.mkdir(csvpath)

    for d in range(0, len(filelist), 1):
        print('Processing on file', d)
        data_original = read_datafile(filelist[d])

        # Create new time axis
        data_transformed = np.linspace(0, data_original[-1, 0], resampling_size)

        f = interpolate.interp1d(data_original[:, 0], data_original[:, 1], fill_value="extraplate")

        data_transformed = np.column_stack((data_transformed, f(data_transformed)))

        # Save resampling data
        np.savetxt(csvpath + 'resampling_' + filenamelist[d] + '.csv', data_transformed)

print('finish')






import os
import subprocess


# File hostname
# gdrive_foldername = '%s' % os.uname()[1]
png_raspiadress = os.getcwd() + '/png'
csv_resampled_raspiadress = os.getcwd() + '/csv_resampled'

# print(os.uname()[1])

# subprocess.run(['rclone sync ' + png_raspiadress + ' gdrive:' + 'Project_folder_heidler2/png'], shell=True)

# subprocess.run(['rclone sync ' + csv_resampled_raspiadress + ' gdrive:' + 'Project_folder_heidler2/csv_resampled'], shell=True)

subprocess.run(['rclone sync ' + png_raspiadress + ' gcs:' + 'practice_yasuilabo/hattori' + '/png'], shell=True)

subprocess.run(['rclone sync ' + csv_resampled_raspiadress + ' gcs:' + 'practice_yasuilabo/hattori' + '/csv_resampled'], shell=True)


print('finish')
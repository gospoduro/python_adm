import os
import datetime
import shutil
import glob

dt = datetime.datetime.now()
currentdate = dt.strftime('%Y-%m-%d_%H%M')

source = 'D:/test_data/'
backup_temp_files = 'D:/test_backup_temp/test_data'
backup_temp_dir = 'D:/test_backup_temp/'
backup_finish_destination = 'D:/test_backup/'
backup_name = backup_temp_files+'_'+currentdate

shutil.make_archive(backup_name, 'zip', source)

files_path_to_move = backup_temp_dir
files_path_dest = backup_finish_destination
files = os.listdir(files_path_to_move)
files.sort()
for f in files:
    if f.startswith('test_data_'):
        source = files_path_to_move+f
        destination = files_path_dest+f
        shutil.move(source,destination)

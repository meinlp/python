import os
import datetime
from glob import glob

SEARCH_DIR = './test_data/'
DAYS_TO_KEEP_ALL = 30


def prepare_data():
    # get list of files, trim all the .sha and .gz, sort, uniq
    filenames = os.listdir(SEARCH_DIR)
    for i in range(len(filenames)):
        filenames[i] = filenames[i][:41]
    unique_filenames = sorted(set(filenames))

    dates = {}
    for filename in unique_filenames:
        # get the date modified for each file
        modified = os.path.getmtime(glob(SEARCH_DIR + filename + '*')[0])
        date_modified = datetime.datetime.fromtimestamp(modified).date()

        # and push it to the dict, so it will have the structure like
        # {date1:[file1,file2], date2:[file]}
        if date_modified not in dates:
            dates[date_modified] = [filename]
        else:
            dates[date_modified].append(filename)
    return dates


def cleanup(files_by_date):
    today = datetime.date.today()
    last_month = (datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_ALL)).date()
    # iterate through the dictionary to delete shit
    for date, files in files_by_date.items():
        # if the date is within the date range, do nothing
        if last_month <= date <= today:
            continue

        # if there's already only one file for the day, do nothing
        if len(files) == 1:
            continue

        # if there are multiple files for the day, keep the first file and delete the rest
        else:
            for file in files[1:]:
                for search in glob(SEARCH_DIR + file + '*'):
                    os.remove(search)


data = prepare_data()
cleanup(data)


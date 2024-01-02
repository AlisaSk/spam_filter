# will use this func to get file_name and truth from !truth file (returns dict)
def read_classification_from_file(filename):
    with open(filename, mode="rt", encoding="utf-8") as f:
        files_and_results = dict()
        for line in f:
            file, result = line.rstrip().split(' ')
            files_and_results[file] = result
             
    return files_and_results

# here should be func that will create .txt file with file_names and predictions 
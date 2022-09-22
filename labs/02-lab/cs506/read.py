def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    import csv
    with open(csv_file_path)as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            print(row)

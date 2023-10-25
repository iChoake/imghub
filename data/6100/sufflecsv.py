import csv
import random

def shuffle_csv(file_path):
    # Read the original CSV file
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Shuffle the data
    random.shuffle(data)

    # Write the shuffled data back to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Provide the path to your CSV file
csv_file_path = '/Users/steven/Documents/GitHub/ichoake.github.io/data/6100/image_urls.csv'
shuffle_csv(csv_file_path)


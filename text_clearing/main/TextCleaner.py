import csv
import string

with open('items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        post_text = row['post_text']
        print(post_text)
        exclude = set(string.punctuation)
        post_text = ''.join(ch for ch in post_text if ch not in exclude)
        print(post_text)
        post_stars = row['stars']
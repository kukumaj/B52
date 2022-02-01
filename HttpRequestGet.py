import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='url to website')  # adding mandatory argument url
args, unknown = parser.parse_known_args()  # parsing this argument read it may have even 1000 arguments
try:
    r = requests.get(args.url)
    if str(r.status_code)[0] != '2':
        print('Something bad happened')
    else:
        print(r)
except requests.exceptions.ConnectionError:
    print('there is no website like this')


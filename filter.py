import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-i',           help='path of input json')
parser.add_argument('-o',           help='path of output json')

def main(i, o):
    data = json.load(open(i))
    new_data = {'items': []}
    new_data['items'] = [{'created': item['created_at'], 'tweet': item['tweet'], 'link': item['link'], 'likes_count': item['likes_count'], 'retweets_count': item['retweets_count'], 'replies_count': item['replies_count'], 'quote_url': item['quote_url'], 'reply_to': item['reply_to'], 'mentions': item['mentions'], 'urls': item['urls'], 'photos': item['photos']} for item in data['items']]
    json.dump(new_data, open(o, 'w'), indent=2)
    print('done')


if __name__ == '__main__':
  args = parser.parse_args()
  main(args.i, args.o)
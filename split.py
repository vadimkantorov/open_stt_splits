import os
import gzip
import random
import itertools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--metadata_file', default = 'public_meta_data_v03.csv')
parser.add_argument('--bad', nargs = '*', default = [
	'bad_trainval_v03.csv',
	'bad_public_train_v03.csv'
])
parser.add_argument('--sources_hard', nargs = '*', default = [
	'asr_public_phone_calls_2',
	'asr_public_phone_calls_1',
	'asr_public_stories_2',
	'asr_public_stories_1',
])
parser.add_argument('--sources_ok', nargs = '*', default = [
	'private_buriy_audiobooks_2', # audiobooks_2
	'public_youtube700',
	'tts_russian_addresses_rhvoice_4voices', # tts_russian_addresses
	'public_series_1',
	'ru_ru',
	'voxforge_ru',
	'russian_single',
	'public_lecture_1'
])
parser.add_argument('--sources_easy', nargs = '*', default = [
	'voxforge_ru'
])
parser.add_argument('--split_train', defaut = 0.9)
parser.add_argument('--split_val', defaut = 0.1)
args = parser.parse_args()

meta = {os.path.basename(s[-2]) : (s[1].split('/')[1], l.strip()) for l in open(args.metadata_file) for s in [l.split(',')] if s[0]}
bad = set(os.path.basename(s[1].strip()) for b in args.bad for l in open(b) for s in [l.split(',')] if s[0])
good = {k : meta[k] for k in meta.keys() - args.bad}
sourced = {k : [t[1] for t in g] for k, g in itertools.groupby(sorted([(source, line) for k, (source, line) in good.items()], key = lambda t: t[0]), key = lambda t: t[0])}

for suffix in ['ok', 'easy', 'hard']:
	train, val = [], []
	for source in getattr(args, 'sources_' + suffix):
		lines = sourced[source]
		random.seed(1)
		random.shuffle(lines)
		c = int(len(lines) * args.split_Train)
		train.extend(lines[:c])
		val.extend(lines[c:])

	with gzip.open(f'train_{suffix}.txt.gz', 'wt') as f:
		f.write('\n'.join(train))
	with gzip.open(f'val_{suffix}.txt.gz', 'wt') as f:
		f.write('\n'.join(val))


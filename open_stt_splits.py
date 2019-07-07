import os
import base64
import gzip
import random
import itertools
import argparse

def samples_html(by_source, samples_html_path, seed = 1, K = 10):
	f = open(samples_html_path, 'w')
	f.write('<html><meta charset="UTF-8"><body>')
	for source, lines in sorted(by_source.items()):
			f.write(f'<h1>{source}</h1>')
			f.write('<table>')
			lines = lines[:]
			random.seed(seed)
			random.shuffle(lines)
			for i in range(K):
					splitted = lines[i].split(',')
					filename = splitted[-2]
					transcript = splitted[2]
					try:
						encoded = base64.b64encode(open(filename, 'rb').read()).decode('utf-8').replace('\n', '')
					except:
						f.write(f'<tr><td>file not found: {filename}</td></tr>')
						break
					f.write(f'<tr><td>{filename}</td><td><audio controls src="data:audio/wav;base64,{encoded}"/></td><td>{transcript}</td></tr>\n')
			f.write('</table>')

def dump(by_source, splits_dir, subset_name, gz = True):
	if not os.path.exists(splits_dir):
		os.makedirs(splits_dir)
	for split_name, subset in by_source.items():
		fname = os.path.join(splits_dir, f'{subset_name}_{split_name}.csv')
		f = (gzip.open(fname + '.gz', 'wt') if gz else open(fname, 'w'))
		print(fname, '\t\tutterances:', len(subset) // 1000, 'K  hours:', int(sum(float(line.split(',')[4]) for line in subset) / 3600))
		f.write('\n'.join(subset))

def split(by_source, sources, spec, sample_keyword = 'sample', seed = 1):
	lines = [l for source in sources for l in by_source[source]]
	random.seed(seed)
	random.shuffle(lines)
	res = {}

	cnt_ = lambda cnt, lines: cnt if isinstance(cnt, int) else int(len(lines) * cnt)

	k = 0
	for split_name, cnt in spec.items():
		if isinstance(cnt, tuple):
			cnt_0 = cnt_(cnt[0], lines)
			shuffled = lines[k: k + cnt_0]
			random.shuffle(shuffled)
			res[split_name] = shuffled
			res[f'{split_name}_{sample_keyword}'] = shuffled[:cnt_(cnt[1], shuffled)]
			cnt = cnt_0
		else:
			cnt = cnt_(cnt, lines)
			res[split_name] = lines[k : k + cnt]
		k += cnt

	return res

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--metadata', default = 'public_meta_data_v03.csv')
	parser.add_argument('--exclude', default = 'public_exclude_file_v5.csv')
	parser.add_argument('--samples', default = 'open_stt_splits.html')
	parser.add_argument('--splits', default = 'splits')
	parser.add_argument('--gzip', action = 'store_true')
	args = parser.parse_args()

	meta = {os.path.basename(s[-2]) : (s[1].split('/')[1], l.strip()) for l in open(args.metadata) for s in [l.split(',')] if s[0]}
	bad = set(os.path.basename(s[1].strip()) for l in open(open(args.exclude)) for s in [l.split(',')] if s[0])
	good = {k : meta[k] for k in meta.keys() - bad}
	by_source = {k : [t[1] for t in g] for k, g in itertools.groupby(sorted([(source, line) for k, (source, line) in good.items()], key = lambda t: t[0]), key = lambda t: t[0])}

	samples_html(by_source, args.samples)

	clean = split(by_source, ['voxforge_ru', 'ru_ru', 'russian_single', 'public_lecture_1', 'public_series_1'], dict(train = 0.95, val = 0.05))
	dump(clean, args.splits, 'clean', gz = args.gzip)

	addresses = split(by_source, ['tts_russian_addresses_rhvoice_4voices'], dict(train_mini = len(clean['train']), val_mini = len(clean['val'])))
	dump(addresses, args.splits, 'addresses', gz = args.gzip)

	audiobooks = split(by_source, ['private_buriy_audiobooks_2'], dict(train_mini1 = len(clean['train']), val_mini1 = len(clean['val']), train_mini2 = len(clean['train']), val_mini2 = len(clean['val']), train_mini3 = len(clean['train']), val_mini3 = len(clean['val']), train = (1_000_000, 500_000)), sample_keyword = 'medium')
	audiobooks['train_mini'] = audiobooks['train_mini1'] + audiobooks['train_mini2'] + audiobooks['train_mini3']
	audiobooks['val'] = audiobooks['val_mini1'] + audiobooks['val_mini2'] + audiobooks['val_mini3']
	audiobooks['train'] = audiobooks['train'] + audiobooks['train_mini']
	dump(audiobooks, args.splits, 'audiobooks', gz = args.gzip)

	mixed = dict(train = clean['train'] + addresses['train_mini'] + audiobooks['train_mini1'], val = clean['val'] + addresses['val_mini'] + audiobooks['val_mini1'])
	dump(mixed, args.splits, 'mixed', gz = args.gzip)

	unused_sources_for_now = ['asr_public_phone_calls_2', 'asr_public_phone_calls_1', 'asr_public_stories_2', 'asr_public_stories_1', 'public_youtube700']

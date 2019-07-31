# Download the dataset
```shell
apt update && apt install -y aria2
aria2c http://academictorrents.com/download/a12a08b39cf3626407e10e01126cf27c198446c2.torrent --seed-time=0

cd ru_open_stt_wav

for f in asr_calls_2_val.tar.gz buriy_audiobooks_2_val.tar.gz public_youtube700_val.tar.gz asr_public_stories_1.tar.gz asr_public_stories_2.tar.gz public_lecture_1.tar.gz public_series_1.tar.gz public_youtube1120.tar.gz radio_2.tar.gz ru_ru.tar.gz public_youtube1120_hq.tar.gz russian_single.tar.gz voxforge_ru.tar.gz asr_public_phone_calls_1.tar.gz; do
tar -xf $f
rm $f
done

for f in audiobooks_2.tar.gz_ public_youtube700.tar.gz_ asr_public_phone_calls_2.tar.gz_; do
cat $f* > tmp.tar.gz
rm $f*
tar -xf tmp.tar.gz
rm tmp.tar.gz
done

```
# Download exclude files
```shell
wget https://ru-open-stt.ams3.digitaloceanspaces.com/public_meta_data_v04_fx.csv

wget https://github.com/snakers4/open_stt/files/3348311/public_exclude_file_v5.zip
wget https://github.com/snakers4/open_stt/files/3348314/public_exclude_file_v5.z01.zip
wget https://github.com/snakers4/open_stt/files/3348312/public_exclude_file_v5.z02.zip
wget https://github.com/snakers4/open_stt/files/3348313/public_exclude_file_v5.z03.zip

cat public_exclude_file_v5.z01.zip public_exclude_file_v5.z02.zip public_exclude_file_v5.z03.zip public_exclude_file_v5.zip > public_exclude_file_v5_.zip
unzip public_exclude_file_v5_.zip

wget https://github.com/snakers4/open_stt/files/3386441/exclude_df_youtube_1120.zip
unzip exclude_df_youtube_1120.zip

wget https://ru-open-stt.ams3.digitaloceanspaces.com/benchmark_v05_public.csv.zip
zcat benchmark_v05_public.csv.zip > benchmark_v05_public.csv

rm public_exclude_file_v5.z01.zip public_exclude_file_v5.z02.zip public_exclude_file_v5.z03.zip public_exclude_file_v5.zip public_exclude_file_v5_.zip exclude_df_youtube_1120.zip benchmark_v05_public.csv.zip

```

```
splits/clean_train.csv          utterances: 26 K  hours: 48
splits/clean_val.csv            utterances: 1 K  hours: 2
splits/mixed_train.csv          utterances: 2020 K  hours: 2686
splits/mixed_val.csv            utterances: 15 K  hours: 9
splits/mixed_small.csv          utterances: 202 K  hours: 268
splits/calls_val.csv            utterances: 12 K  hours: 7


splits/clean_train.csv          utterances: 26 K  hours: 48
splits/clean_val.csv            utterances: 1 K  hours: 2
splits/mixed_train.csv          utterances: 2046 K  hours: 2698
splits/mixed_val.csv            utterances: 28 K  hours: 17

splits/clean_train.csv          utterances: 28 K  hours: 50
splits/clean_val.csv            utterances: 1 K  hours: 2
splits/mixed_train.csv          utterances: 2638 K  hours: 3369
splits/mixed_val.csv            utterances: 28 K  hours: 17

splits/clean_train.csv                          utterances: 37 K   hours: 58
splits/clean_val.csv                            utterances: 1 K    hours: 3
splits/addresses_train_mini.csv                 utterances: 37 K   hours: 16
splits/addresses_val_mini.csv                   utterances: 1 K    hours: 0
splits/audiobooks_train_mini1.csv               utterances: 37 K   hours: 49
splits/audiobooks_val_mini1.csv                 utterances: 1 K    hours: 2
splits/audiobooks_train_mini2.csv               utterances: 37 K   hours: 49
splits/audiobooks_val_mini2.csv                 utterances: 1 K    hours: 2
splits/audiobooks_train_mini3.csv               utterances: 37 K   hours: 49
splits/audiobooks_val_mini3.csv                 utterances: 1 K    hours: 2
splits/audiobooks_train.csv                     utterances: 1010 K hours: 1352
splits/audiobooks_train_medium.csv              utterances: 500 K  hours: 669
splits/audiobooks_train_mini.csv                utterances: 111 K  hours: 148
splits/audiobooks_val.csv                       utterances: 5 K    hours: 7
splits/mixed_train.csv                          utterances: 111 K  hours: 124
splits/mixed_val.csv                            utterances: 5 K    hours: 6
```

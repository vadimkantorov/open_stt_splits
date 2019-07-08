```shell
wget https://ru-open-stt.ams3.digitaloceanspaces.com/public_meta_data_v04_fx.csv

wget https://github.com/snakers4/open_stt/files/3348311/public_exclude_file_v5.zip
wget https://github.com/snakers4/open_stt/files/3348314/public_exclude_file_v5.z01.zip
wget https://github.com/snakers4/open_stt/files/3348312/public_exclude_file_v5.z02.zip
wget https://github.com/snakers4/open_stt/files/3348313/public_exclude_file_v5.z03.zip

cat public_exclude_file_v5.z01.zip public_exclude_file_v5.z02.zip public_exclude_file_v5.z03.zip public_exclude_file_v5.zip > public_exclude_file_v5_.zip
unzip public_exclude_file_v5_.zip
```

```
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

# Word Segmenter

## 1.Install CRF++
* download [CRF++][1]
* install CRF++

```
./configure
make
sudo make install

```
## 2.Preparing Data
* download [backoff2005 data][2]


## 3.Convert data to CRF++ format
```
python conv_format.py icwb2-data/training/pku_training.utf8 train.data
```


## 4.CRF++ train
```
crf_learn -f 3 -c 4.0 CRF++-0.58/example/seg/template train.data model
```
training time: about 20 minutes

## 5.CRF++ test
```
python run_test.py model icwb2-data/testing/pku_test.utf8 test.result
```

## 6.Backoff2005 experiment
```
perl icwb2-data/scripts/score icwb2-data/gold/pku_training_words.utf8 icwb2-data/gold/pku_test_gold.utf8 test.result > a.txt
```

# Reference
<http://www.mutouxiaogui.cn/blog/?p=224>

[1]:https://drive.google.com/drive/folders/0B4y35FiV1wh7fngteFhHQUN2Y1B5eUJBNHZUemJYQV9VWlBUb3JlX0xBdWVZTWtSbVBneU0
[2]:http://www.sighan.org/bakeoff2005/
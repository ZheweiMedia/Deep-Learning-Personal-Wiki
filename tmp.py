import pickle
import gzip
import numpy
from random import shuffle








TRAIN_NO = 56
VALID_NO = 6
TEST_NO = 5
BATCH_SIZE = 30
nb_epoch = 750
hd_notes = 10
Groups = 2


def normalize(_data):
    ## _data shape: subject number, feature number, time length
    ## the output should be (ImageNo, timesteps, featureNo)
    output = numpy.zeros((_data.shape[0], _data.shape[2], _data.shape[1]))
    for iNo in range(_data.shape[0]):
        for fNo in range(_data.shape[1]):
            _tmp = _data[iNo, fNo, :]
            if numpy.any(_tmp):
                _tmp = _tmp/(numpy.linalg.norm(_tmp))
            output[iNo, :, fNo] = _tmp

    return output

def featureSelection(_data, _label):
    ## _data shape: (ImageNo, timesteps, featureNo)
    selected_feature_index = list()
    for iNo in range(_data.shape[0]):
        for fNo in range(_data.shape[2]):
            _tmp = _data[iNo, :, fNo]
            #print (numpy.corrcoef(_tmp, _label[iNo,:])[0,1])
            #print (fNo)
            if (numpy.corrcoef(_tmp, _label[iNo,:])[0,1] > 0.3):
                selected_feature_index.append(fNo)
    print(set(selected_feature_index))
    print (len(set(selected_feature_index)))


def label_for_keras(_label):
    output = numpy.empty((_label.shape[0], _label.shape[1],2))
    for iNo in range(_label.shape[0]):
        for fNo in range(_label.shape[1]):
            if _label[iNo, fNo] == 0:
                output[iNo, fNo,:] = [1,0]
            if _label[iNo, fNo] == 1:
                output[iNo, fNo, :] = [0,1]
    return output




with gzip.open('EMOTION_Data.pickle.gz', 'r') as datafile:
    original_data = pickle.load(datafile)

with gzip.open('EMOTION_Label.pickle.gz', 'r') as labelfile:
    wholeLabel = pickle.load(labelfile)

# normalize
wholeData = normalize(original_data)
print(wholeData.shape)

# featureSelection(wholeData, wholeLabel)

whole_index = [i for i in range(wholeData.shape[0])]
shuffle(whole_index)

train_data = wholeData[whole_index[:TRAIN_NO],:,:]
train_label = wholeLabel[whole_index[:TRAIN_NO],:]
valid_data = wholeData[whole_index[TRAIN_NO:TRAIN_NO+VALID_NO],:,:]
valid_label = wholeLabel[whole_index[TRAIN_NO:TRAIN_NO+VALID_NO],:]
test_data = wholeData[whole_index[TRAIN_NO+VALID_NO:],:,:]
test_label = wholeLabel[whole_index[TRAIN_NO+VALID_NO:],:]

print(train_data.shape)
print(train_label.shape)
print(valid_data.shape)
print(valid_label.shape)
print(test_data.shape)
print(test_label.shape)

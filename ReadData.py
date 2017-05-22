
"""
"""


import os
from glob import glob
import gzip
import pickle
import numpy
from random import shuffle


class _Subject_with_data:
    def __init__(self, SubjectID, DX_Group):
        self.DX_Group = DX_Group
        self.SubjectID = SubjectID
        # baseline 
        self.MRI_baseline = dict()
        self.fMRI_baseline = dict()
        # otherdata after baseline 
        self.MRI_other = list()
        self.fMRI_other = list()


def read_data(index_list, total_data):
    _data = list()
    label = list()
    for index in index_list:
        subject = total_data[index]
        if subject.MRI_baseline:
            imageID = list(subject.MRI_baseline.keys())[0]
            imageData = subject.MRI_baseline[imageID]
            _data.append(imageData)
            if subject.DX_Group == 'AD':
                label.append('1')
            else:
                label.append('0')
        if subject.MRI_other:
            for subj in subject.MRI_other:
                imageID = list(subj.keys())[0]
                imageData = subj[imageID]
                _data.append(imageData)
                if subject.DX_Group == 'AD':
                    label.append('1')
                else:
                    label.append('0')

    size_of_imageData = len(_data[0])

    _array = numpy.empty([2,2])
    for index, content in enumerate(_data):
        if index == 0:
            _array = content;
        else:
            _array = numpy.concatenate((_array, content))

    _array = _array.reshape((len(_data), size_of_imageData))
    return _array, label


with gzip.open("smallDataset_imageID_with_Data.gz", "rb") as output_file:
    subjects_list = pickle.load(output_file)

print (len(subjects_list))

subjects_index = [i for i in range(len(subjects_list))]


trainNo = 100
testNo = 15

shuffle(subjects_index)

print (subjects_index)

trainsubjects = subjects_index[:100]
testsubjects = subjects_index[100:]


train_data, train_label = read_data(subjects_index[:100], subjects_list)
test_data, test_label = read_data(subjects_index[100:], subjects_list)

print (train_data.shape)
print (test_data.shape)

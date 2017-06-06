import os
from glob import glob
import gzip
import pickle
import numpy

class _EachSubject:
    # each subject is a element of a list
    def __init__(self, SubjectID, DX_Group, MRI_imageID, fMRI_imageID):
        self.DX_Group = DX_Group
        self.SubjectID = SubjectID
        # baseline 
        self.MRI_baseline = MRI_imageID
        self.fMRI_baseline = fMRI_imageID
        # otherdata after baseline 
        self.MRI_other = list()
        self.fMRI_other = list()

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

"""
os.chdir('/media/medialab/Seagate Expansion Drive/ADNI/SIEMENS/fMRI')
fMRI_ID = list()
for i in glob('*/'):
    print (i)
    print (i[5:11])
    fMRI_ID.append(i[5:11])
os.chdir('/home/medialab/Zhewei/fMRI_CSV_Analysis')
with gzip.open("smallDataset_fMRIList", "wb") as output_file:
    pickle.dump(fMRI_ID, output_file)
"""

with gzip.open("smallDataset_fMRIList", "rb") as output_file:
    fMRI_ID = pickle.load(output_file)

print (len(fMRI_ID))
"""
with open('fMRI_ID', 'w') as output_file:
    for ID in fMRI_ID:
        output_file.write(ID)
        output_file.write('\n')
"""

with gzip.open("After_Registration_Clean_imageID.gz", "rb") as output_file:
    subjects = pickle.load(output_file)


for subject in subjects:
    if subject.DX_Group == 'AD' or subject.DX_Group =='Normal':
        #print (subject.SubjectID)
        if subject.fMRI_baseline not in fMRI_ID:
            #print (subject.fMRI_baseline)
            subject.fMRI_baseline = None
            subject.MRIBaseline = None
        if subject.fMRI_other:
            for ID in subject.fMRI_other:
                if ID not in fMRI_ID:
                    ID_index = subject.fMRI_other.index(ID)
                    subject.fMRI_other[ID_index] = None
                    subject.MRI_other[ID_index] = None



# one bad data. cannot read the file 196079, and some images didn't process
bad_list = ['196079', '756267', '763572', '797153']
for subject in subjects:
    if subject.DX_Group == 'AD' or subject.DX_Group =='Normal':
        #print (subject.SubjectID)
        if subject.fMRI_baseline in bad_list:
            #print (subject.fMRI_baseline)
            print ('YES')
            subject.fMRI_baseline = None
            subject.MRIBaseline = None
        if subject.fMRI_other:
            for ID in subject.fMRI_other:
                if ID in bad_list:
                    print ('YES, HERE')
                    ID_index = subject.fMRI_other.index(ID)
                    subject.fMRI_other[ID_index] = None
                    subject.MRI_other[ID_index] = None


# statistic about the data
AD_No = 0
Normal_No = 0
MRI_imgNo = 0
flag = False
for subject in subjects:
    if subject.DX_Group == 'AD' or subject.DX_Group =='Normal':
        #print (subject.SubjectID)
        flag = False
        if subject.fMRI_baseline != None:
            #print (subject.fMRI_baseline)
            MRI_imgNo += 1
            flag = True
        if subject.fMRI_other:
            for ID in subject.fMRI_other:
                if ID != None:
                    MRI_imgNo += 1
                    flag = True
        if flag:
            if subject.DX_Group == 'AD':
                AD_No += 1
            if subject.DX_Group == 'Normal':
                Normal_No +=1

print ('We have AD subjects:', AD_No)
print ('We have Normal subjects:', Normal_No)
print ('We have MRI image:', MRI_imgNo)

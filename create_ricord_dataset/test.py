import sys

import os
import cv2
import glob
import pydicom
from pydicom.pixel_data_handlers import apply_modality_lut, apply_voi_lut
import numpy as np
import pandas as pd


def _extract_data(df_row):
    return df_row['Anon MRN'], df_row['Anon TCIA Study Date'], df_row['Anon Exam Description'], df_row['Anon Study UID']


def load_ricord_metadata(ricord_meta_file):
    df = pd.read_excel(ricord_meta_file, sheet_name='CR Pos - TCIA Submission')
    ricord_metadata = []
    for index, row in df.iterrows():
        ricord_metadata.append(_extract_data(row))
    return ricord_metadata

def make_ricord_dict(ricord_data_set_file):
    """Loads bboxes from the given text file"""
    ricord_dict = {}
    with open(ricord_data_set_file, 'r') as f:
        for line in f.readlines():
            # Values after file name are crop dimensions
            if(len(line.split()) > 1):
                fname, xmin, ymin, xmax, ymax = line.rstrip('\n').split()
                bbox = tuple(int(c) for c in (xmin, ymin, xmax, ymax))
                ricord_dict[fname] = bbox
            else:
                fname = line.rstrip('\n')
                ricord_dict[fname] = None
                
    return ricord_dict

ricord_dir = "G:\\dataset\\DICOM\\manifest-1610656454899"
ricord_meta_file = 'G:\\dataset\\DICOM\\MIDRC-RICORD-1c Clinical Data Jan 13 2021 .xlsx'

out_dir = 'ricord_images'
ricord_set_file = 'ricord_data_set.txt'

os.makedirs(out_dir, exist_ok=True)

ricord_dict = make_ricord_dict(ricord_set_file)
metadata = load_ricord_metadata(ricord_meta_file)


file_count = 0
for mrn, date, desc, uid in metadata:
    date = date.strftime('%m-%d-%Y')
    uid = uid[-5:]
    study_dir = os.path.join(ricord_dir, 'MIDRC-RICORD-1C-{}'.format(mrn), '*-{}'.format(uid))
#     patht = study_dir + '*' + '*.dcm'
    files = glob.glob(os.path.join(study_dir, '*', '*.dcm'))
    print(files)
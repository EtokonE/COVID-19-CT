#!/bin/bash
FILE=CT_dicom.zip

URL=https://www.dropbox.com/s/mxyl81l0m2u994r/CT_dicom.zip?dl=0
echo loading file $FILE from $URL

ZIP_FILE=./data/raw/$FILE
TARGET_DIR=./data/raw/
curl -L $URL -o $ZIP_FILE
mkdir $TARGET_DIR
unzip $ZIP_FILE -d $TARGET_DIR
rm $ZIP_FILE

echo Data successfully uploaded

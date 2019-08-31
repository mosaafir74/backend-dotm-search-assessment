#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import zipfile


"""
Given a directory path, search all files in the path for a given text string
within the 'word/document.xml' section of a MSWord .dotm file.
"""

"""
def get_dotm_files(directory):
    files = os.listdir(directory)
    files = [os.path.join(os.path.dirname(os.path.abspath(f)),'dotm_files',f) for f in files if f.endswith('.dotm')]
    return files

def search_for_text(text, file):
    with zipfile.ZipFile(file, 'r') as zip:
        data = zip.read('word/document.xml')
    print(data)
//////////////////////////
"""

__author__ = "Haydar with instructor help"


def main(directory, text_to_search):
    file_list = os.listdir(directory)
    files_searched = 0
    files_matched = 0
    print(' ')
    print(' ')
    print("Searching directory {} ./dotm_files for text '{}' ...".format(directory, text_to_search))
    print(' ')
    for file in file_list:
        files_searched += 1 
        full_path = os.path.join(directory, file)
        if not full_path.endswith(".dotm"):
            print("this isn't a dotm {}".format(full_path))
            continue
        if not zipfile.is_zipfile(full_path):
            print("this isn't a zip file {}".format(full_path))
            continue
        with zipfile.ZipFile(full_path, 'r') as zipped:
            toc = zipped.namelist()
            if 'word/document.xml' in toc:
                with zipped.open('word/document.xml', 'r') as doc:
                    for line in doc:
                        i = line.find(text_to_search)
                        if i >= 0:
                            files_matched += 1
                            print('...{}...'.format(line[i - 40:i + 40]))
    print('Files matched: {}'.format(files_matched))
    print('Files searched: {}'.format(files_searched))
            
            
            #print(archived)
    # parser = argparse.ArgumentParser()
    # parser.add_argument("text")
    # parser.add_argument("--dir")
    # args = parser.parse_args()
    # print(args)
    # dotm_files = get_dotm_files('dotm_files')
    # for file in dotm_files:
    #     search_for_text('$', file)


if __name__ == '__main__':
    main("dotm_files","$")

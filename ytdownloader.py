import os
from os import listdir

from pytube import YouTube

global folder_path


def download():
    file_path = os.path.dirname(os.path.realpath(__file__))
    print('Paths you pass here will be relative to this program path: ', file_path)
    print('-----------------------------------------------------------------')
    while True:
        urls = read_urls_from_file()
        if urls:
            download_files(urls)
            break
        else:
            continue
    play_file(folder_path)


def read_urls_from_file():
    print('Pass the directory of text file with youtube URLs')
    file = input()
    content = []
    print('Reading file. Please wait...')
    try:
        with open(file) as f:
            content = f.readlines()
    except FileNotFoundError:
        print('File not found. Make sure you passed right directory')
        print('-----------------------------------------------------------------')
    return content


def download_files(content):
    music_files = []
    for val in content:
        music_files.append(YouTube(val))
    print('-----------------------------------------------------------------')
    print('Pass the directory where you want your files to be downloaded\nIf you dont pass any, folder '
          'will be created in current working folder')
    download_path = input() or 'music'
    global folder_path
    folder_path = download_path
    for val in music_files:
        val.streams.filter(only_audio=True).first().download(download_path)


def play_file(path):
    files = listdir(path)
    print('-----------------------------------------------------------------')
    print('You have downloaded', len(files), 'files. Select number from 1 to', len(files), 'to play specific file\n'
                                                                                             'Type exit to quit program')
    while True:
        selected_file = input()
        if selected_file == 'exit':
            break
        else:
            try:
                try:
                    selected_file_int = int(selected_file)
                except ValueError:
                    print('Pass integer!')
                    continue
                path = os.path.abspath(os.path.join(path, files[selected_file_int - 1]))
                print('Playing', os.path.basename(path))
                os.startfile(path)
                path = folder_path
            except IndexError:
                print('Number not in range')
                continue
    print('Thank for using my downloader :)')

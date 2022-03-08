from os import walk
# import pygame

# def import_folder(path):
#     for info in  walk(path):
#         print(info)

path = '/graphics/character/run'
for info in walk(path):
    print(info)
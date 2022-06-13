import os
import fire
import sys
from PIL import Image, ImageFilter


def main(filepath, width=256, height=256, extension='png', exclude=[]):
    file_list = get_file_list(
        filepath=filepath, extension=extension, exclude=list(exclude))
    resize(filepath, file_list, width, height)


def resize(filepath, file_list, width, height):
    def convert_absolute_path_list(file):
        absolute_path = os.path.join(filepath, file)
        return absolute_path

    absolute_pathes = list(map(convert_absolute_path_list, file_list))

    for file, path in zip(file_list, absolute_pathes):
        im = Image.open(path)
        print(f'converting {file} {im.size} -> ({width}, {height})')
        resized = im.resize((width, height))
        resized.save(path)

    print(f'{len(file_list)} photos successfully converted to {width}x{height}!!')


def is_exclude_file(file_name, exclude) -> bool:
    for exclude_name in exclude:
        if exclude_name in file_name:
            return True

    return False


def get_file_list(filepath, extension, exclude) -> list:
    result = []
    file_list = os.listdir(filepath)
    for file in file_list:
        file_name, ext = os.path.splitext(file)
        is_exclude = is_exclude_file(file_name, exclude)
        if ext[1:] == extension and not is_exclude:
            result.append(file)

    return result


if __name__ == '__main__':
    fire.Fire(main)

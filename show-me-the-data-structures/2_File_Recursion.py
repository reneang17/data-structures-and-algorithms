import os
import argparse

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """


    paths = [os.path.join(path, d) for d in os.listdir(path) if \
    os.path.isdir(os.path.join(path,d))]

    files = [os.path.join(path, f) for f in os.listdir(path) \
            if os.path.isfile(os.path.join(path, f)) and  f.endswith(suffix)]


    for path in paths:
        files+=find_files(suffix, path)

    return files


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    def dir_path(string):
        if os.path.isdir(string):
            return string
        else:
            raise NotADirectoryError(string)


    parser.add_argument('--initial_dir', type=dir_path, default = './testdir/',
                        help='Path to scan')
    parser.add_argument('--suffix', type=str, default = '.c',
                        help='target sufix')
    args = parser.parse_args()
    initial_dir = args.initial_dir
    suffix = args.suffix
    #print(initial_dir, '/n', suffix)
    print(find_files(suffix, initial_dir))

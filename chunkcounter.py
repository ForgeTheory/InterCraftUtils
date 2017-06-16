import os
import sys

from os import path

def main(args):
    print(count_chunks(args[1]))


def get_region_files(world_dir):
    overworld_path = path.join(world_dir, "region")
    nether_path = path.join(world_dir, "DIM1", "region")
    end_path = path.join(world_dir, "DIM-1", "region")
    files = []
    for p in (overworld_path, nether_path, end_path):
        if path.isdir(p):
            files.extend([path.join(p, i) for i in os.listdir(p)])
    return files


def chunks_in_region_file(filename):
    chunks = 0

    with open(filename, 'rb') as f:
        for i in range(1024):
            entry = f.read(4)
            if entry[-1] != 0:
                chunks += 1

    return chunks


def count_chunks(dirname):
    region_files = get_region_files(dirname)
    chunks = 0
    for f in region_files:
        chunks += chunks_in_region_file(f)

    return chunks


if __name__ == '__main__':
    main(sys.argv)

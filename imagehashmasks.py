import csv

import click
import imagehash
from PIL import Image


def find_by_image(mask, masks):
    sample_hash = imagehash.phash(Image.open(mask))
    return min(masks, key=lambda x: imagehash.hex_to_hash(x["phash"]) - sample_hash)


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def main(path):
    masks = list(csv.DictReader(open("masks.csv")))
    mask = find_by_image(path, masks)
    index = (16384 - 10141 + int(mask["index"])) % 16384
    print(f"https://www.thehashmasks.com/detail/{index}")


if __name__ == "__main__":
    main()

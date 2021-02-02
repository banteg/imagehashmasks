import csv

import click
import imagehash
from PIL import Image


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def main(path):
    masks = list(csv.DictReader(open("masks.csv")))
    im = Image.open(path)
    sample = imagehash.crop_resistant_hash(im, imagehash.phash)
    for mask in masks:
        mask["phash"] = imagehash.ImageMultiHash([imagehash.hex_to_hash(mask["phash"])])
        mask["diff"] = mask["phash"] - sample
    min_diff = min(masks, key=lambda mask: mask["diff"])["diff"]
    for mask in masks:
        if mask["diff"] == min_diff:
            index = (16384 - 10141 + int(mask["index"])) % 16384
            print(f"https://www.thehashmasks.com/detail/{index}")


if __name__ == "__main__":
    main()

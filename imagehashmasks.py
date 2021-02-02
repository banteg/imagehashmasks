import csv

import click
from imagehash import ImageMultiHash, crop_resistant_hash, hex_to_hash, phash
from PIL import Image


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def main(path):
    masks = list(csv.DictReader(open("masks.csv")))
    im = Image.open(path)
    sample = crop_resistant_hash(im, phash)
    mask = min(masks, key=lambda x: ImageMultiHash([hex_to_hash(x["phash"])]) - sample)
    index = (16384 - 10141 + int(mask["index"])) % 16384
    print(f"{mask['url']}\nhttps://www.thehashmasks.com/detail/{index}")


if __name__ == "__main__":
    main()

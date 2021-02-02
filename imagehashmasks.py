import csv

import click
import imagehash
from PIL import Image


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def main(path):
    masks = list(csv.DictReader(open("masks.csv")))
    sample = imagehash.phash(Image.open(path))
    mask = min(masks, key=lambda x: imagehash.hex_to_hash(x["phash"]) - sample)
    index = (16384 - 10141 + int(mask["index"])) % 16384
    print(f"{mask['url']}\nhttps://www.thehashmasks.com/detail/{index}")


if __name__ == "__main__":
    main()

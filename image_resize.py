import argparse
import sys

from PIL import Image


def resize_to_scale(original_image: Image, result_scale: float) -> Image:
    xsize, ysize = map(lambda x: int(x * result_scale), original_image.size)
    return original_image.resize((xsize, ysize))


def resize_to_width_and_height(original_image: Image, width: int,
                               height: int) -> Image:
    xsize, ysize = original_image.size
    if xsize / width != ysize / height:
        print('Result image scale is different from original!')
    return original_image.resize((width, height))


def main(path_to_original: str, path_to_output: str, args: dict) -> None:
    image_original = Image.open(path_to_original)
    if (args.width != 0 or args.height != 0) and args.scale != 0:
        raise ValueError('Height/width OR scale should be defined, not both!')
    if args.scale != 0:
        image_result = resize_to_scale(image_original, args.scale)
    elif args.height == 0:
        scale = args.width / image_original.size[0]
        image_result = resize_to_scale(image_original, scale)
    elif args.width == 0:
        scale = args.height / image_original.size[1]
        image_result = resize_to_scale(image_original, scale)
    else:
        image_result = resize_to_width_and_height(image_original, args.width,
                                                  args.height)
    save_result_image(image_result, args)


def save_result_image(result_image: Image, args: dict):
    if args.output:
        result_image.save(args.output)
    else:
        xsize, ysize = result_image.size
        asd = 'asd'
        asd.rfind('.')
        ext = args.filename.rfind('.')
        result_filename = '{}__{}x{}{}'.format(args.filename[:ext], xsize,
                                               ysize, args.filename[ext:])
        result_image.save(result_filename)
        print('Result image is saved: {}'.format(result_filename))


def resolve_args(argv):
    parser = argparse.ArgumentParser(description='Image resize script.')
    parser.add_argument('filename',
                        help='Source image filename', )
    parser.add_argument('-width', metavar='WIDTH', type=int, default=0,
                        help='Width of the output picture')
    parser.add_argument('-height', metavar='HEIGHT', type=int, default=0,
                        help='Height of the output picture')
    parser.add_argument('-scale', metavar='SCALE', type=float, default=0,
                        help='Scale of the output picture')
    parser.add_argument('-output', metavar='OUTPUT',
                        type=argparse.FileType('w'),
                        help='Name of the output image file')
    return parser.parse_args()


if __name__ == '__main__':
    args = resolve_args(sys.argv)
    main(args.filename, args.output, args)

import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--domain", "-d", default="sketch", help="Target")
parser.add_argument("--gpu", "-g", default=0, type=int, help="Gpu ID")
parser.add_argument("--times", "-t", default=1, type=int, help="Repeat times")
parser.add_argument("--root", default=None, type=str)

args = parser.parse_args()

###############################################################################

source = ["photo", "cartoon", "art_painting", "sketch"]
target = args.domain
source.remove(target)

input_dir = '/content/drive/MyDrive/CIRL/data/PACS/train-val-splits'
output_dir = '/content/drive/MyDrive/CIRL/output/logs'

config = "PACS/ResNet50"

domain_name = target
path = os.path.join(output_dir, config.replace("/", "_"), domain_name)
##############################################################################
train_script = '/content/drive/MyDrive/CIRL/train.py'
for i in range(args.times):
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} '
              f'python {train_script} '
              f'--source {source[0]} {source[1]} {source[2]} '
              f'--target {target} '
              f'--input_dir {input_dir} '
              f'--output_dir {output_dir} '
              f'--config {config}',)


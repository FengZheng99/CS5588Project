import argparse

parser = argparse.ArgumentParser(description='WSAD')
parser.add_argument('--feat-extractor', default='i3d', choices=['i3d', 'c3d'])
parser.add_argument('--feature-size', type=int, default=1024, help='size of feature (default: 1024)')
parser.add_argument('--modality', default='RGB', help='the type of the input, RGB,AUDIO, or MIX')
parser.add_argument('--rgb-list', default='list/ucf-c3d.list', help='list of rgb features ')
parser.add_argument('--test-rgb-list', default='list/ucf-c3d-test.list', help='list of test rgb features ')
parser.add_argument('--gt', default='list/gt-ucf.npy', help='file of ground truth ')
parser.add_argument('--gpus', default=1, type=int, choices=[0, 1], help='gpus')
parser.add_argument('--lr', type=float, default=0.00005, help='learning rate (default: 0.0001)')
parser.add_argument('--batch-size', type=int, default=32, help='number of instances in a batch of data (default: 16)')
parser.add_argument('--workers', default=0, help='number of workers in dataloader')
parser.add_argument('--model-name', default='deepmil', help='name to save model')
parser.add_argument('--pretrained-ckpt', default=None, help='ckpt for pretrained model')

parser.add_argument('--num-classes', type=int, default=1, help='number of class')
parser.add_argument('--dataset-name', default='UCF-Crime', help='dataset to train on (default: )')
parser.add_argument('--plot-freq', type=int, default=10, help='frequency of plotting (default: 10)')
parser.add_argument('--max-epoch', type=int, default=50, help='maximum iteration to train (default: 100)')

import argparse

parser = argparse.ArgumentParser(description='Plot results of Simulations')
parser.add_argument('--alg', default = None, nargs='*')
parser.add_argument('--network', default = None, nargs='*')
args = parser.parse_args()

print(args)
print(args.alg)
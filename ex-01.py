import argparse
## Este es un teste en environment repo

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="base")
parser.add_argument("y", type=int, help="exponente")

args = parser.parse_args()

answer = args.x**args.y

if args.quiet:
    print("respuesta: ", answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")




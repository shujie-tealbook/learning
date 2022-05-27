import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()


# parser = argparse.ArgumentParser() # create an argument instance
# parser.add_argument("echo", help="echo the string you use here") # add an positional argument, this argument is required
# args = parser.parse_args() 
# print(args.echo)

parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args() # parse the argument given by the user
# print(args.square ** 2) # now "square" is converted to an instance of args, the type is string

parser.add_argument("--verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
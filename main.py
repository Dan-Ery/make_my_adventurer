import argparse
from adventurer import Adventurer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Adventurer name')
    parser.add_argument('species', help='Adventurer Species (eg. Dwarf/Human/Elf)')
    args = parser.parse_args()
    adventurer = Adventurer(args.name, args.species)
    print(adventurer.create_description())

main()
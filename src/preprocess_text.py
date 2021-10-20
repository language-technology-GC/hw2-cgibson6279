#!/usr/bin/env python 
"""
Write phones column to training file with space 
between each UTF-8 character.
"""

import argparse

import csv

import typing


def main(args: argparse.Namespace) -> None:
    # Open file
    with open(args.input, "r", encoding="UTF-8") as csv_file:
        with open(args.word, "w", encoding = "UTF-8") as out:
            with open(args.phone, "w", encoding="UTF-8") as phone:
                csv_reader = csv.reader(csv_file, delimiter='\t')
                for line in csv_reader:
                    # Split and join token and join by space.
                    word = list(line[0])
                    processed_word = " ".join(word)
                    print(processed_word, file=out)
                    print(line[1], file = phone)
    
    # Write to file.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help= "path to input file.")
    parser.add_argument("word", help= "path to output file for split word.")
    parser.add_argument("phone", help = "path to output file for phones in column two.") 
    main(parser.parse_args())
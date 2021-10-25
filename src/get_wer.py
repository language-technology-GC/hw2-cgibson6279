#!/usr/bin/env python 
import logging

if __name__ == "__main__":
    logging.basicConfig(filename="logging/wer.log", filemode= "w", format="%(message)s", level="INFO")
    with open("predictions.txt", "r", encoding="UTF-8") as src:
        target = []
        pred = []
        for line in src:
            line = line.rstrip().split("\t")
            if line[0].startswith("T"):
                target.append(line[1])
            if line[0].startswith("H"):
                pred.append(line[2])
        corp = list(zip(target,pred))
        # Get WER
        error = 0
        for pair in corp:
            if pair[0] != pair[1]:
                error +=1
        wer = int((error/len(corp))*100)
        logging.info(f"WER:\t {wer}")


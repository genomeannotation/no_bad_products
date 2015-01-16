#!/usr/bin/env python3
import sys
from src.fix import fix_anno

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("usage: main.py <file.tbl>\n")
        sys.exit()

    filename = sys.argv[1]
    with open(filename, 'r') as tbl, open("no_bad_products.log", 'w') as logfile:
        for line in tbl:
            if 'product' not in line:
                sys.stdout.write(line)
            else:
                fields = line.split('\t')
                if len(fields) != 5:
                    sys.stderr.write("error reading this line: " + line +
                            "\n...expected 5 fields. skipping...\n")
                    continue
                original = fields[4].strip()
                fields[4] = fix_anno(fields[4].strip())
                if original != fields[4].strip():
                    logfile.write("changed\t" + original + "\nto\t" + 
                            fields[4].strip() + "\n\n")
                print("\t".join(fields))


###########################################

if __name__ == '__main__':
    main()

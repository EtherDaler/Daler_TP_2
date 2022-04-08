#!/usr/bin/env python3
import sys

my_file = open(sys.argv[1], "w+")
my_file.write("#ifndef INDEX_H\n")
my_file.write("#define INDEX_H\n")
my_file.write("inline int delta(int x, int y){return x-y;}\n")
my_file.write("inline int mult(int x, int y){return x*y;}\n")
my_file.write("#endif")
my_file.close()

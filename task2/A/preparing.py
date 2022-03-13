#!/usr/bin/env python3
my_file = open("index.h", "w+")
my_file.write("#ifndef INDEX_H \n#define INDEX_H")
my_file.write("inline int delta(int x, int y){return x-y;}\n")
my_file.write("inline int mult(int x, int y){return x*y;}\n")
my_file.write("#endif")
my_file.close()

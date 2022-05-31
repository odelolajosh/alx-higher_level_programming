#!/usr/bin/python3
def uppercase(str):
  for ch in str:
    offset = 0
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      offset = ord('A') - ord('a')
    print(f"{(ord(ch) + offset):c}", end='')
  print()

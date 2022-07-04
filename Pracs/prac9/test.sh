#!/bin/bash
n="500"
for i in m q w r l
do
    python3 SortsTestHarness.py ${n} ${i}r >> test.txt
done

for i in m q w r l
do
    python3 SortsTestHarness.py ${n} ${i}a >> test.txt
done

for i in m q w r l
do
    python3 SortsTestHarness.py ${n} ${i}d >> test.txt
done

for i in m q w r l
do
    python3 SortsTestHarness.py ${n} ${i}n >> test.txt
done
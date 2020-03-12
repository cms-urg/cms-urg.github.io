#!/bin/bash

rm -f *.dat
php combined.php | tail -n +4 > combined_table.html
cat pub_header.txt combined_table.html > ../publications.html
sed -i.bak -e '9,27d' ../publications.html 
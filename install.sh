#!/bin/bash
git clone https://github.com/tklijnsma/togoer.git
echo "Add the following line to your .bashrc:"
echo "source $(pwd)/togoer/activate.sh"
rm "${BASH_SOURCE[0]}"
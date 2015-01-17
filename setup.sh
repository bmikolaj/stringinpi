#!/bin/bash
#Setup File
#String in Pi, stringinpi.py v1.0
#Copyright (c) 2015 by Brian Mikolajczyk, brianm12@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

if [ $1 == "install" ]; then
	wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
	if [ ! $(which pip) ]; then
		wget https://bootstrap.pypa.io/get-pip.py -O - | sudo python
	fi
	if [[ $(pydoc -w sympy | head -1 | cut -c1-2) == "no" ]]; then
		sudo pip install sympy
	fi
	sudo pip install sympy --upgrade
	rm setuptools* sympy.html
	echo "String in Pi setup successfully"
	echo "Usage: ./stringinpi.py <integer>"
else
	echo "Usage;"
	echo "'sudo ./setup.sh install' to install"
fi

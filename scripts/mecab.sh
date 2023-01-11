
#! /bin/bash
#
# Copyright 2019 Team KoNLPy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Set mecab related variable(s)
mecab_dicdir="/usr/local/lib/mecab/dic/mecab-ko-dic"

# Exit as soon as we fail
set -e

# Determine OS
os=$(uname)
if [[ ! $os == "Linux" ]] && [[ ! $os == "Darwin" ]]; then
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/konlpy/konlpy/blob/master/scripts/mecab.sh"
    exit 0
fi

# Determine sudo
if hash "sudo" &>/dev/null; then
    sudo="sudo"
else
    sudo=""
fi

# Determine python
# TODO: Prefer python3 and Respect pyenv
python="python3"
if hash "pyenv" &>/dev/null; then
    python="python"
fi

# Determine python site location are writable.
check_python_site_location_is_writable(){
    $python - <<EOF
import site, os
found = False
for dir in site.getsitepackages():
    if not os.path.isdir(dir):
        continue
    if os.access(dir, os.W_OK | os.X_OK):
        found = True
        break
print(1 if found else 0)
EOF
}
at_user_site=""
if [[ "$(check_python_site_location_is_writable)" == "0" ]]; then
    at_user_site="--user"
fi

install_mecab_ko(){
    cd /tmp
    curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
    tar zxfv mecab-0.996-ko-0.9.2.tar.gz
    cd mecab-0.996-ko-0.9.2
    ./configure
    make
    make check
    $sudo make install
}

install_automake(){
    ## install requirement automake1.11
    # TODO: if not [automake --version]
    if [ "$os" == "Linux" ]; then
        if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then
            $sudo apt-get update && $sudo apt-get install -y automake
        elif [ "$(grep -Ei 'fedora|redhat' /etc/*release)" ]; then
            $sudo yum install -y automake diffutils make
        else
            ##
            # Autoconf
            #
            # stage directory
            builddir=`mktemp -d` && cd $builddir

            # download and extract source
            curl -LO http://ftpmirror.gnu.org/autoconf/autoconf-latest.tar.gz
            tar -zxvf autoconf-latest.tar.gz
            rm autoconf-latest.tar.gz

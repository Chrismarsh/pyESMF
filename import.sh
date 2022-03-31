#!/bin/bash
set -e

ESMF_VERSION=$1

rm -rf ${ESMF_VERSION}
mkdir $ESMF_VERSION

# <8.3 naming
#git clone --depth 1 --branch ESMF_${ESMF_VERSION//./_} https://github.com/esmf-org/esmf.git $ESMF_VERSION

git clone --depth 1 --branch v${ESMF_VERSION} https://github.com/esmf-org/esmf.git $ESMF_VERSION

cd ${ESMF_VERSION} 


cp -r src/addon/ESMPy/src tmp
mv LICENSE tmp/
find . -maxdepth 1 -not -name 'tmp' -exec rm -rf {} \;
mv tmp/* .
rm -rf tmp

echo ${ESMF_VERSION} > ESMF_VERSION
cp ../setup.py .
cp ../MANIFEST.in .
cp ../pyproject.toml .
cp ../CMakeLists.txt .
cp ../conanfile.py .

#!/bin/bash
set -e

ESMF_VERSION=$1

rm -rf ${ESMF_VERSION}
mkdir $ESMF_VERSION
git clone --depth 1 --branch ESMF_${ESMF_VERSION//./_} https://github.com/esmf-org/esmf.git $ESMF_VERSION

cd ${ESMF_VERSION} 

# wget -q https://github.com/OSGeo/gdal/archive/v${ESMF_VERSION}.tar.gz -O - \
#     | tar xz --strip-components=4 -C ${ESMF_VERSION} gdal-${ESMF_VERSION}/gdal/swig/python/

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
# ln -s ../README.rst ${ESMF_VERSION}/
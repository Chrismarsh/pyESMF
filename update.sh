#!/bin/bash
set -e

ESMF_VERSION=$1

rm -rf ${ESMF_VERSION}
mkdir $ESMF_VERSION

git clone --depth 1 --branch ESMF_${ESMF_VERSION//./_} https://github.com/esmf-org/esmf.git $ESMF_VERSION

# wget -q https://github.com/OSGeo/gdal/archive/v${ESMF_VERSION}.tar.gz -O - \
#     | tar xz --strip-components=4 -C ${ESMF_VERSION} gdal-${ESMF_VERSION}/gdal/swig/python/

cp -r ${ESMF_VERSION}/src/addon/ESMPy/src ${ESMF_VERSION}/tmp
mv ${ESMF_VERSION}/LICENSE ${ESMF_VERSION}/tmp/
find ${ESMF_VERSION} -not -name 'tmp' -delete -maxdepth 1

# rm -rf ${ESMF_VERSION}/build ${ESMF_VERSION}/README ${ESMF_VERSION}/build ${ESMF_VERSION}/build_config ${ESMF_VERSION}/cmake ${ESMF_VERSION}/makefile ${ESMF_VERSION}/scripts
# find ${ESMF_VERSION} -maxdepth 1 -type f -exec rm -f {} \;

# echo ${ESMF_VERSION} > ${ESMF_VERSION}/ESMF_VERSION
# ln -s ../setup.py ${ESMF_VERSION}/
# ln -s ../MANIFEST.in ${ESMF_VERSION}/
# ln -s ../README.rst ${ESMF_VERSION}/
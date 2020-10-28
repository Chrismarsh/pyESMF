#!/bin/bash
set -e

while read ESMF_VERSION; do
    echo "Processing ${ESMF_VERSION} ..."
    ./import.sh ${ESMF_VERSION}
    ./publish ${ESMF_VERSION}
done <VERSIONS
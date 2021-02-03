# pyESMF

This is an unofficial packaging of the ESMF Python interface that is compatible with pip and with virtual environments. Currently, ESMPy only supports a manual installation or a conda-forge installation. 

## how it works
Because the python bindings require a ESMF compilation, this package automates that using a conan-based installation of ESMF and then packages the ESMF binaries into the virtual environment. Thus, different versions of ESMF can be installed into seperate virtual environments.

__note__:
Currently, only `gfortran` is supported.

## install
This will install the current stable release using ESMF 8.0.1
```
pip install pyESMF
```

This package uses a package-version e.g., `<ESMF-version>.<package-version>` so specific versions can be installed as

`pip install pyESMF==8.0.1.3`

## beta version
The beta snapshots of ESMF 8.1.0 are available using 
```
pip install --pre pyESMF
```

## use
```
$ python

import ESMF
```

## notes

As this relies on a conan build, once the build artifacts are available, pyESMF can be installed into multiple virtual environments without required a ESMF build

### why is there no bdist?

On Linux it is because this links against a non [PEP0513](https://www.python.org/dev/peps/pep-0513/)

However, even on macos, the post processing step in install to correctly patch a python file needed to identify required .mk file are not run with the bdist causing the import to fail.
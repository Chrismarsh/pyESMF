# pyESMF

This is an unofficial packaging of the ESMF Python interface that is compaitible with pip and with virtual environments. Currently, ESMPy only supports a manual installation or a conda-forge installation. 

## how it works
Because the python bindings require a ESMF compilation, this package automates that using a conan-based installation of ESMF and then packages the ESMF binaries into the virtual environment. Thus, different versions of ESMF can be installed into seperate virtual environments.

__note__:
Currently, only `gfortran` is supported.

## install
This will install the current stable release using ESMF 8.0.1
```
pip install pyESMF
```

This package uses a package-version e.g., `<ESMF-version>.<package-version>` so sepecific versions can be installed as

`pip install pyESMF==8.0.1.3`

## beta version
The beta snapshots of ESMF 8.1.0 are available using 
```
pip install --pre pyESMF
```

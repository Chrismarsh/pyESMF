## pyESMF

This is an unofficial packaging of the ESMF Python interface that is compaitible with pip and with virtual environments. Currently, ESMPy only supports a manual installation or a conda-forge installation. 

Because the python bindings require a ESMF compilation, this package automates that using a conan-based installation of ESMF and then packages the ESMF binaries into the virtual environment. Thus, different versions of ESMF can be installed into seperate virtual environments.
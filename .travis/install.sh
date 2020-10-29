#!/bin/bash

set -e

if  [ "$TRAVIS_OS_NAME" = "osx" ]; then

    bash -c 'echo $pyv'
    bash -c 'echo $TRAVIS_PYTHON_VERSION'
    bash -c 'echo $TRAVIS_OS_NAME'

    brew update || true
    brew upgrade || true

   if [ "$test_conda" != "1" ]; then
      brew outdated pyenv || brew upgrade pyenv
      brew install pyenv-virtualenv

      eval "$(pyenv init -)"
      pyenv install $pyv
      pyenv virtualenv $pyv esmf
      pyenv rehash
      pyenv activate esmf
  fi

else
  sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y;
  sudo apt-get update -qq
  sudo apt-get install g++-7
fi

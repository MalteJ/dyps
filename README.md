# dyps

Project Home: [https://github.com/MalteJ/dyps/](https://github.com/MalteJ/dyps/)

## System requirements

You should have git and/or hg installed.
Further you need Python 2.x and the python-yaml library.

## Commands

### dyps run 
ensures that every dependency is present in the right version, or - if no version is defined - the latest version.

### dyps update <dependency>
updates a dependency by pulling from the repository. If it is versioned, the new version number will be saved.

### dyps update-all
The same like `dyps update` but for all dependencies.

### dyps keep <dependency>
Adds the dependency's version number to `dyps.yaml`. Now you can be sure you will always get the same changeset.

### dyps release <dependency>
Releases the dependency's version pinning. At the next `dyps run` the LATEST version will be fetched.

### dyps import-hg-submodules <.hgsub file>
Imports submodules from a given hgsub file and saves the configuration to your `dyps.yaml` file.

## Installation
    python setup.py install

## License
Copyright 2012 Malte Janduda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

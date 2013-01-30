MDN Selenium Tests
============================

This repository holds automated tests for [http://developer.mozilla.org][MOZ]

[MOZ]: http://developer.mozilla.org

The following have all contributed to mdn-tests:

https://github.com/mozilla/mdn-tests/contributors

Running Tests
-------------

### Submodules
Before you start, be sure to get the git submodules:

    git submodule update --init

### Python
Before you will be able to run these tests you will need to have Python 2.6 installed.

####Virtualenv and Virtualenvwrapper (Optional/Intermediate level)
While most of us have had some experience using virtual machines, [virtualenv][venv] is something else entirely.  It's used to keep libraries that you install from clashing and messing up your local environment.  After installing virtualenv, installing [virtualenvwrapper][wrapper] will give you some nice commands to use with virtualenvwrapper.

[venv]: http://pypi.python.org/pypi/virtualenv
[wrapper]: http://www.doughellmann.com/projects/virtualenvwrapper/

__note__

If you do not use virtualenv, you can follow the instructions below to install
the required Python libraries into your global Python installation.

If you don't mind installing globally, just run

    sudo easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__

If you are running on Ubuntu/Debian you will need to first do

    sudo apt-get install python-setuptools

to install the required Python libraries.

### Running tests locally

You will need persona credentials for the site being tested. Get the URL being tested from mozwebqa.cfg in the project root, sign up for that site, and enter the credentials in a yaml file (see credentials.yaml in the project root). To avoid version control conflicts, you may want to store your credentials files separately from your source code.

For all tests to pass, you will need to edit your MDN profile and ensure all fields are filled out.

An example of running all tests without a Selenium Server:

    py.test --driver=firefox --credentials=/path/to/credentials/credentials.yaml --destructive .

An example of running all of the tests in one file:

    py.test --driver=firefox --credentials=/path/to/credentials/credentials.yaml tests/test_sign_in.py

An example of running one test in a file:

    py.test --driver=firefox --credentials=/path/to/credentials/credentials.yaml tests/test_sign_in.py -k test_sign_out

For more command line options see https://github.com/davehunt/pytest-mozwebqa

Writing Tests
-------------

If you want to get involved and add more tests then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/

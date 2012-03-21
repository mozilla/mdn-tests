MDN Selenium Tests
============================

This repository holds automated tests for [http://developer.mozilla.org][MOZ]

[MOZ]: http://developer.mozilla.org

The following have all contributed to mdn-tests:

https://github.com/mozilla/mdn-tests/contributors

Running Tests
-------------

### Python
Before you will be able to run these tests you will need to have Python 2.6 installed.

__note__

The below instructions will install the required Python libraries into your
global Python installation. If you work on multiple Python projects that might
end up needing different versions of the same libraries, you might want to
follow `sudo easy_install pip` with `sudo pip install virtualenv`, and then
create and activate a [virtualenv](http://www.virtualenv.org) (e.g. `virtualenv
caseconductor-tests-env; source case-conductor-tests-env/bin/activate`) to
create a clean "virtual environment" for just this project. Then you can `pip
install -r requiremenst/mozwebqa.txt` in your virtual environment without
needing to use `sudo`.

If you don't mind installing globally, just run

    sudo easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__

If you are running on Ubuntu/Debian you will need to first do

    sudo apt-get install python-setuptools

to install the required Python libraries.

### Running tests locally

To run tests locally it's a simple case of calling py.test from the root directory.

    py.test --driver=firefox

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

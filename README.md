MDN Selenium Tests
============================

This repository holds automated tests for [http://developer.mozilla.org][MOZ]

[MOZ]: http://developer.mozilla.org

The following contributors have submitted pull requests to Mdn-tests:

https://github.com/mozilla/mdn-tests/contributors

Running Tests
-------------

### Java
You will need a version of the [Java Runtime Environment][JRE] installed

[JRE]: http://www.oracle.com/technetwork/java/javase/downloads/index.html

### Python
Before you will be able to run these tests you will need to have Python 2.6 installed.

Run

    easy_install pip

followed by

    sudo pip install pytest 
    sudo pip install pytest-xdist
    sudo pip install selenium
    sudo pip install unittestzero
    sudo pip install pytest-mozwebqa
    
to install the required Python libraries.

### Selenium
Once this is all set up you will need to download and start a Selenium server. You can download the latest Selenium server from [here][Selenium Downloads]. The filename will be something like 'selenium-server-standalone-2.0b1.jar'

To start the Selenium server run the following command:

    java -jar ~/Downloads/selenium-server-standalone-x.x.jar (where x.x is current shipping version)

Change the path/name to the downloaded Selenium server file.

[Selenium Downloads]: http://code.google.com/p/selenium/downloads/list



Once the above prerequisites have been met you can run the tests using the
following command:

    py.test --api=rc --browser=*firefox --baseurl=http://developer-stage9.mozilla.org --timeout=120000

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

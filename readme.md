## GitExtract

This small script can assist in finding secrets in remote `.git` folders in webapplications.

The tool was created to assist in penetration test, where finding a `.git` folder on a webapplication happens more often than not.

This is an example of a class of risks called [source code disclosure](https://portswigger.net/kb/issues/006000b0_source-code-disclosure).

A simple way to fix such problems is to remember that *git/svn are not code deployment tools !*


### Requirements

This script makes use of [TruffleHog](https://github.com/trufflesecurity/truffleHog), which scans git repositories for secrets.
To install the requirements, simply run `pip3 install -r requirements.txt`

Also depends on `wget`.

### Usage

`python3 gitExtract.py <URL>`

The URL format must be of the form `http://example.com/some/dir/.git/`

### Disclaimer

This tool is provided as is and with no guarantees. You are responsible for how you choose to use this tool, do not use this tool without prior authorization of the webapplication owner.

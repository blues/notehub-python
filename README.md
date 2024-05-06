# Blues Notehub Py

![Python Version Support](https://img.shields.io/pypi/pyversions/notehub-py)
![PyPi Version](https://img.shields.io/pypi/v/notehub-py)
![Wheel Support](https://img.shields.io/pypi/wheel/notehub-py)

The notehub-py library is a Python implementation for communicating with the [Blues Notehub API](https://dev.blues.io/reference/notehub-api/api-introduction/)
generated by the [OpenAPI Generator](https://openapi-generator.tech) tool.

This library is auto-generated via the `openapi.yaml` file from the Blues Wireless Notehub project and published
to [PyPi](https://pypi.org/project/notehub-py/) for ease of use in Python-based projects that need to interact with [Notehub.io][notehub].

## Table of Contents 

- [Blues Notehub Py](#blues-notehub-py)
  - [Table of Contents](#table-of-contents)
  - [Package Installation](#package-installation)
  - [Usage](#usage)
  - [Sample Code](#sample-code)
  - [Library Documentation and Code Examples](#library-documentation-and-code-examples)
  - [Project Structure](#project-structure)
    - [High Level Project Overview](#high-level-project-overview)
    - [Root Folder](#root-folder)
    - [`src/` Folder](#src-folder)
  - [Repo Usage](#repo-usage)
    - [Initial Project Setup and Dependencies](#initial-project-setup-and-dependencies)
    - [Modifying the Project](#modifying-the-project)
    - [Updating the Auto-Generated notehub-py Package](#updating-the-auto-generated-notehub-py-package)
    - [Testing the Package Locally](#testing-the-package-locally)
  - [Generate and Publish the Notehub API Python SDK to PyPi](#generate-and-publish-the-notehub-api-python-sdk-to-pypi)
    - [Steps to Publish an Updated notehub\_py Package to PyPi](#steps-to-publish-an-updated-notehub_py-package-to-pypi)
  - [Contributing](#contributing)
    - [Resources](#resources)
  - [To learn more about Blues, the Notecard and Notehub, see:](#to-learn-more-about-blues-the-notecard-and-notehub-see)
  - [License](#license)


## Package Installation

With `pip` via PyPy:

```bash
python3 -m pip install notehub-py
```

or

```bash
python3 -m pip3 install notehub-py
```

## Usage

Once the package is installed, you can import it into a Python file using `import`.

```python
import notehub_py
```

## Sample Code

Here's an example script to fetch all the devices associated with a Notehub project.

The `token` variable declared below is an `X-SESSION-TOKEN` authentication token required for all Notehub API requests.

It can be obtained by using the Notehub Py SDK to call the Notehub API's `/auth/login` endpoint via the `notehub_py.AuthorizationApi` method while supplying a Notehub username and password in the `login_request` object.

Then using the newly generated authentication token to whatever method the package needs, by setting it equal to: `configuration.api_key['api_key'] = token`.

> **NOTE:** Be aware that all Notehub API calls made using the Notehub Py library utilize your account's [Consumption Credits](https://dev.blues.io/reference/glossary#consumption-credit) (CCs). For more information, please consult our [pricing page](https://blues.com/pricing/).

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"  #
)

with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.AuthorizationApi(api_client)
    login_request = {"username":"name@example.com","password":"test-password"} # LoginRequest | 
    api_response = api_instance.login(login_request)
    token = api_response.session_token

configuration.api_key['api_key'] = token

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    device_api_instance = notehub_py.DevicesApi(api_client)
    env_api_instance = notehub_py.EnvironmentVariablesApi(api_client)
    project_uid = 'notehub-project-uid-goes-here' # str | 
    device_uid = 'dev:xxxxxxxxxxxxxxxx' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)

    api_response = device_api_instance.get_device(project_uid, device_uid)
    print("The response of DevicesApi->get_project_device:\n")
    pprint(api_response)
```

## Library Documentation and Code Examples

If you want more information, code examples of how to use each of the Notehub API endpoints are located in the `src/docs/` folder and available on the Blues Developer Experience site.

Each API (device, event, fleet, etc.) had a `.md` file displaying:

* All the HTTP methods it supports,
* A full URL string of what the HTTP request looks like (including required and optional parameters),
* An example of how to implement the code for a particular method inside of a Python file,
* A sample return type from a particular method,
* Required authorization to access the method.

## Project Structure

As this project is partially generated via the OpenAPI Generator tool, it has a rather unique structure and some important files to be aware of.

### High Level Project Overview

```plaintext
.
├── .github/
│   └── workflows/
│       └── GH Action files
├── lib_template/
│   └── python library template files
├── src/
│   ├── notehub_py/
│   │   └── Python-based API and model files
│   ├── docs/
│   │   └── MD documentation
│   ├── test/
│   │   └── unit tests
│   ├── dist/
│   │   └── bundled .tar and .whl binaries for PyPi
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── setup.py
├── openapi.yaml
├── config.json
├── README.md
└── scripts.py
```

### Root Folder

Files and folders to be aware of in the root of the project.

- The [`.github/`](.github/) folder holds the GitHub Actions workflows that automate common tasks in the repo. See the [Modifying the Project](#modifying-the-project) section for further information.

- The [`openapi.yaml`](openapi.yaml) is a key player for this project: it provides the documentation of all the Notehub API endpoints that the OpenAPI Generator tool uses to build the library - without this file, the project doesn't exist.

- The [`lib_template/`](/lib_template/) folder is the Python library template that the OpenAPI generator uses to generate the `src/` folder where auto-generated Python library is created.

> **NOTE:** In many scenarios, downloading the OpenAPI Generator library template is not necessary, but there were some [minor modifications](https://openapi-generator.tech/docs/templating/#modifying-templates) needed in the template's generation to make the package notes published in PyPi more user friendly. Being able to download and modify those files offered the fine-grained control needed when generating the Python library code.

- The [`config.json`](config.json) file is a configuration file of additional properties used by the OpenAPI Generator and its Python library template to define certain variables like package name, version, etc.

- The [`scripts.py`](scripts.py) file is a set of reusable commands to automate the steps of updating this repo and packaging it up for publishing a new version to PyPi.

### `src/` Folder

The `src/` folder inside the root of the project contains the contents of the auto-generated `notehub_py` package that is eventually published to PyPi, including:

- The [`docs/`](src/docs/) folder documenting how to access the API endpoints via the library,
- The internal [`notehub_python/`](src/notehub_python/) folder that holds the Python-based `api` and `model` files for each endpoint,
- The [`test/`](src/test/) folder for unit tests,
- And the `dist/` folder that contains the packaged up `.tar` file (source distribution) and `.whl` file (built distribution) that are uploaded to PyPi.

> **NOTE:** Do not modify the files in the `src/` folder. These are all auto-generated by the OpenAPI Generator tool and the next time the generator command is run to update the library any manual changes will be overwritten.

## Repo Usage

Instructions for how to modify or run this project locally.

### Initial Project Setup and Dependencies 

This project requires [Python v3](https://www.python.org/downloads/) runtime, [pip](https://pypi.org/project/pip/), and the [OpenAPI Generator CLI Tool](https://openapi-generator.tech/).

Follow the installation instructions for Python and pip, and see the note about globally installing the OpenAPI generator CLI below.

> **NOTE:** For best results, it's recommended to install the OpenAPI Generator CLI Tool globally through the terminal.

```bash
npm install @openapitools/openapi-generator-cli -g
```

Now you should be ready to work with the package locally or make changes and modifications.

### Modifying the Project

Most of the files stored at the root of this project should require little to no modifications.

The [`lib_template`](lib_template/) folder holds the Python generator template files the OpenAPI Generator tool relies upon to build its library in the `src/` folder.

The [`.github/`](.github/) folder holds a set of GitHub Actions workflows that automate common tasks like [creating PRs](.github/workflows/create-pr.yml) out of new branches and publishing new releases to PyPi.

The [`openapi.yaml`](openapi.yaml) file is a copy of the one in the Notehub repo (a private Blues repository). Anytime a new version of [Notehub.io][notehub] is deployed and the `openapi.yaml` file there is updated, a fresh copy of that file is added to this project in a new branch via a GitHub Actions workflow.

The [`config.json`](config.json) file is the one that will require changes before a new version of the package is published to PyPi. The [next section](#updating-the-auto-generated-notehub-py-package) will elaborate further.

### Updating the Auto-Generated notehub-py Package

When the `openapi.yaml` file is updated in the original Notehub repo which this library supports, the updated file is copied over into a new feature branch in this repo through the magic of [GitHub Actions](https://github.com/features/actions).

When this occurs, it's time to regenerate the notehub-py Python package based on the newly updated `openapi.yaml`.

**To regenerate the notehub_py package:**

1. Git clone the repo from GitHub.

```shell
$ git clone git@github.com:blues/notehub-py.git
```

2. Check out the newly created remote branch from GitHub locally. (It will be named something like `feat-XYZ`.)
3. Update the `config.json` file at the project's root so the `packageVersion` parameter is incremented (please follow [semantic versioning](https://semver.org/) practices here).
4. At the root of the project, run the following script command from your terminal:

```shell
$ python3 scripts.py generate_package
```

This command will kick off the OpenAPI Generator tool to generate a new copy of the library inside of the `src/` folder, which can then be merged to the `main` repo branch and published to PyPi.

> **NOTE:** If you'd like more information about what exactly the `generate_package` script is doing with its OpenAPI generator CLI commands, you can see the documentation for them [here](https://openapi-generator.tech/docs/usage/).

### Testing the Package Locally

If you'd like to test some changes you've made to the notehub-py API locally before submitting a new PR to the repo, follow steps 1 - 4 above and then use the following commands to migrate to the correct folder and install the dependencies locally:

```bash
cd src/ # <---- path to folder where you want to test the local notehub_python SDK package
python3 -m venv .venv
source ./.venv/Scripts/activate # <---- path to the script to Activate the Python virtual environment may vary
pip3 install -r requirements.txt
```

Once the dependencies are installed, import the library using `import` code and test it out.

```python
import notehub_py

# some more code here
```

All of these directions are also available in the auto-generated [`README.md`](src/README.md) in the `src/` folder as well, for reference.

> **NOTE:** Even testing locally, you will need an `X-SESSION-TOKEN` (this is the 'api-key' referenced in the code examples). See [these directions](https://dev.blues.io/reference/notehub-api/api-introduction/#authentication-with-session-tokens-deprecated) on the Blues Developer Experience site to generate one.

## Generate and Publish the Notehub API Python SDK to PyPi

Although many of the processes around this repository are automated with GitHub Actions, publishing an updated version of the repo requires some human intervention as well.

Run the following commands from the `notehub-py` root directory in this order to make a new version of the `openapi.yaml` file ready to deploy to PyPi.

### Steps to Publish an Updated notehub_py Package to PyPi

1. Update the `"packageVersion"` in the `config.json` file. Follow [semantic versioning](https://semver.org/) for this.

2. Generate the new version of the package.

```bash
python3 scripts.py generate_package
```

3. Rebuild the distribution packages for the PyPi package repository.

```bash
python3 scripts.py build_distro_package
```

4. Commit and push the changes to a new branch in GitHub and open a new pull request when the branch is ready for review. See the [contribution documentation](CONTRIBUTING.md) for further details around a good PR and commit messages.
5. Get the PR approved and merged to `main`.
6. Create a new release with a tag following the [semantic versioning](https://semver.org/) style of [vX.X.X], click the "Generate release notes" button, and publish the release. For example: a new release with a tag named v1.0.2.

## Contributing

We love issues, fixes, and pull requests from everyone. By participating in this project, you agree to abide by
the Blues Inc. [code of conduct].

For details on contributions we accept and the process for contributing, see our
[contribution guide](CONTRIBUTING.md).

### Resources

- [Contributing guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

## To learn more about Blues, the Notecard and Notehub, see:

- [blues.com][blues]
- [notehub.io][notehub]
- [Blues Developer Experience Site][blues.dev]

## License

Copyright (c) 2024 Blues Inc. Released under the MIT license. See
[LICENSE](LICENSE) for details.

[blues]: https://blues.com
[blues.dev]: https://blues.dev
[code of conduct]: https://blues.github.io/opensource/code-of-conduct
[notehub]: https://notehub.io
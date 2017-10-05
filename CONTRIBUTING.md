If you intend to contribute to the project, please make sure you've followed the instructions provided in the [Azure Projects Contribution Guidelines](http://azure.github.io/guidelines/).
## Project Setup
The Azure Storage development team uses Visual Studio so instructions will be tailored to that preference. However, any preferred IDE or other toolset should be usable.

### Install
* Python 2.7, 3.3, 3.4, or 3.5
* Visual Studio 2013 or 2015.
* [Python Tools for Visual Studio](https://www.visualstudio.com/en-us/features/python-vs.aspx)
* Clone the source code from GitHub and then run "python setup.py install" from the azure-storage-python folder.

### Open Solution
Open the project from VS using File->Open->Project/Solution and navigating to the azure-storage-python.sln solution file in the repo base folder.

## Tests

### Configuration
The only step to configure testing is to add a settings_real.py file to the Test folder. You should insert your storage account information into the file using [this](Test/settings_fake.py) as a template.

### Running
To actually run tests, right click the individual test or test class in the Test Explorer panel.

### Testing Features
As you develop a feature, you'll need to write tests to ensure quality. You should also run existing tests related to your change to address any unexpected breaks.

## Pull Requests

### Guidelines
The following are the minimum requirements for any pull request that must be met before contributions can be accepted.
* Make sure you've signed the CLA before you start working on any change.
* Discuss any proposed contribution with the team via a GitHub issue **before** starting development.
* Code must be professional quality
	* No style issues
	* You should strive to mimic the style with which we have written the library
	* Clean, well-commented, well-designed code
	* Try to limit the number of commits for a feature to 1-2. If you end up having too many we may ask you to squash your changes into fewer commits.
* [ChangeLog.md](ChangeLog.md) needs to be updated describing the new change
* Thoroughly test your feature

### Branching Policy
Changes should be based on the **dev** branch, not master as master is considered publicly released code. Each breaking change should be recorded in [BreakingChanges.md](BreakingChanges.md).

### Adding Features for All Platforms
We strive to release each new feature for each of our environments at the same time. Therefore, we ask that all contributions be written for both Python 2.7 and 3.3+ (you can validate 3.3, 3.4, and 3.5 with just one of the versions since they are so similar). We recommend writing in Python 3.x first, and then back porting to 2.7. This is much easier than the other direction.

### Review Process
We expect all guidelines to be met before accepting a pull request. As such, we will work with you to address issues we find by leaving comments in your code. Please understand that it may take a few iterations before the code is accepted as we maintain high standards on code quality. Once we feel comfortable with a contribution, we will validate the change and accept the pull request.


Thank you for any contributions! Please let the team know if you have any questions or concerns about our contribution policy.

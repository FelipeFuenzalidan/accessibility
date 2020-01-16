# Accessibility project in python language.
![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-Ckfyk55DtL1a9EApX84jIzIduzXb2qYbtAlVUtUDWhvnbyYX)

### Set up work environment on mac
Open a terminal and run:
* `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* `brew install python3`
* `pip install allure-behave`
* `pip install axe-selenium-python`

### Running Test
Open a terminal and run:
* `behave -f allure_behave.formatter:AllureFormatter -o report_accessibility/results ./features`

### Generate Report
Open a terminal and run:
* `allure generate report_accessibility/results/ -o report_accessibility/reports --clean`
* To see the report `allure open report_accessibility/reports`

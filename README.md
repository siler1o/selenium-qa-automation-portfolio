# Selenium QA Automation Portfolio

A personal UI automation project by **Reuben Silerio**, applying professional manual QA and test-design experience to **Python, Selenium WebDriver, Pytest, Page Object Model (POM), Allure, Git, and GitHub**.

The project translates documented scenarios into automated checks against [Automation Exercise](https://automationexercise.com/), with a focus on repeatable execution, meaningful assertions, reusable page objects, explicit synchronization, and clear test evidence.

[View Live Allure Report](https://siler1o.github.io/selenium-qa-automation-portfolio/) · [Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) · [Test Scripts](tests/) · [Latest Scenario: TC013](tests/test_TC013_Product_Quantity.py) · [About Reuben](https://github.com/siler1o)

## Current Snapshot

Snapshot updated: **13 September 2026**.

- **13 automated scenarios out of 26 planned** — 50.0% of the planned scenario list, not application-wide coverage.
- **Latest committed Allure snapshot: 12 total, 12 passed.** See the [report statistics](docs/widgets/statistic.json) and [scenario tree](docs/widgets/tree.json).
- TC-013 product-quantity validation is implemented in source code but is not included in the current published Allure snapshot.
- Coverage includes registration, authentication, logout, duplicate-email validation, contact-form submission, navigation, product listing, product-detail validation, product search, subscriptions, multi-product cart validation, and product-quantity preservation.
- All thirteen tests use the shared Chrome fixture. TC-002 through TC-013 include named Allure steps and metadata.
- The latest report is published through GitHub Pages as a manually generated snapshot.

The documented local environment is Windows with Google Chrome, Python 3.11.4, Pytest 9.1.1, and allure-pytest 2.16.0; the report is built with Allure CLI 3.16.0. The result above is a snapshot of a local run, not a CI result, application-wide coverage measurement, or guarantee that future runs will pass.

## Automated Scenarios

| ID | Scenario | Main checks |
| --- | --- | --- |
| [TC-001](tests/test_TC001_Register.py) | Register user | Generates a unique UUID-based email and verifies the visible ACCOUNT CREATED confirmation. |
| [TC-002](tests/test_TC002_Valid_Login.py) | Valid login | Verifies the login form and confirms that valid credentials display the logged-in navigation indicator. |
| [TC-003](tests/test_TC003_Invalid_Login.py) | Invalid login | Verifies the exact invalid-credentials message and confirms that Signup / Login remains available. |
| [TC-004](tests/test_TC004_Logout_User.py) | Logout | Logs in and out, then verifies both the logged-out indicator and redirected login heading. |
| [TC-005](tests/test_TC005_Existing_Email.py) | Existing-email registration | Verifies the duplicate-email error and confirms that the signup form remains displayed on the /signup route. |
| [TC-006](tests/test_TC006_Contact.py) | Contact Us form | Validates the attachment path, submits the form, accepts the alert, checks the exact success message, and returns to the homepage. |
| [TC-007](tests/test_TC007_Test_Case.py) | Test Cases navigation | Verifies the Test Cases heading, expected text, and /test_cases destination. |
| [TC-008](tests/test_TC008_Products_Page.py) | Products and product details | Verifies the All Products heading, confirms that product cards are present, opens the first product, and validates its name, category, price, availability, condition, and brand. |
| [TC-009](tests/test_TC009_Product_Search.py) | Product search | Searches for `Blue Top`, verifies the Searched Products heading, requires at least one visible result, and checks that every returned product card contains the search phrase using a case-insensitive comparison. |
| [TC-010](tests/test_TC010_Subscription.py) | Homepage subscription | Verifies the homepage URL, scrolls to the subscription section, checks the heading is visible, submits a valid test email, and checks the visible confirmation message against the expected text. |
| [TC-011](tests/test_TC011_Subscription_Cart.py) | Cart-page subscription | Opens the Cart page, scrolls to its subscription section, submits a valid test email, and verifies the exact visible success message. |
| [TC-012](tests/test_TC012_Add_Products.py) | Add products to cart | Adds the first two listed products, verifies both product links are visible in the cart, compares cart unit prices with prices captured from the listing, checks quantity 1, and verifies each displayed total. |
| [TC-013](tests/test_TC013_Product_Quantity.py) | Product quantity in cart | Opens the first product, changes and verifies the quantity field as 4, adds the item, confirms the Cart route, compares the cart product name with the captured detail-page name, and verifies that quantity 4 is preserved. |

## Implementation Highlights

- Refactored TC-001 through TC-007 to use a shared Pytest browser fixture and improved their assertions, naming, synchronization, and reporting.
- Added UUID-based registration data to prevent TC-001 from failing because of reused email addresses.
- Added Allure features, stories, titles, severity levels, and readable step-level reporting to TC-002 through TC-013.
- Strengthened validations for login, invalid login, logout, existing-email registration, Contact Us, and Test Cases navigation.
- Made the TC-006 attachment path portable by resolving it from the test file and verifying that the file exists before uploading.
- Centralized reusable locators and interactions in page objects, including a `ProductPage` reused by TC-008, TC-009, TC-012, and TC-013.
- Used visibility and clickability conditions instead of depending only on fixed timing.
- Learned to validate a collection of product elements with visibility_of_all_elements_located and len().
- Added product-detail value checks while normalizing whitespace from Selenium element text.
- Extended `ProductPage` with search-field, search-button, and result-heading methods for TC-009.
- Validated search results with a non-empty-list assertion followed by `all()` and `.lower()`. This checks every returned card for the search phrase; it is not a separate test of the search engine's case sensitivity.
- Added homepage subscription methods in `LoginPage` for TC-010, using JavaScript `scrollIntoView`, explicit waits, and exact confirmation-text validation.
- Reused the homepage subscription interactions for TC-011 on the Cart page.
- Added parent-scoped CSS selectors for cart rows and captured listing prices dynamically before validating cart unit prices and totals in TC-012.
- Added a focused `HomePage` object and reused existing product and cart methods for TC-013.
- Added input-value validation with `get_attribute("value")` and confirmed that a quantity of 4 is preserved after adding the selected product to the cart.
- Reduced interference from unrelated third-party advertising by blocking known ad endpoints through Chrome DevTools Protocol in the shared fixture.
- Generated an Allure 3 report and published the latest 12/12 passing result through GitHub Pages.

## Project Organization

| Location | Responsibility |
| --- | --- |
| [tests/](tests/) | Test workflows, expected-result assertions, and Allure steps. |
| [pages/home_page.py](pages/home_page.py) | Homepage URL verification and product-detail navigation used by TC-013. |
| [pages/login_page.py](pages/login_page.py) | Login, signup, logout, authentication messages, and subscription interactions. |
| [pages/contact_us.py](pages/contact_us.py) | Contact form fields, attachment upload, alert handling, success message, and home navigation. |
| [pages/navigation_bar.py](pages/navigation_bar.py) | Reusable navigation to Products, Test Cases, and Cart. |
| [pages/products_page.py](pages/products_page.py) | Product listing, product details, search, quantity input, Add to cart, and cart-validation interactions shared by TC-008, TC-009, TC-012, and TC-013. |
| [conftest.py](conftest.py) | Shared Chrome setup, third-party ad-request blocking, and teardown after each test, including assertion failures. |
| [test_data/](test_data/) | Sample attachment used by TC-006. |
| [requirements.txt](requirements.txt) | Python dependencies required by the project. |
| [docs/](docs/) | Generated Allure report published through GitHub Pages. |
| [.gitignore](.gitignore) | Excludes the virtual environment, caches, and local report output. |

Page objects handle locating and interacting with UI elements. Tests describe the business workflow and evaluate returned elements against expected results.

### Visible Learning Progression

TC-001 intentionally retains its original direct-Selenium structure as a foundational example. It now uses the shared fixture, a UUID-based email, and an explicit account-creation wait while preserving some inline locators and fixed sleeps.

TC-002 onward demonstrate the transition toward reusable page objects, explicit waits, clearer assertions, and structured Allure reporting. TC-008 extends that progression with a dedicated product page object, collection handling, and multiple detail validations. TC-009 reuses that object for product search and checks each result against the search phrase. TC-010 adds scrolling to a footer section and distinguishes action methods from methods that return elements for assertions. TC-011 reuses that subscription flow on the Cart page. TC-012 adds multi-product cart interactions, parent-scoped selectors, dynamic price capture, and price, quantity, and total comparisons. TC-013 adds input-value replacement and verification, dynamic product-name capture, and quantity-preservation validation across pages.

## Setup

The recorded local environment uses Python 3.11.4 and Google Chrome on Windows. Install Python, Chrome, and Git before starting. Internet access to the practice website is required.

From PowerShell:

~~~powershell
git clone https://github.com/siler1o/selenium-qa-automation-portfolio.git
cd selenium-qa-automation-portfolio
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
~~~

If PowerShell blocks activation, use ./.venv/Scripts/python.exe instead of python for the install and test commands; no execution-policy change is necessary.

### Test Data and Preconditions

TC-002, TC-004, and TC-005 use a pre-existing practice account specified in the test files. That account must exist for the login and duplicate-email checks to behave as designed. These scenarios do not use the email generated by TC-001.

TC-001 creates a new practice account and currently ends at the account-creation confirmation. Browser teardown does not delete that account. Only use dedicated dummy data on the practice website; never substitute personal or production credentials.

TC-008 validates the current first product and its displayed details. TC-009 uses the search phrase `Blue Top` and checks the visible text of each result card. Catalog changes may require the expected data to be updated. The current search test does not yet cover empty searches, no-match results, partial phrases, or search completeness against a separate catalog.

TC-010 and TC-011 use a dummy email to submit the subscription form and check its on-page confirmation. They do not verify email delivery or persistent subscription storage.

TC-012 expects a fresh browser session and adds products 1 and 2 once each. It captures their current listing prices during execution, then checks that the cart shows both product links, matching unit prices, quantity 1, and matching row totals.

TC-013 opens product 1, replaces the quantity field with 4, captures the displayed product name, and verifies that the same name and quantity appear in the cart. Its test code is committed, while the published report remains the preceding 12/12 snapshot.

## Run the Tests

Run all thirteen tests:

~~~powershell
python -m pytest tests/ -v
~~~

Run an individual scenario:

~~~powershell
python -m pytest tests/test_TC013_Product_Quantity.py -v
~~~

Check test discovery without opening browsers:

~~~powershell
python -m pytest tests/ --collect-only -q
~~~

### Generate Allure Results

Generate fresh raw results for the full suite:

~~~powershell
python -m pytest tests/ -v --alluredir=allure-results --clean-alluredir
~~~

The Python integration records the result files; the separate Allure CLI builds the HTML report. The command above clears previous raw results in `allure-results/`, so archive any evidence you want to retain before running it.

### Generate and Preview an Allure 3 Report

The documented CLI version is 3.16.0. Use `generate` and `open`, following the [Allure 3 generation](https://allurereport.org/docs/v3/generate-report/) and [viewing](https://allurereport.org/docs/v3/view-report/) guides. Do not add the Allure 2 `--clean` flag.

Run from the repository root in PowerShell. Generate into a fresh temporary folder so old report files cannot be mixed with the new run:

~~~powershell
$qaReportBuild = Join-Path ([IO.Path]::GetTempPath()) ("qa-allure-" + [guid]::NewGuid().ToString("N"))
allure.cmd generate ".\allure-results" -o $qaReportBuild
if ($LASTEXITCODE -ne 0) { throw "Allure generation failed. Do not publish." }

$qaReportSource = $qaReportBuild
if (Test-Path (Join-Path $qaReportBuild "awesome\index.html")) {
    $qaReportSource = Join-Path $qaReportBuild "awesome"
}

if (-not (Test-Path (Join-Path $qaReportSource "index.html"))) {
    throw "Generated report index.html was not found."
}
Get-Content (Join-Path $qaReportSource "widgets\statistic.json") -ErrorAction Stop
~~~

Compare the displayed totals with the test run you intend to publish. The recorded snapshot for TC-001 through TC-012 is `{"total":12,"passed":12}`. For a new publication, review any failures and confirm that all 12 intended scenarios appear in the report:

~~~powershell
allure.cmd open $qaReportSource
~~~

Press Ctrl+C to stop the local preview server. This does not delete the results or report files. Keep the same PowerShell session for the next step.

### Publish the Allure Report to GitHub Pages

Allure can put its Awesome report inside an `awesome/` subfolder. Publish the contents of the actual report directory, not an older root report beside it.

Before replacing `docs/`, check `git status --short` and preserve any hand-written files or unpublished edits. This repository uses that folder for generated reports and its empty `.nojekyll` marker. The commands below move the previous copy to a temporary backup, then copy the verified report to the publishing root:

~~~powershell
if (Test-Path ".\docs") {
    $qaDocsBackup = Join-Path ([IO.Path]::GetTempPath()) ("qa-docs-backup-" + [guid]::NewGuid().ToString("N"))
    Move-Item -LiteralPath ".\docs" -Destination $qaDocsBackup -ErrorAction Stop
    Write-Host "Previous report backed up to: $qaDocsBackup"
}

Copy-Item -LiteralPath $qaReportSource -Destination ".\docs" -Recurse -ErrorAction Stop
New-Item ".\docs\.nojekyll" -ItemType File -Force | Out-Null
Test-Path ".\docs\index.html"
Get-Content ".\docs\widgets\statistic.json"
~~~

Confirm that `index.html` exists and the totals still match. Inspect the replacement, then publish:

~~~powershell
git status --short
git add -A docs
git commit -m "docs: update published Allure report"
git push origin main
~~~

These staging commands include only report files. When publishing new test code too, review and explicitly stage its test and page-object files before committing.

GitHub Pages publishes from `main` → `/docs`. Test execution, report generation, and publication are separate steps; running tests alone does not refresh the public report. The reports shown here are local-run snapshots, and CI execution remains planned.

[Open the published Allure report](https://siler1o.github.io/selenium-qa-automation-portfolio/).

### Optional pytest-html Summary

~~~powershell
python -m pytest tests/ -v --html=report.html --self-contained-html
~~~

This creates a separate pytest-html summary rather than the step-level Allure report. Generated report.html, assets/, allure-results/, and allure-report/ output are excluded from Git tracking.

## Test Documentation

The [Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) contains the planned scenarios, priorities, detailed actions, test data, expected results, actual results, and execution history. Scenario IDs connect that manual documentation to the automated scripts.

## Current Scope and Next Steps

This is a personal practice project rather than production automation. Execution currently targets Chrome, and results depend on the availability, behavior, and test data of a public website. Third-party ad requests are blocked through Chrome-specific DevTools commands; this is a controlled test-environment choice, not coverage of the site's advertising behavior. TC-001 still has fixed sleeps and inline locators.

Planned improvements:

- Add automatic screenshots and browser details to failed Allure results.
- Externalize practice-account data and formalize account setup and cleanup.
- Add CI execution with automatic report generation and GitHub Pages deployment.
- Add TC-014: place an order by registering during checkout.
- Refresh the published Allure report after the next selected batch of passing scenarios.
- Continue with checkout coverage from the 26-case roadmap.
- Expand product search with no-match, empty-input, and other data variations.
- Gradually standardize the earlier page objects while preserving the visible learning progression.

These are planned capabilities, not features already implemented.

## Acknowledgements

Thanks to [Automation Exercise](https://automationexercise.com/) for providing a public QA practice website and [test-case scenarios](https://automationexercise.com/test_cases).

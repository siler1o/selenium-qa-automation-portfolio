# Selenium QA Automation Portfolio

[![Selenium CI/CD](https://github.com/siler1o/selenium-qa-automation-portfolio/actions/workflows/selenium-ci.yml/badge.svg)](https://github.com/siler1o/selenium-qa-automation-portfolio/actions/workflows/selenium-ci.yml)

A personal UI automation project by **Reuben Silerio**, applying professional manual QA and test-design experience to **Python, Selenium WebDriver, Pytest, Page Object Model (POM), Allure, Git, and GitHub**.

The project translates documented scenarios into automated checks against [Automation Exercise](https://automationexercise.com/), with a focus on repeatable execution, meaningful assertions, reusable page objects, explicit synchronization, and clear test evidence.

[View Live Allure Report](https://siler1o.github.io/selenium-qa-automation-portfolio/) · [Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) · [Test Scripts](tests/) · [Latest Scenario: TC016](tests/test_TC016_Order_Login_Before_Checkout.py) · [About Reuben](https://github.com/siler1o)

## Current Snapshot

Snapshot updated: **26 September 2026**.

- **16 automated scenarios out of 26 planned** — 61.5% of the planned scenario list, not application-wide coverage.
- **Verified CI snapshot:** [26 September 2026 run](https://github.com/siler1o/selenium-qa-automation-portfolio/actions/runs/36233668616) — **16 passed in 76.02 seconds**, followed by successful Allure deployment, for commit `117447c`.
- **Automated delivery:** GitHub Actions runs the complete suite in headless Chrome on pushes and pull requests. A successful `main` run generates and deploys a fresh Allure report; failed runs cannot replace the published report.
- **Test evidence:** Raw Allure results are retained as a workflow artifact for 14 days, including failed runs. See the [CI/CD workflow](.github/workflows/selenium-ci.yml), [workflow history](https://github.com/siler1o/selenium-qa-automation-portfolio/actions), and [live report](https://siler1o.github.io/selenium-qa-automation-portfolio/).
- Coverage includes registration, authentication, logout, duplicate-email validation, contact-form submission, navigation, product listing, product-detail validation, product search, subscriptions, multi-product cart validation, product-quantity preservation, and three order-placement journeys with delivery and billing address checks.
- All sixteen tests use the shared Chrome fixture and include named Allure steps and metadata.
- The public Allure report is deployed through GitHub Pages only after the complete CI suite passes on `main`.

The documented local environment is Windows with Google Chrome, Python 3.11.4, Pytest 9.1.1, and allure-pytest 2.16.0. CI runs on Ubuntu with Python 3.11 and headless Google Chrome, while Allure CLI 3.16.0 builds the deployment artifact. Each report represents one completed run, not application-wide coverage or a guarantee that future runs will pass.

## Automated Scenarios

| ID | Scenario | Main checks |
| --- | --- | --- |
| [TC-001](tests/test_TC001_Register.py) | Register user | Uses the reusable registration page object, generates a unique email, verifies account creation and the signed-in name, then deletes its test account. |
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
| [TC-014](tests/test_TC014_Order_Register.py) | Register during checkout | Adds a product before registration, resumes checkout, checks delivery and billing address values and order-review name/price/quantity, submits dummy payment details, verifies Order Placed, and deletes its account. |
| [TC-015](tests/test_TC015_Order_Register_Before_Checkout.py) | Register before checkout | Registers before shopping, verifies cart and order-review details and both address sections, places an order with dummy payment data, and deletes its account. |
| [TC-016](tests/test_TC016_Order_Login_Before_Checkout.py) | Login before checkout | Creates a dedicated account during setup, logs out and back in, validates cart and order-review details and both addresses, places an order, then deletes only that account. |

**Coverage boundaries:** TC-014 through TC-016 verify product name, unit price, and quantity at checkout; checkout line-total and overall order-total assertions remain pending. TC-014's delivery-address check currently omits state and postcode; its billing check includes them. Address checks use normalized text containment rather than exact, field-by-field equality. A passing run covers the assertions implemented in code, not every planned tracker check.

## Implementation Highlights

- Refactored TC-001 through TC-007 to use a shared Pytest browser fixture and improved their assertions, naming, synchronization, and reporting.
- Reused `RegistrationPage` across TC-001 and TC-014 through TC-016, with UUID-based emails, account/address entry, confirmation checks, and successful-flow cleanup.
- Kept TC-016 independent of TC-002/TC-004 by creating its own account, then explicitly logging out and logging back in before shopping.
- Compared delivery and billing address text with submitted registration data and captured product names and prices dynamically for the checkout scenarios.
- Added Allure features, stories, titles, severity levels, and readable step-level reporting to TC-001 through TC-016.
- Strengthened validations for login, invalid login, logout, existing-email registration, Contact Us, and Test Cases navigation.
- Made the TC-006 attachment path portable by resolving it from the test file and verifying that the file exists before uploading.
- Centralized reusable locators and interactions in page objects, including a `ProductPage` reused for catalog, cart, checkout, address, and payment interactions.
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
- Added GitHub Actions CI/CD: automated dependency installation, headless-Chrome execution, Allure evidence retention, and gated GitHub Pages deployment after a passing `main` run.

## Project Organization

| Location | Responsibility |
| --- | --- |
| [tests/](tests/) | Test workflows, expected-result assertions, and Allure steps. |
| [pages/home_page.py](pages/home_page.py) | Homepage URL verification, product-detail navigation, and product name/price capture. |
| [pages/login_page.py](pages/login_page.py) | Login, signup, logout, authentication messages, and subscription interactions. |
| [pages/registration_page.py](pages/registration_page.py) | Account information, address entry, preferences, account confirmations, signed-in name, and test-account deletion. |
| [pages/contact_us.py](pages/contact_us.py) | Contact form fields, attachment upload, alert handling, success message, and home navigation. |
| [pages/navigation_bar.py](pages/navigation_bar.py) | Reusable navigation to Products, Test Cases, and Cart. |
| [pages/products_page.py](pages/products_page.py) | Product listing, search, quantity input, cart interactions, checkout, delivery/billing address access, payment form entry, and order confirmation. |
| [conftest.py](conftest.py) | Shared Chrome setup, CI-only headless options, third-party ad-request blocking, and teardown after each test, including assertion failures. |
| [.github/workflows/selenium-ci.yml](.github/workflows/selenium-ci.yml) | GitHub Actions CI/CD pipeline for test execution, Allure artifacts, and gated report deployment. |
| [test_data/](test_data/) | Sample attachment used by TC-006. |
| [requirements.txt](requirements.txt) | Python dependencies required by the project. |
| [docs/](docs/) | Legacy generated report files; current GitHub Pages publication uses the CI deployment artifact. |
| [.gitignore](.gitignore) | Excludes the virtual environment, caches, and local report output. |

Page objects handle locating and interacting with UI elements. Tests describe the business workflow and evaluate returned elements against expected results.

### Visible Learning Progression

TC-001 has been refactored into reusable page-object interactions with explicit waits, unique account data, Allure steps, and account deletion. The same registration methods now support the checkout scenarios.

TC-002 onward demonstrate the transition toward reusable page objects, explicit waits, clearer assertions, and structured Allure reporting. TC-008 extends that progression with a dedicated product page object, collection handling, and multiple detail validations. TC-009 reuses that object for product search and checks each result against the search phrase. TC-010 adds scrolling to a footer section and distinguishes action methods from methods that return elements for assertions. TC-011 reuses that subscription flow on the Cart page. TC-012 adds multi-product cart interactions, parent-scoped selectors, dynamic price capture, and price, quantity, and total comparisons. TC-013 adds input-value replacement and verification, dynamic product-name capture, and quantity-preservation validation across pages. TC-014 through TC-016 extend this into order-placement journeys with registration at different stages, login setup, address checks, dummy payment entry, and order confirmation.

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

TC-001 and TC-014 through TC-016 each create a unique practice account and delete it at the end of a successful flow. TC-016 creates its account as setup, logs out, and logs back in using the same saved credentials; it does not reuse or delete TC-002/TC-004's account. Account deletion is not yet guaranteed after an earlier failure, even though browser teardown still runs. Only use dummy data on the practice website.

TC-008 validates the current first product and its displayed details. TC-009 uses the search phrase `Blue Top` and checks the visible text of each result card. Catalog changes may require the expected data to be updated. The current search test does not yet cover empty searches, no-match results, partial phrases, or search completeness against a separate catalog.

TC-010 and TC-011 use a dummy email to submit the subscription form and check its on-page confirmation. They do not verify email delivery or persistent subscription storage.

TC-012 expects a fresh browser session and adds products 1 and 2 once each. It captures their current listing prices during execution, then checks that the cart shows both product links, matching unit prices, quantity 1, and matching row totals.

TC-013 opens product 1, replaces the quantity field with 4, captures the displayed product name, and verifies that the same name and quantity appear in the cart.

## Run the Tests

Run the complete suite:

~~~powershell
python -m pytest tests/ -v
~~~

Run an individual scenario:

~~~powershell
python -m pytest tests/test_TC016_Order_Login_Before_Checkout.py -v
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

The Python integration records the result files; the separate Allure CLI builds the HTML report. The command above clears previous local results in `allure-results/`. CI stores its own raw-results artifact for 14 days.

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

Compare the displayed totals with the actual Pytest run. The current suite contains 16 scenarios; confirm that all intended tests appear and review any failures before using the report as evidence:

~~~powershell
allure.cmd open $qaReportSource
~~~

Press Ctrl+C to stop the local preview server. This does not delete the results or report files.

### Publish the Allure Report through CI/CD

The [Selenium CI/CD workflow](.github/workflows/selenium-ci.yml) is the primary publishing path:

1. A push or pull request targeting `main` starts the test job.
2. GitHub installs Python 3.11 dependencies and runs the complete suite in headless Chrome.
3. Raw `allure-results` are uploaded as a downloadable artifact for 14 days, even if a test fails.
4. For a successful push to `main`, Allure CLI 3.16.0 generates and verifies the HTML report.
5. GitHub Pages receives the report only after the test job passes.

Pull requests perform CI validation but never deploy. The workflow can also be started from the Actions tab with **Run workflow** on `main`.

Repository administrators must select **Settings → Pages → Build and deployment → Source → GitHub Actions** once. After that one-time setting, report generation, validation, and publication require no manual `docs/` commit.

[Open the workflow history](https://github.com/siler1o/selenium-qa-automation-portfolio/actions) · [Open the published Allure report](https://siler1o.github.io/selenium-qa-automation-portfolio/).

### Optional pytest-html Summary

~~~powershell
python -m pytest tests/ -v --html=report.html --self-contained-html
~~~

This creates a separate pytest-html summary rather than the step-level Allure report. Generated report.html, assets/, allure-results/, and allure-report/ output are excluded from Git tracking.

## Test Documentation

The [Reuben Selenium Test Case Tracker](https://docs.google.com/spreadsheets/d/1E-rbgsHj4jv7pamglMdsREiQnfcl-aHWACqrRmAwD3w/edit?usp=drivesdk) contains the planned scenarios, priorities, detailed actions, test data, expected results, actual results, and execution history. Scenario IDs connect that manual documentation to the automated scripts.

## Current Scope and Next Steps

This is a personal practice project rather than production automation. Execution currently targets Chrome, and results depend on the availability, behavior, and test data of a public website. Third-party ad requests are blocked through Chrome-specific DevTools commands; this is a controlled test-environment choice, not coverage of the site's advertising behavior. Payment checks verify the practice site's UI confirmation, not real payment processing.

Planned improvements:

- Add automatic screenshots and browser details to failed Allure and CI results.
- Externalize practice-account data and ensure account cleanup also runs after failures.
- Add checkout line-total and overall order-total assertions to TC-014 through TC-016.
- Add TC-014 delivery state/postcode checks and strengthen address validation with field-specific assertions and distinct test values.
- Implement TC-017: remove products from the cart, then continue the remaining 26-case roadmap.
- Expand product search with no-match, empty-input, and other data variations.
- Gradually standardize the earlier page objects while preserving the visible learning progression.

These are planned capabilities, not features already implemented.

## Acknowledgements

Thanks to [Automation Exercise](https://automationexercise.com/) for providing a public QA practice website and [test-case scenarios](https://automationexercise.com/test_cases).

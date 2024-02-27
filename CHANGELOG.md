# CHANGELOG



## v0.6.8 (2024-02-27)

### Fix

* fix: separate template and service version ([`2c36948`](https://gitlab.com/ai-services/ai-service-template/-/commit/2c369486725bc9dca3dc019af9e76f14a5fcbe31))


## v0.6.7 (2024-02-27)

### Fix

* fix: remove unused imports ([`b1ef538`](https://gitlab.com/ai-services/ai-service-template/-/commit/b1ef53825709d6fa92d3b406dd948b05678e6fbe))

* fix: use default paths for docs and openapi urls

use env variables FASTAPI_DOCS_URL, FASTAPI_OPENAPI_URL and FASTAPI_GRADIO_INTERFACE_URL to change the default behaviour ([`364727b`](https://gitlab.com/ai-services/ai-service-template/-/commit/364727b1ef3359c7d7522fde07a7d3df20aaaa73))

* fix: add python path to run and test commands ([`483bbde`](https://gitlab.com/ai-services/ai-service-template/-/commit/483bbde6dea6ca4698eb2eb2ad5377dae6b8d824))

### Style

* style: fix formatting using black ([`d3d6047`](https://gitlab.com/ai-services/ai-service-template/-/commit/d3d6047351b66598f924513ffe99c2b1e9d23954))

* style: add service and template version to cli command ([`f08ddff`](https://gitlab.com/ai-services/ai-service-template/-/commit/f08ddff92428cfa65aa7fc559188b4103b652480))


## v0.6.6 (2024-02-19)

### Fix

* fix: separate template version

separate the template version from the service version so that template and service can have different versions ([`ed19025`](https://gitlab.com/ai-services/ai-service-template/-/commit/ed190254062e0f814a68b806264645e1e969d3e9))


## v0.6.5 (2024-02-13)

### Build

* build(deps): bump fastapi from 0.104.1 to 0.109.1

Bumps [fastapi](https://github.com/tiangolo/fastapi) from 0.104.1 to 0.109.1.
- [Release notes](https://github.com/tiangolo/fastapi/releases)
- [Commits](https://github.com/tiangolo/fastapi/compare/0.104.1...0.109.1)

---
updated-dependencies:
- dependency-name: fastapi
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`27f1aac`](https://gitlab.com/ai-services/ai-service-template/-/commit/27f1aac042dc678954f19c7bb95186759675edb3))

### Unknown

* Merge pull request #2 from AmirLavasani/dependabot/pip/fastapi-0.109.1

build(deps): bump fastapi from 0.104.1 to 0.109.1 ([`a7b2d1d`](https://gitlab.com/ai-services/ai-service-template/-/commit/a7b2d1d4c38649f68e0c27b02e355ff11b8b0fd5))


## v0.6.4 (2024-01-30)

### Build

* build: add ruff to reqs ([`1c0d8e8`](https://gitlab.com/ai-services/ai-service-template/-/commit/1c0d8e8c405174eafc70b5dade5de4d6e8dad4e4))

* build: use ruff instead of flake8 ([`729558b`](https://gitlab.com/ai-services/ai-service-template/-/commit/729558b4c12dadf00f787b8e27a0a9ec95a40be3))

### Style

* style: reformat using black ([`717dd4c`](https://gitlab.com/ai-services/ai-service-template/-/commit/717dd4c7bb2241ef454a183848d9f5115c1f8fc1))


## v0.6.3 (2024-01-28)

### Fix

* fix: update print to logger ([`3accda3`](https://gitlab.com/ai-services/ai-service-template/-/commit/3accda3c276eca2845ec93ae344f2d57178c2d47))


## v0.6.2 (2024-01-28)

### Fix

* fix: update uninstall command ([`544f8c2`](https://gitlab.com/ai-services/ai-service-template/-/commit/544f8c2c3a8114479bab9314a8c91fc55f70df20))


## v0.6.1 (2024-01-28)

### Fix

* fix: update docs ([`d9be9af`](https://gitlab.com/ai-services/ai-service-template/-/commit/d9be9af4e1d6181f369e80f7e264ba3e60cf0a14))

### Style

* style: fix lint issues ([`f79263d`](https://gitlab.com/ai-services/ai-service-template/-/commit/f79263d4ca1520f9d8a4bde3ac5b7a4443ac1757))


## v0.6.0 (2024-01-28)

### Feature

* feat: add cli

adding a cli using typer. now after installing the service using pip a command cli will be accessible. the cli has version and run command. ([`226d60d`](https://gitlab.com/ai-services/ai-service-template/-/commit/226d60d7b1e776a6666782a62eea5149339e690f))


## v0.5.5 (2024-01-28)

### Style

* style: change default port to 8080 ([`7a39440`](https://gitlab.com/ai-services/ai-service-template/-/commit/7a39440b5a836870719977a6c5306ca6973ad194))


## v0.5.4 (2024-01-28)

### Fix

* fix: changed python path

changed python path to include src folder. After changing the structure the more standard src/app structure the python path should include src in order for the Makefile commands to work properly without installing the package. ([`3c26074`](https://gitlab.com/ai-services/ai-service-template/-/commit/3c2607473e8f2c3b62b6c1f6a4b7683b7d99271b))


## v0.5.3 (2024-01-28)

### Documentation

* docs: update docs ([`e68647e`](https://gitlab.com/ai-services/ai-service-template/-/commit/e68647e97217de3f8bc2885f907b516bad36bfd6))

### Fix

* fix: add /api/v1 prefix to routes

the current gateway does not strip the prefix from the url. adding fastapi root_path will interfere with swagger html.

The only solution is to add this prefix to each of the routers. the best practice is to strip the prefix in the gateway. it might get updated after changing the gateway. ([`3466a31`](https://gitlab.com/ai-services/ai-service-template/-/commit/3466a3167db707757360820e66c35ffcb33d944e))

* fix: uninstall package after versioning ([`82ec8fc`](https://gitlab.com/ai-services/ai-service-template/-/commit/82ec8fc266a07bf53b0f6bfad257762c4de297e1))


## v0.5.2 (2024-01-28)

### Style

* style: updated gradio interface instance ([`e8b8e7c`](https://gitlab.com/ai-services/ai-service-template/-/commit/e8b8e7c0a6fb4956a895a51d32ff152ffc28b497))


## v0.5.1 (2024-01-24)

### Documentation

* docs: add eureka ([`549c3a3`](https://gitlab.com/ai-services/ai-service-template/-/commit/549c3a3781e9cd120f3a2f838626e128d3af6e41))

### Fix

* fix: change the building order ([`c63a2c2`](https://gitlab.com/ai-services/ai-service-template/-/commit/c63a2c213895985f72a323a7902bf3b25d59c8ca))

### Style

* style: update using black ([`13b591b`](https://gitlab.com/ai-services/ai-service-template/-/commit/13b591be11db48d9dfe2e4847c5c520f5ecd9e21))


## v0.5.0 (2024-01-24)

### Documentation

* docs: update readme

update readme to include all the files needs renaming ([`4257169`](https://gitlab.com/ai-services/ai-service-template/-/commit/4257169328cc7082d3fc052830e2f86c3812dabb))

### Feature

* feat: add eureka

add eureka service registery to the project. It will now register its service name in the serivce discovery provided by EUREKA_URL ([`dc8199d`](https://gitlab.com/ai-services/ai-service-template/-/commit/dc8199d9a78265cd6ac8306d997133338856b78e))

### Fix

* fix: activate env in script ([`eca5d60`](https://gitlab.com/ai-services/ai-service-template/-/commit/eca5d60a3c09978656fa81e1d1d277046efd8a46))


## v0.4.1 (2024-01-22)

### Fix

* fix(testing): rename target

rename Makefile target to avoid keyword similarities ([`ab6c9f9`](https://gitlab.com/ai-services/ai-service-template/-/commit/ab6c9f96418b3864e0806a58e6e9c82675f82054))


## v0.4.0 (2024-01-22)

### Feature

* feat(testing): add pytest and code coverage

add pytest testing and coverage to the project. tests should be written in tests/ folder and can be run by the `make tests` command. ([`200f3c2`](https://gitlab.com/ai-services/ai-service-template/-/commit/200f3c202b120d0e00a338391b1b0cb2a0ebea5c))

### Unknown

* Add pytest-cov to dev requirements ([`d9291a3`](https://gitlab.com/ai-services/ai-service-template/-/commit/d9291a3629c4e28c206d6a3ac6fd0dc47e765e07))


## v0.3.5 (2024-01-22)

### Fix

* fix: make --no-tag the defualt command ([`d3ac7b7`](https://gitlab.com/ai-services/ai-service-template/-/commit/d3ac7b78e60520e23810221ce8285e88bb8ef5c4))


## v0.3.4 (2024-01-22)

### Build

* build: add PSR as dev dependency ([`286d513`](https://gitlab.com/ai-services/ai-service-template/-/commit/286d5138c97abb918efb2364819f5cc2a3e7ef8a))

### Documentation

* docs: add new docuementation ([`bb2a39d`](https://gitlab.com/ai-services/ai-service-template/-/commit/bb2a39da568a8b903eb86b5decfd96d29b79dc3e))

* docs: add docstring to version file

adding docstring to version file explaining the methodology of our versioning ([`edb4bca`](https://gitlab.com/ai-services/ai-service-template/-/commit/edb4bcaadfc3b321cbfd4e122a878b3f1d42477a))

### Feature

* feat: add package building

adding package building commands to makefile to build the .wheel and sdist of the project ([`7656ce1`](https://gitlab.com/ai-services/ai-service-template/-/commit/7656ce10d20111a5b8a0c5556f8fb83fc2ff3c14))

* feat: add versioning command in make

add versioning command to makefile ([`d9717c5`](https://gitlab.com/ai-services/ai-service-template/-/commit/d9717c55f35430c7fc369a9f237b845f82034f2b))

* feat(versioning): testing the angular commit style again

checking the commit style ([`3c3aa8d`](https://gitlab.com/ai-services/ai-service-template/-/commit/3c3aa8d1adc19403982b31f642bd0a75d4049bad))

### Fix

* fix: update the make version command to not add tags ([`6470063`](https://gitlab.com/ai-services/ai-service-template/-/commit/6470063ca6cfdb138eb73f449c65d1d1a60463b4))

* fix: add gradio to requirements

add the missing gradio to requirements ([`8699e67`](https://gitlab.com/ai-services/ai-service-template/-/commit/8699e67e6aa2763332cfbed3b31c8607a6f932b0))

* fix: rename dependency installation command

add pip install and rename the old dependency installation ([`2bfa858`](https://gitlab.com/ai-services/ai-service-template/-/commit/2bfa8586eb376963ca0ec530e7ee5567ff826fb9))

* fix: add make all to pyproject

add make all command as build_command to pyproject, so that versioning will build the project first. ([`6434101`](https://gitlab.com/ai-services/ai-service-template/-/commit/64341014bb067354a476ff5166ef3f64da7fbde0))

* fix: update docs command

update docs command, it seems `docs` is a make default keyword ([`5305724`](https://gitlab.com/ai-services/ai-service-template/-/commit/5305724498be0a66c66e61761cab2b5f0811b15c))

* fix: change the release command

change the release command with tag in order to test if the unauthorized is resolved ([`b4826ae`](https://gitlab.com/ai-services/ai-service-template/-/commit/b4826aed5fa5affab8d12e887547ee024b0917c1))

* fix: update readme commands

update commands to include both  building tags and only-push commands ([`4ba5917`](https://gitlab.com/ai-services/ai-service-template/-/commit/4ba591794192cbe1234add1b8060e606093e7584))

* fix: change upload_to_vcs_release to false

changing the config so that the ([`68ad4d2`](https://gitlab.com/ai-services/ai-service-template/-/commit/68ad4d2421a16b4315540b373d35703b41cce55e))

* fix(versioning): trying fix config for unauthorized gitlab connection ([`98c4f83`](https://gitlab.com/ai-services/ai-service-template/-/commit/98c4f83be2438a1941b9254cc597c969076cba3d))

### Style

* style: update formatting using black ([`cd242e8`](https://gitlab.com/ai-services/ai-service-template/-/commit/cd242e86ee1fa111385b144a8798744c2309ef1c))

### Test

* test: add building to versioning

testing the build_command of the semantic-release ([`f93de37`](https://gitlab.com/ai-services/ai-service-template/-/commit/f93de371c779b7726b5a3079dcf25ec3ec0a2237))

* test: commenting out gitlab token

commenting out gitlab token to resolve unauthorized error ([`1ab4d59`](https://gitlab.com/ai-services/ai-service-template/-/commit/1ab4d591d1933dd78446ec2913b306b6866ed904))

### Unknown

* Add nex-version command ([`c0e18e6`](https://gitlab.com/ai-services/ai-service-template/-/commit/c0e18e66e0a37b72ee1eb3aa645ce0c4f6e0cc84))

* feat (versioning): fixing the commit message

fixing the commit message to be in angular commit style. testing the auto versioning, adding commands to readme ([`1b55076`](https://gitlab.com/ai-services/ai-service-template/-/commit/1b55076e2dffab7039e7a399bab8e585cf9226e4))

* &lt;feat&gt;(versioning): add versioning configs

Adding versioning config to the pyproject using python-semantic-release, testing the auto commit message reading by semantic-release ([`6fd2a65`](https://gitlab.com/ai-services/ai-service-template/-/commit/6fd2a65e98d30cbdc9fd67f78b2fcc2070a8de5f))

* fix lint issue ([`c3b221d`](https://gitlab.com/ai-services/ai-service-template/-/commit/c3b221dc5d2b6b9504c0499c49a3fa388b6aa81f))

* fix lint dir ([`5155788`](https://gitlab.com/ai-services/ai-service-template/-/commit/5155788ee8fe384efa317cffbe08636c97eef03a))

* Add dynaic versioning to package ([`64fc526`](https://gitlab.com/ai-services/ai-service-template/-/commit/64fc5263a1cce57848d64d3e566507d7d1d213fd))

* Add pyproject for packaging ([`35d2866`](https://gitlab.com/ai-services/ai-service-template/-/commit/35d28665292f84364f827b51eeaef798956cdc24))

* Add license for packaging ([`e51d7ae`](https://gitlab.com/ai-services/ai-service-template/-/commit/e51d7ae0aeaaafbfbea64bd8795f5ed87e7d904c))

* update version manually ([`ed41005`](https://gitlab.com/ai-services/ai-service-template/-/commit/ed41005312da2779531b4f971bbf449a7f37e38e))

* move app to src for structure ([`95026fa`](https://gitlab.com/ai-services/ai-service-template/-/commit/95026faac63c0974f504aa4225094cb0afd930c1))

* Update readme ([`88ed715`](https://gitlab.com/ai-services/ai-service-template/-/commit/88ed7154d0157e0fc4ab49fdf7cf3330f3f86b86))

* Fix typo ([`eccf18b`](https://gitlab.com/ai-services/ai-service-template/-/commit/eccf18b0e9cf48ad15dcc0a19a2ef603418c7d23))

* Add creating new project guide ([`6273ea8`](https://gitlab.com/ai-services/ai-service-template/-/commit/6273ea8a3da5843a3fe29b0d03aa646813504533))

* Update errors ([`dd3d56a`](https://gitlab.com/ai-services/ai-service-template/-/commit/dd3d56a875c53d16d18a29e2ae962d7d33a3a63a))

* Add gradio demo ui ([`4a8fbed`](https://gitlab.com/ai-services/ai-service-template/-/commit/4a8fbedb0fd848e923dd2a4dfbe8f4d64facbc16))

* Add comment to change template name ([`85e04e4`](https://gitlab.com/ai-services/ai-service-template/-/commit/85e04e497dcf96af66224e0afa3305bca2aa80fc))

* Add docker commands ([`99fe94d`](https://gitlab.com/ai-services/ai-service-template/-/commit/99fe94d7f2914bdaf8471126791fd60f606d09b2))

* Add error reponse samples ([`2a2cbab`](https://gitlab.com/ai-services/ai-service-template/-/commit/2a2cbab37ba6735224a0aec218039bee582c3868))

* initial commit ([`7b2058c`](https://gitlab.com/ai-services/ai-service-template/-/commit/7b2058c3df7de9b988f98a1e838006e8e2cb6320))

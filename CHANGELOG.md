# Changelog

## [1.4.1](https://github.com/googleapis/python-debugger-client/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#118](https://github.com/googleapis/python-debugger-client/issues/118)) ([2d56dfa](https://github.com/googleapis/python-debugger-client/commit/2d56dfa0703364b0ed5f28008426cda180ab4403))
* **deps:** require proto-plus >= 1.22.0 ([2d56dfa](https://github.com/googleapis/python-debugger-client/commit/2d56dfa0703364b0ed5f28008426cda180ab4403))

## [1.4.0](https://github.com/googleapis/python-debugger-client/compare/v1.3.2...v1.4.0) (2022-07-15)


### Features

* add audience parameter ([8f2963d](https://github.com/googleapis/python-debugger-client/commit/8f2963d5dcaffec289b4653eafd29aa7915ae16f))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#110](https://github.com/googleapis/python-debugger-client/issues/110)) ([8f2963d](https://github.com/googleapis/python-debugger-client/commit/8f2963d5dcaffec289b4653eafd29aa7915ae16f))
* require python 3.7+ ([#112](https://github.com/googleapis/python-debugger-client/issues/112)) ([0265d05](https://github.com/googleapis/python-debugger-client/commit/0265d053c9ec5c82e139268388560213e2f32985))

## [1.3.2](https://github.com/googleapis/python-debugger-client/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#100](https://github.com/googleapis/python-debugger-client/issues/100)) ([2a37072](https://github.com/googleapis/python-debugger-client/commit/2a37072151041db69d2c71fd31a9e5bfa5256218))


### Documentation

* fix changelog header to consistent size ([#101](https://github.com/googleapis/python-debugger-client/issues/101)) ([835df83](https://github.com/googleapis/python-debugger-client/commit/835df83d50beeb0ab452264f2ebb7cc8657b8c0a))

## [1.3.1](https://github.com/googleapis/python-debugger-client/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#75](https://github.com/googleapis/python-debugger-client/issues/75)) ([26f0b3f](https://github.com/googleapis/python-debugger-client/commit/26f0b3f4f0f0ae325d61bdb69e711dee288d8c93))

## [1.3.0](https://github.com/googleapis/python-debugger-client/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#61](https://github.com/googleapis/python-debugger-client/issues/61)) ([57c2e93](https://github.com/googleapis/python-debugger-client/commit/57c2e9396b2b56e7bed4fe49d68f2cb0a9495a22))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([a4fe64d](https://github.com/googleapis/python-debugger-client/commit/a4fe64ddb07ff580ec7ba64fe02629678117a1bf))

## [1.2.1](https://www.github.com/googleapis/python-debugger-client/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([b68553f](https://www.github.com/googleapis/python-debugger-client/commit/b68553ff06d1f13cc77eb64909b53758e1610fd0))
* **deps:** require google-api-core >= 1.28.0 ([b68553f](https://www.github.com/googleapis/python-debugger-client/commit/b68553ff06d1f13cc77eb64909b53758e1610fd0))


### Documentation

* list oneofs in docstring ([b68553f](https://www.github.com/googleapis/python-debugger-client/commit/b68553ff06d1f13cc77eb64909b53758e1610fd0))

## [1.2.0](https://www.github.com/googleapis/python-debugger-client/compare/v1.1.0...v1.2.0) (2021-10-14)


### Features

* add support for python 3.10 ([#41](https://www.github.com/googleapis/python-debugger-client/issues/41)) ([a11ecac](https://www.github.com/googleapis/python-debugger-client/commit/a11ecacecab3f313cdda5128c3b6a1e117c694ab))

## [1.1.0](https://www.github.com/googleapis/python-debugger-client/compare/v1.0.2...v1.1.0) (2021-10-08)


### Features

* add context manager support in client ([#38](https://www.github.com/googleapis/python-debugger-client/issues/38)) ([d8ef19f](https://www.github.com/googleapis/python-debugger-client/commit/d8ef19fdee913a1b8988fd54938bf2b8f4b11233))

## [1.0.2](https://www.github.com/googleapis/python-debugger-client/compare/v1.0.1...v1.0.2) (2021-10-07)


### Bug Fixes

* **deps:** require google-cloud-source-context 1.0.0 ([#35](https://www.github.com/googleapis/python-debugger-client/issues/35)) ([1db551b](https://www.github.com/googleapis/python-debugger-client/commit/1db551b8a06f85377052f0408a59e012677f94ff))

## [1.0.1](https://www.github.com/googleapis/python-debugger-client/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([6387d7c](https://www.github.com/googleapis/python-debugger-client/commit/6387d7c589f7c04f0d832b7976b5fa7d64956d99))

## [1.0.0](https://www.github.com/googleapis/python-debugger-client/compare/v0.1.3...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#18](https://www.github.com/googleapis/python-debugger-client/issues/18)) ([2eb231c](https://www.github.com/googleapis/python-debugger-client/commit/2eb231ca3913485e2d33d7ca1c5aa0a7c69c6872))

## [0.1.3](https://www.github.com/googleapis/python-debugger-client/compare/v0.1.2...v0.1.3) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#14](https://www.github.com/googleapis/python-debugger-client/issues/14)) ([7b1faea](https://www.github.com/googleapis/python-debugger-client/commit/7b1faea9588b66d46bf51da09d337ba90ec7090f))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#10](https://www.github.com/googleapis/python-debugger-client/issues/10)) ([4e55f78](https://www.github.com/googleapis/python-debugger-client/commit/4e55f78e0dfbc4cc804dce8d048c502bdd972ab7))


### Miscellaneous Chores

* release as 0.1.3 ([#15](https://www.github.com/googleapis/python-debugger-client/issues/15)) ([bdc4b8f](https://www.github.com/googleapis/python-debugger-client/commit/bdc4b8f52863c4993dcc8648e0fa50ba1654e3ff))

## [0.1.2](https://www.github.com/googleapis/python-debugger-client/compare/v0.1.1...v0.1.2) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#9](https://www.github.com/googleapis/python-debugger-client/issues/9)) ([e465487](https://www.github.com/googleapis/python-debugger-client/commit/e465487f8c682efdacaf977085d3143af2d146da))

## [0.1.1](https://www.github.com/googleapis/python-debugger-client/compare/v0.1.0...v0.1.1) (2021-07-14)


### Bug Fixes

* disable always_use_jwt_access ([#4](https://www.github.com/googleapis/python-debugger-client/issues/4)) ([cfca4f8](https://www.github.com/googleapis/python-debugger-client/commit/cfca4f85fa8e59d6767536ff016fa9ae5b9a1c97))

## 0.1.0 (2021-06-25)


### Features

* generate v2 ([afdc102](https://www.github.com/googleapis/python-debugger-client/commit/afdc102ffec8e0f2c9129be6200ecebfe66e1cbe))

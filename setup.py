#  Copyright (C) 2023 XuanYang-cn. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setuptools.setup(
    name='etcd-sdk-python',
    version='0.0.1',
    setup_requires=['setuptools_scm'],
    use_scm_version={'local_scheme': 'no-local-version', 'version_scheme': 'release-branch-semver'},
    description="Python client for the etcd3 API",
    long_description=README,
    long_description_content_type='text/markdown',
    author="Yang Xuan",
    author_email='jumpthepig@gmail.com',
    url='https://github.com/xuanyang-cn/pyetcd',
    license="Apache-2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "grpcio>=1.49.1,<=1.53.0",
        "grpcio-tools>=1.49.1,<=1.53.0",
    ],
    keywords='etcd3-sdk-python',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)

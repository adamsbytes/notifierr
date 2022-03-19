''' The application setup.py file '''
from setuptools import find_packages, setup

SHORT_DESCRIPTION = \
    "An API server to receive webhook events from Sonarr and Radarr and send SMS messages."
install_requires = [
    "flask > 2.0.0, < 3.0.0",
    "twilio",
]

setup(
    name="notifierr",
    version='0.1.7',
    description=SHORT_DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/adamsbytes/notifierr",
    author="adamsbytes",
    author_email="adamsbytescode@gmail.com",
    python_requires=">=3.6.0",
    license="GPLv3",
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'notifierr = notifierr.cli:main',
        ],
    },
    scripts=[],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Flask",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Home Automation",
    ],
)

''' The application setup.py file '''
from setuptools import find_packages, setup

install_requires = [
    "flask > 2.0.0, < 3.0.0",
    "twilio >= 7.7.1, < 8.0.0",
]

setup(
    name="notifierr",
    version='0.1.1',
    description="An API server to receive webhook events from Sonarr and Radarr and send SMS messages.",
    long_description=open("README.md").read(),
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
    packages=find_packages(where="notifierr"),
    package_dir={"": "notifierr"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Flask",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: Home Automation",
    ],
)

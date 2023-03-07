from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

VERSION = '0.1.0'

setup(
    name="project",
    version=VERSION,
    description='Django Saas',
    long_description=_README_MD,
    author="Author",
    author_email="<author@gmail.com>",
    license='MIT',
    packages=find_packages(include=['project*']),
    # install_requires=['packages'],
    test_suite="tests",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    keywords='project',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='BenchScript',
    packages=['BenchScript'],
    version='0.0.1',
    license='MIT',
    description='A mathematical based scripting language',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sriram Govindan',
    author_email='sriramgovindanwork@gmail.com',
    url='https://github.com/Bench-ai/BenchScript',
    project_urls={  # Optional
        "Bug Tracker": "https://github.com/Bench-ai/BenchScript/issues"
    },
    install_requires=["<chicken> == <0.1.0>;python_version<'<3.10.0>'",
                      "<dill> == <0.3.6>;python_version<'<3.10.0>'",
                      "<egg> == <0.2.0>;python_version<'<3.10.0>'",
                      "<mpmath> == <1.2.1>;python_version<'<3.10.0>'",
                      "<numpy> == <1.24.1>;python_version<'<3.10.0>'",
                      "<sympy> == <1.11.1>;python_version<'<3.10.0>'",],

    keywords=["pypi", "BenchScript"],  # descriptive meta-data
    classifiers=[  # https://pypi.org/classifiers
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.1o',
    ],
    download_url="https://github.com/Bench-ai/BenchScript/archive/refs/heads/master.zip",
)

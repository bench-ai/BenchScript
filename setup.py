import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='BenchScript',
    python_requires='3.10.0',
    packages=['BenchScript'],
    version='0.0.3',
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
    install_requires=["chicken==0.1.0",
                      "dill==0.3.6",
                      "egg == 0.2.0",
                      "mpmath == 1.2.1",
                      "numpy == 1.24.1",
                      "sympy == 1.11.1"],

    keywords=["pypi", "BenchScript"],  # descriptive meta-data
    classifiers=[  # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.1o',
    ],
    download_url="https://github.com/Bench-ai/BenchScript/archive/refs/heads/master.zip",
)

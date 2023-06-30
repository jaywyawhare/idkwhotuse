from setuptools import setup, find_packages

setup(
    name='idkwhotuse',
    version='1.0.1',
    author='Arinjay',
    author_email='2005441@kiit.ac.in',
    description='''I don't know whot use of this project.''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jaywyawhare/idkwhotuse',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

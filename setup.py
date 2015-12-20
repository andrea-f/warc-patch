from setuptools import setup, find_packages



DESCRIPTION = 'Modified Warc patch to work with Heritrix 1.4'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

setup(name='warcPatch',
    version='0.2',
    author="Andrea F",
    author_email="information@dinx.tv",
    url="http://www.walkabout.xyz",
    license='2-clause BSD',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,

    install_requires=[],

    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
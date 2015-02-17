from setuptools import setup

setup(
    name='changetip',
    version='0.3.3',
    description='ChangeTip helper library',
    url='https://github.com/changecoin/changetip-python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers'
    ],
    keywords=['changetip', 'changecoin', 'bitcoin', 'tipping', 'micropayments'],
    author='ChangeCoin, Inc.',
    author_email='oss@changecoin.com',
    license='MIT',
    install_requires=['requests'],
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=[
        'changetip',
        'changetip.bots',
    ]
)

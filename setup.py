from setuptools import setup

setup(name='changetip',
      version='0.0.1',
      description='ChangeTip helper library',
      url='http://github.com/storborg/funniest',
      long_description=open("README.md").read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      author='ChangeCoin, Inc.',
      author_email='oss@changecoin.com',
      license='MIT',
      install_requires=['requests'],
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['changetip'])

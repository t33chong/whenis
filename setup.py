from setuptools import setup

VERSION='0.0.2'

setup(
    name='whenis',
    version=VERSION,
    description='A command-line utility to convert timestamps between UTC and local timezones.',
    author='Tristan Chong',
    author_email='ong@tristaneuan.ch',
    url='https://github.com/tristaneuan/whenis',
    download_url='https://github.com/tristaneuan/whenis/tarball/{}'.format(VERSION),
    keywords='time zone timezone conversion',
    packages=['whenis'],
    install_requires=['arrow', 'parsedatetime', 'pytz', 'tzlocal'],
    entry_points={'console_scripts': ['whenis=whenis:main']},
    license='MIT'
    )

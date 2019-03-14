from setuptools import setup


def get_description():
    return 'A Python Library for accessing Universal Base Image configuration'


def get_long_description():
    with open('README.md') as f:
        text = f.read()

    # Long description is everything after README's initial heading
    idx = text.find('\n\n')
    return text[idx:]


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name='ubi-config',
    version='0.1.0',
    author='',
    author_email='',
    packages=['ubiconfig',
              'ubiconfig.utils',
              'ubiconfig.utils.api',
              'ubiconfig.config_types'],
    package_data={'ubiconfig': ['utils/config_schema.json']},
    url='https://github.com/release-engineering/ubi-config',
    license='GNU General Public License',
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=get_requirements(),
    project_urls={
        'Documentation': 'https://release-engineering.github.io/ubi-config/',
    },
)

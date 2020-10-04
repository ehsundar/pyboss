from pip._internal.network.session import PipSession
from setuptools import setup
from pip._internal.req import parse_requirements


def load_requirements(file_name):
    reqs = parse_requirements(file_name, session=PipSession())
    return [str(ir.requirement) for ir in reqs]


setup(
    name='pyboss',
    version='0.0.2',
    packages=['pyboss', 'pyboss.source'],
    install_requires=load_requirements('requirements.txt'),
    url='https://github.com/ehsundar/pyboss',
    license='GPL-3.0-only',
    author='Amir Ehsandar',
    author_email='ehsandaramir@gmail.com',
    description='Manage your app\'s configurations from multiple sources, e.g. Env, File, Redis, MongoDB, ...'
)

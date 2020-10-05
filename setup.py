from setuptools import setup


def load_requirements(file_name):
    with open(file_name, 'r') as f:
        return list(f.readlines())


setup(
    name='pyboss',
    version='0.0.3',
    packages=['pyboss', 'pyboss.source'],
    install_requires=load_requirements('requirements.txt'),
    url='https://github.com/ehsundar/pyboss',
    license='GPL-3.0-only',
    author='Amir Ehsandar',
    author_email='ehsandaramir@gmail.com',
    description='Manage your app\'s configurations from multiple sources, e.g. Env, File, Redis, MongoDB, ...'
)

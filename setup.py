from setuptools import setup

setup(
    name='devops-smart-car',
    version='1.0',
    packages=['smart_carapi', 'smart_carapi.tests', 'smart_carapi.helpers', 'smart_carapi.modules',
              'smart_carapi.car_instance', 'tests', 'helpers', 'modules', 'car_instance'],
    package_dir={'': 'smart_carapi'},
    url='',
    license='',
    author='anaescobar',
    author_email='ana.escobar-llamazares@edu.dsti.institute',
    description='Continuous Testing, Continuous Integration & Continuous Delivery (Deployment) (CI/CD) of an Smart Car REST API developed using Flask'
)

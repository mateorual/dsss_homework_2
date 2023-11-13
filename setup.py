from setuptools import setup, find_packages

setup(
   name='math_quiz',
   version='1.0.0',
   scripts=['math_quiz.py', 'tests_math_quiz.py'],
   description='A module to generate some random arithmetic operations, ask for an answer to the user and give a feedback',
   author='Mateo Ruiz Alvarez',
   author_email='mateo.a.ruiz@fau.de',
   packages=find_packages(),
   install_requires=[]
)
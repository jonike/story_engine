"""
setup.py file. Part of the StoryTechnologies project.

December 21, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from setuptools import setup, find_packages

setup(name='story-engine',
      version='0.1.0',
      description='A high-level semantic description of stories -including 3D environments- using a bespoke topic map-based graph database',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
      ],
      keywords='story engine, storytelling, 3d environments',
      url='https://github.com/brettkromkamp/story_engine',
      author='Brett Alistair Kromkamp',
      author_email='brett.kromkamp@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'connexion', 'flask-cors', 'gevent', 'topic-db'
      ],
      include_package_data=True,
      zip_safe=False)

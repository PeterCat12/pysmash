from distutils.core import setup


setup(name="pysmash",
      author="Peter Wensel",
      url="https://github.com/PeterCat12/pysmash",
      description="python bindings for Smash.gg API",
      version="2.0.8",
      packages=[
          'pysmash',
      ],
      install_requires=[
        'requests==2.12.1',
    ],
)


# from setuptools import setup
#
# setup(name='funniest',
#       version='0.1',
#       description='The funniest joke in the world',
#       url='http://github.com/storborg/funniest',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['funniest'],
#       install_requires=[
#           'markdown',
#       ],
#       zip_safe=False)

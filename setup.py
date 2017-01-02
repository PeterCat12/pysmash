from distutils.core import setup


setup(name="pysmash",
      author="Peter Wensel",
      url="https://github.com/PeterCat12/pysmash",
      description="python bindings for Smash.gg API",
      version="2.1.2",
      packages=[
          'pysmash',
      ],
      install_requires=[
        'requests==2.12.1',
    ],
)

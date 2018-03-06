try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
          'description' : 'My Project',
          'author' : 'Satyaki Mitra',
          'url' : 'URL to get it at.',
          'download_url' : 'Where to download it.',
          'author_email' : 'satyaki.mitra93@gmail.com',
          'version' : '0.1',
          'install_requires' : ['nose'],
          'packages' : ['dragon_game'],
          'scripts' : [],
          'name' : 'projectname'
          }


setup(**config)

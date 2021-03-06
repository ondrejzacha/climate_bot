#!/usr/bin/env python3
from setuptools import setup

setup(name='climabot',
      version='0.1',
      description='ClimateChange hackathon bot for assessing credibility scores',
      url='https://github.com/IsThisAnExpert/climate_bot',
      author='Francisco Arcila',
      author_email='farcilas@gmail.com',
      license='GNU Affero General Public License v3.0',
      packages =  ['climabot'],
      keywords=['Climate Change', 'fact-checking', 'FFF', 'scientist for future', 'S4FHD'],
      scripts=['climabot/db_query_api.py', 'climabot/clima_bot.py'],
      install_requires=[
          'pandas',
            'pymysql',
            'mysqlclient',
            'configobj',
            'tweepy'
      ],

      zip_safe=False)

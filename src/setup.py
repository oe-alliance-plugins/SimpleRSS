from setuptools import setup
import setup_translate

pkg = 'Extensions.SimpleRSS'
setup(name='enigma2-plugin-extensions-simplerss',
       version='3.0',
       description='rss viewer for the enigma2 gui',
       package_dir={pkg: 'SimpleRSS'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'plugin.png', 'icons/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

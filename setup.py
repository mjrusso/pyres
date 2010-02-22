from setuptools import setup, find_packages
    
version='0.5.0'
setup(
    name='pyres',
    version=version,
    description='Python resque clone',
    author='Matt George',
    author_email='mgeorge@gmail.com',
    maintainer='Matt George',
    license='MIT',
    url='http://github.com/binarydud/pyres',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_data={'resweb': ['templates/*.mustache','media/*']},
    download_url='http://cloud.github.com/downloads/binarydud/pyres/pyres-v%s.tar.gz' % version,
    include_package_data=True,
    scripts=['scripts/pyres_worker', 'scripts/pyres_web'],
    install_requires=[
        'simplejson>=2.0.9',
        'itty>=0.6.2',
        'redis>=0.6.0',
        'pystache>=0.1.0',
        'grizzled>=0.9.3'        
    ],
    classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python'],
)
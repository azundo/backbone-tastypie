#!/usr/bin/env python
from distutils.core import setup
import os


# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('backbone_tastypie_mixin'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('backbone_tastypie_mixin/'):] # Strip "backbone_tastypie_mixin/"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
print data_files
setup(
    name='Backbone-tastypie-mixin',
    version='0.2',
    description='A small conversion layer to make backbone.js and '
        'django-tastypie work together happily. Modified from backbone_tastypie by Ben Best',
    author='Paul Uithol',
    author_email='paul.uithol@gmail.com',
    url='https://github.com/azundo/backbone-tastypie-mixin',
    packages=['backbone_tastypie_mixin'],
    package_data={'backbone_tastypie_mixin': data_files},
)

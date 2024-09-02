import os
import shutil
import sys
import time
from livereload import Server, shell

OUTPUT_PATH = 'output'

def clean():
    """Remove generated files"""
    if os.path.isdir(OUTPUT_PATH):
        shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)

def build():
    """Build local version of site"""
    os.system('pelican content')

def rebuild():
    """`build` with the delete switch"""
    os.system('pelican content -d')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(OUTPUT_PATH)
    os.system('python -m http.server')

def reserve():
    """Build and then serve"""
    build()
    serve()

def livereload():
    """Automatically reload browser tab upon file modification."""
    server = Server()
    server.watch('content/*.md', shell('pelican content -o output -s pelicanconf.py'))
    server.watch('content/pages/*.md', shell('pelican content -o output -s pelicanconf.py'))
    server.watch('themes/piney/templates/*.html', shell('pelican content -o output -s pelicanconf.py'))
    server.watch('themes/piney/static/css/*.css', shell('pelican content -o output -s pelicanconf.py'))
    server.watch('pelicanconf.py', shell('pelican content -o output -s pelicanconf.py'))
    server.serve(root=OUTPUT_PATH)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
    else:
        rebuild()
        livereload()

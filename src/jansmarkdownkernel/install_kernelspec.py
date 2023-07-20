#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""Kernel installer"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

json ="""{"argv":["python","-m","jansmarkdownkernel", "-f", "{connection_file}"],
 "display_name":"Markdown"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="300"
   height="300"
   viewBox="0 0 300 300"
   version="1.1"
   id="svg196"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs200" />
  <g
     id="g312"
     transform="matrix(1.4423077,0,0,1.4423077,-8.0000001e-7,57.692307)">
    <rect
       width="198"
       height="118"
       x="5"
       y="5"
       ry="10"
       stroke="#000000"
       stroke-width="10"
       fill="none"
       id="rect192"
       style="stroke:#ff6600" />
    <path
       d="M 30,98 V 30 H 50 L 70,55 90,30 h 20 V 98 H 90 V 59 L 70,84 50,59 v 39 z m 125,0 -30,-33 h 20 V 30 h 20 v 35 h 20 z"
       id="path194"
       style="fill:#ff6600" />
  </g>
</svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/jansmarkdownkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jansmarkdownkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jansmarkdownkernel')
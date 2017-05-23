##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
"""Schema for repos.yaml configuration file.

.. literalinclude:: ../spack/schema/test.py
   :lines: 32-

"""
schema = {
    '$schema': 'http://json-schema.org/schema#',
    'title': 'Spack test configuration file schema',
    'type': 'object',
    'definitions': {
        'test-suite': {
            "required": ["packages", "packages", 'compilers'],
            'include': {
                'type': 'array',
                'default': [],
                'items': {'type': 'string'}
            },
            'exclude': {
                'type': 'array',
                'default': [],
                'items': {'type': 'string'}
            },
            'packages': {
                'type': 'array',
                'default': [],
                'additionalProperties': False,
                'patternProperties': {
                    r'\w[\w-]*': {  
                        'type':  'array',
                        'default': [],
                        'additionalProperties': False,
                        'properties': {
                            'versions': {
                                'type': 'array',
                                'default': [],
                                'items': {'type': 'string'}, 
                            }, 
                        }, 
                    },
                },
            },
            'compilers': {
                'type': 'array',
                'default': [],
                'additionalProperties': False,
                'patternProperties': {
                    r'\w[\w-]*': {  
                        'type':  'array',
                        'default': [],
                        'additionalProperties': False,
                        'properties': {
                            'versions': {
                                'type': 'array',
                                'default': [],
                                'items': {'type': 'string'}, 
                            }, 
                        }, 
                    },
                },
            },
            'cdash': {
                'type': 'array',
                'default': [],
                'items': {'type': 'string'}
            },
            'project': {
                "type": "string"
            },
        },
    },
}

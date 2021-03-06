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
from spack import *


class Nalu(CMakePackage):
    """Nalu: a generalized unstructured massively parallel low Mach flow code
       designed to support a variety of energy applications of interest (most
       notably Wind ECP) built on the Sierra Toolkit and Trilinos solver
       Tpetra/Epetra stack
    """

    homepage = "https://github.com/NaluCFD/Nalu"
    url      = "https://github.com/NaluCFD/Nalu.git"

    version('master',
            git='https://github.com/NaluCFD/Nalu.git', branch='master')

    variant('debug', default=False,
            description='Builds a debug version')

    # Currently Nalu only builds static libraries; To be fixed soon
    depends_on('yaml-cpp+fpic~shared')
    depends_on('trilinos~shared+tpetra+muelu+belos+ifpack2+amesos2+zoltan+stk+boost~superlu-dist+superlu+hdf5+zlib+pnetcdf@master')

    def build_type(self):
        if '+debug' in self.spec:
            return 'Debug'
        else:
            return 'Release'

    def cmake_args(self):
        spec = self.spec
        options = []

        options.extend([
            '-DTrilinos_DIR:PATH=%s' % spec['trilinos'].prefix,
            '-DYAML_DIR:PATH=%s' % spec['yaml-cpp'].prefix,
            '-DENABLE_INSTALL:BOOL=ON'
        ])

        return options

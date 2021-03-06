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


class RRstan(RPackage):
    """User-facing R functions are provided to parse, compile, test, estimate,
    and analyze Stan models by accessing the header-only Stan library provided
    by the 'StanHeaders' package. The Stan project develops a probabilistic
    programming language that implements full Bayesian statistical inference
    via Markov Chain Monte Carlo, rough Bayesian inference via variational
    approximation, and (optionally penalized) maximum likelihood estimation via
    optimization. In all three cases, automatic differentiation is used to
    quickly and accurately evaluate gradients without burdening the user with
    the need to derive the partial derivatives."""

    homepage = "http://mc-stan.org/"
    url      = "https://cran.r-project.org/src/contrib/rstan_2.10.1.tar.gz"

    version('2.10.1', 'f5d212f6f8551bdb91fe713d05d4052a')

    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-stanheaders', type=('build', 'run'))
    depends_on('r-inline', type=('build', 'run'))
    depends_on('r-gridextra', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'))
    depends_on('r-rcppeigen', type=('build', 'run'))
    depends_on('r-bh', type=('build', 'run'))

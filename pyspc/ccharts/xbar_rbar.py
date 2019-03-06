# Copyright (C) 2016  Carlos Henrique Silva <carlosqsilva@outlook.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Modified by Joshua Hyatt <joshua_hyatt@denso-diam.com>

from .ccharts import ccharts
from .tables import A2, D3, D4
import numpy as np


class xbar_rbar(ccharts):

    _title = "Xbar-R Chart"

    def plot(self, data, size, newdata=None):
        assert size >= 2
        assert size <= 10
        newvalues = None

        R, X = [], []  # values
        for xs in data:
            assert len(xs) == size
            R.append(max(xs) - min(xs))
            X.append(np.mean(xs))

        Rbar = np.mean(R)  # center
        Xbar = np.mean(X)

        lcl = Xbar - A2[size] * Rbar
        ucl = Xbar + A2[size] * Rbar

        if newdata is not None:
            newvalues = [np.mean(xs) for xs in newdata]

        return (X, Xbar, lcl, ucl, self._title, newvalues)


class rbar(ccharts):

    _title = "R Chart"

    def plot(self, data, size, newdata=None):
        assert size >= 2
        assert size <= 10
        newvalues = None

        R = []  # values
        for xs in data:
            assert len(xs) == size
            R.append(max(xs) - min(xs))

        Rbar = np.mean(R)  # center

        lcl = D3[size] * Rbar
        ucl = D4[size] * Rbar

        if newdata is not None:
            newvalues = [max(xs) - min(xs) for xs in newdata]

        return (R, Rbar, lcl, ucl, self._title, newvalues)

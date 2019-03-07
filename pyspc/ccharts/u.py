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
import numpy as np


class u(ccharts):

    _title = "U Chart"

    def __init__(self, size=1):
        super(u, self).__init__()

        self.size = size - 1

    def plot(self, data, size, newdata=None):

        sizes, data = data.T
        if self.size == 1:
            sizes, data = data, sizes
            print('oi')

        data2 = sizes / data
        ubar = np.sum(sizes) / np.sum(data)

        lcl, ucl = [], []
        for i in data:
            lcl.append(ubar - 3 * np.sqrt(ubar / i))
            ucl.append(ubar + 3 * np.sqrt(ubar / i))

        return (data2, ubar, lcl, ucl, self._title, newdata)

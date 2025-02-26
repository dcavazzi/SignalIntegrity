"""Series capacitance"""

# Copyright (c) 2018 Teledyne LeCroy, Inc.
# All rights reserved worldwide.
#
# This file is part of SignalIntegrity.
#
# SignalIntegrity is free software: You can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation, either
# version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>

from SignalIntegrity.Lib.Devices.SeriesG import SeriesG
from numpy import math

def SeriesC(C,f,Z0=None,df=0.,esr=0.):
    """Series Capacitance
    @param C float capacitance
    @param f float frequency
    @param Z0 (optional) float of complex reference impedance (defaults to 50 Ohms)
    @param df (optional) float dissipation factor (or loss-tangent) (defaults to 0)
    @param esr (optional) float effective-series-resistance (defaults to 0)
    @return the list of list s-parameter matrix for a series capacitance
    """
    G=C*2.*math.pi*f*(1j+df)
    try: G=G+1/esr
    except: pass
    return SeriesG(G,Z0)
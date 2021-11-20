# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThermalMetrics
                                 A QGIS plugin
 This plugin helps to calculate basic metrics and indices from thermal images. 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-02
        copyright            : (C) 2021 by Florian Ellsäßer
        email                : info@ecothermographylab.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ThermalMetrics class from file ThermalMetrics.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .thermalmetrics import ThermalMetrics
   
    return ThermalMetrics(iface)

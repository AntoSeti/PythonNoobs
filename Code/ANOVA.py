# -*- coding: utf-8 -*-
"""

"""

import numpy
import pandas
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

data = pandas.read_csv('nesarc.txt', low_memory=False)
print data['S3AQ3B1']
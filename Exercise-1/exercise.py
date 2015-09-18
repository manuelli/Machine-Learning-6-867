__author__ = 'manuelli'

import numpy as np
import math

data = np.array([0.9,1,1.1,1.2,3,3.1])

def MLMean():
    return data.mean()

def MLVar():
    mu = MLMean()
    a = data - mu
    a = np.power(a,2)
    var = a.mean()
    return var

def computeLikelihood(mu,var):
    const = 1/np.sqrt(2*np.pi*var)
    log_const = np.log(const)
    xbar = data - mu
    a = -1/(2*var)*np.power(xbar,2)
    log_likelihood = np.size(data)*log_const + a.sum()
    print "log likelihood is "
    print log_likelihood

    likelihood = math.exp(log_likelihood)
    print "likelihood is "
    print likelihood

def main():
    print "using var = 0.25"
    mu = MLMean()
    var = 0.25
    computeLikelihood(mu,var)

    print "using var_ML"
    var_ML = MLVar()
    computeLikelihood(mu,var_ML)




if __name__=="__main__":
    print "using var = 0.25"
    mu = MLMean()
    var = 0.25
    computeLikelihood(mu,var)

    print "using var_ML"
    var_ML = MLVar()
    computeLikelihood(mu,var_ML)


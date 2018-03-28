import numpy as np
from scipy.integrate import odeint
from scipy import interpolate
from scipy.integrate import quad
from scipy.interpolate import splrep
from scipy.interpolate import splev
from scipy.interpolate import UnivariateSpline
from scipy.misc import derivative
from scipy.optimize import fsolve
import transfer_func as tf
from scipy.special import gamma
def n(self,z,z0,alpha,beta):
    return ((beta/z0)/(gamma((1.+alpha)/beta)))*((z/z0)**alpha)*np.exp(-((z/z0)**beta))
def intg(self,z3,z,z0,alpha,beta):
    return (1.-self.co_dis_z(z3)/self.co_dis_z(z))*self.n(z3,z0,alpha,beta)
def g(self,z,z0,alpha,beta):  
    return quad(self.intg,z,5.,args=(z,z0,alpha,beta,))[0]
def intpl_wh(self,z,l,z0,alpha,beta):
    return (l*(l+1.)/(2.*np.pi))*((1./self.D_H())**3.)*(9./4.)*(self.Om0**2.)*((1.+z)**2.)*self.invhub(z)*((self.g(z,z0,alpha,beta))**2.)*self.Pk_wh((l/self.co_dis_z(z)),z)
def Pl_wh2(self,l,z0,alpha,beta): 
    return quad(self.intpl_wh,0.001,5.,args=(l,z0,alpha,beta,))[0]
def Pl_wh(self,l,z0,alpha,beta): 
    return np.vectorize(self.Pl_wh2)(l,z0,alpha,beta)
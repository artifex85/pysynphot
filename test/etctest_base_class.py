import os
from pytools import testutil
from pysynphot import locations
from pysynphot.newobservation import Observation 

class ETCTestCase(testutil.FPTestCase):
    """Base class for cases generated from the ETC test listings"""
    def setUp(self):
        self.oldpath=os.path.abspath(os.curdir)
        os.chdir(locations.specdir)
        self.setparms()
        if self.sp is not None:#Skip the base class!!
            self.obs=Observation(self.sp,self.bp)
        
    def setparms(self):
        self.sp=None
        self.bp=None
        self.ref_rate=None
        self.file=None
        self.cmd=None
        
    def tearDown(self):
        os.chdir(self.oldpath)
                                     
    def testrate(self):
        if self.sp is not None:
            self.assertApproxFP(self.obs.countrate(),self.ref_rate)
                
#    def testfile(self):
#        """Need to figure out where to keep reference files"""
#        pass


FROM keyi/python2-mcr2017a-rpi-isl

COPY JSTMB_O4550/ ./JSTMB_O4550
COPY setup.py ./
COPY O4550_JSTMB_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./


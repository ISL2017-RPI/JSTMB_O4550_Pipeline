import sys
import JSTMB_O4550
import numpy as np

def JSTMB(data_file = 'trainData.csv', target_file = 'trainTargets.csv'):
    my_JMI = JSTMB_O4550.initialize()
    feat = my_JMI.JSTMB_primitive_O4550(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = sys.argv[1]
    target = sys.argv[2]
    selected_feature = np.array(JSTMB(data, target), dtype=np.int16)
    np.savetxt('Features_O4550_JMI.csv', selected_feature, delimiter=',')
    print selected_feature

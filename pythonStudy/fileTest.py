#!/usr/bin/python
import csv

out_file = 'scene1.csv'

ax = [1,2, 3,4] ; ay = [3,5,6,7]; az = [1,3,5,6] 
tem = [28,29,27,28]; hum = [20,40,50,60]; ecg = [1,1,1,1]
#thrput_ecg_new = [10, 10,10,10], thrput_acc_new = [], thrput_tem_new = [] 
#thrput_ecg_base = [], thrput_acc_base = [], thrput_tem_base = [] 
#thrput_ecg = [thrput_ecg_new, thrput_ecg_base]
#thrput_acc = [thrput_acc_new, thrput_acc_base]
#thrput_tem = [thrput_tem_new, thrput_tem_base] 
#
#pdr_ecg_new = [], pdr_ecg_base = []
#pdr_acc_new = [],pdr_acc_base = []
#pdr_tem_new = [],pdr_tem_base = []
#pdr_ecg = [pdr_ecg_new, pdr_ecg_base]
#pdr_acc = [pdr_acc_new, pdr_acc_base]
#pdr_tem = [pdr_tem_new, pdr_tem_base]
#
acc_ts = [1,2,3,4] ; tem_ts = [1,2,3,4]; ecg_ts = [1,2,3,4] 
#ecg_net_ts_new = [], acc_net_ts_new = [], tem_net_ts_new = []
#ecg_net_ts_base = [], acc_net_ts_base = [], tem_net_ts_base = []
#ecg_net_ts = [ecg_net_ts_new, ecg_net_ts_base]
#acc_net_ts = [acc_net_ts_new, acc_net_ts_base]
#tem_net_ts = [tem_net_ts_new, tem_net_ts_base]
def write_data():
    f = open(out_file, 'w')
    writer = csv.writer(f)
    writer.writerow(['acc_ts', 'ax', 'ay', 'az'])
    for i in range(len(acc_ts)):
        writer.writerow([acc_ts[i], ax[i], ay[i], az[i]])


if __name__ == '__main__':
    write_data()
    


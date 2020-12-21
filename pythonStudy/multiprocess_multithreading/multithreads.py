import threading
import time
import argparse

def generate_sample(thread_name, timefun=time.perf_counter, freq=50):
    count = 0
    delta = 1.0/freq
    # record the start of the sequence of timed periods
    time_start = timefun()
    
    f = open('thread_{}_sample.csv'.format(thread_name), "w")
    f.write("timestamp, abs_time, sample\n")
    total_count = 0
    while total_count < 6*freq:               
        try:
            f.write("{},{},{}\n".format(time.time(), time_start, count))
            count+=1                
        except("KeyboardInterrupt"):
            f.close()
        time_next = time_start + delta
        while timefun() < time_next:
            pass
        time_start = time_next
        if count == freq:
            count=0 # break  
        total_count +=1
        
if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--single_thread',
        action='store_true')
    args = parser.parse_args()
    
    if args.single_thread:   
        t1 = threading.Thread(target=generate_sample, args=('t1_single', time.perf_counter, 50))               
        t1.daemon = True
        t1.start()       
        print("Start sample data at 50Hz")                
        t1.join()
        print("End")
    else:    
        t1 = threading.Thread(target=generate_sample, 
            args=('t1_multi', time.perf_counter, 50))
        t2 = threading.Thread(target=generate_sample, 
            args=('t2_multi', time.perf_counter, 50))
        t=time.time()
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()
        print("Start multi threads, sample data at 50Hz")
               
        t1.join()
        t2.join()
        print("End")

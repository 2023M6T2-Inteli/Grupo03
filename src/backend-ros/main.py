import os
from multiprocessing import Pool

processes = ('./controllers/battery_controller.py', './controllers/camera_controller.py')


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=2)
pool.map(run_process, processes)
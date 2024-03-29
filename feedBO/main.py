# This is a sample Python script.

import torch
import numpy as np
from botorch.sampling import SobolQMCNormalSampler
from evaluation_func import (generate_initial_data, initialize_model)
from pena_function import Pena_func
from GeneratorSampling import gensamples
from Acq_funct import optimize_qNehvi_and_get_observation
from Bay_Opt import BO_feed

tkwargs = {"dtype": torch.float64,
    "device": torch.device("cuda" if torch.cuda.is_available() else "cpu"),
}


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#seeds = np.random.randint(1, 300000, 1)
seeds=np.array([149763])
Seeds = seeds.tolist()
print(Seeds)
x,y=generate_initial_data(50)
print(y)
mll, model =initialize_model(x,y)
sampler = SobolQMCNormalSampler(512)
#optimizer=optimize_qNehvi_and_get_observation(model=model, sampler=sampler, train_x=x)
Exp1 = BO_feed(Seeds=Seeds, Init_samples=50, num_exp=1)

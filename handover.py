import numpy as np
num_timesteps = 18
handover_threshold = 50
timestep = 1

num_bs = 3
bs_locations = np.array([[0,0],[200,0],[100,0]])
ris_location = np.array([100,100])
ue_location = np.array([0,0])
ue_velocity = np.array([10,0])

def update_ue_location(ue_location, ue_vel, timestep):
    ue_location=ue_location + ue_vel*timestep
    return ue_location

def simulate(ue_location, bs_locations):
    distances = np.linalg.norm(bs_locations-ue_location,axis=1)
    print(f'values are {distances[0]}, {distances[1]}, {distances[2]}')
    target_bs = np.argmin(distances)

    if(distances[target_bs] < handover_threshold):
        handover_init = True
    else:
        handover_init = False
    return handover_init, target_bs

for t in range(num_timesteps):
    ue_location = update_ue_location(ue_location, ue_velocity, timestep)

    handover_initiated, target_bs = simulate(ue_location, bs_locations)
    if handover_initiated:
        print(f'Handover initiated to BS {target_bs} at time {t}')
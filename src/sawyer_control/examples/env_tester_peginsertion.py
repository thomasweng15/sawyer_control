#!/usr/bin/python3
from sawyer_control.envs.sawyer_peginsertion import SawyerPegInsertion

env = SawyerPegInsertion(
    action_mode='position',
    config_name='austri_config',
    reset_free=False,
	position_action_scale=0.01,
	max_speed=0.4,
)
env.reset()

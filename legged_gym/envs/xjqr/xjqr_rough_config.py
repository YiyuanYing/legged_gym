from legged_gym.envs.base.legged_robot_config import LeggedRobotCfgPPO, LeggedRobotCfg

class xjqrRoughCfg(LeggedRobotCfg):
    class env:
        num_envs = 4096
        num_observations = 247
        num_privileged_obs = None
        num_actions = 16
        env_spacing = 3.
        send_timeouts = True
        episode_length_s = 20

    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.4]
        default_joint_angles = {
            'FL_hip_joint': 0.3,  # [rad]
            'RL_hip_joint': 0.3,  # [rad]
            'FR_hip_joint': 0.3,  # [rad]
            'RR_hip_joint': 0.3,  # [rad]

            'FL_thigh_joint': -0.6,  # [rad]
            'RL_thigh_joint': -0.8,  # [rad]
            'FR_thigh_joint': -0.6,  # [rad]
            'RR_thigh_joint': -0.8,  # [rad]

            'FL_knee_joint': 0.0,  # [rad]
            'RL_knee_joint': 0.0,  # [rad]
            'FR_knee_joint': 0.0,  # [rad]
            'RR_knee_joint': 0.0,  # [rad]

            'FL_calf_joint': 1.0,  # [rad]
            'RL_calf_joint': 1.2,  # [rad]
            'FR_calf_joint': 1.0,  # [rad]
            'RR_calf_joint': 1.2,  # [rad]
        }

    # class terrain(LeggedRobotCfg.terrain):
    #     mesh_type = 'plane'

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 20.}  # [N*m/rad]
        damping = {'joint': 0.5}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset(LeggedRobotCfg.asset):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/xjqr/urdf/xjqr.urdf'
        name = "xjqr"
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base_link",
                                       "FL_thigh", "FR_thigh", "RL_thigh", "RR_thigh",
                                       "FL_knee", "FR_knee", "RL_knee", "RR_knee"]
        self_collisions = 1

    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.25
        class scales( LeggedRobotCfg.rewards.scales ):
            tracking_lin_vel = 5.0
            torques = -0.0002
            dof_pos_limits = -10.0
            orientation = -2.0
            feet_air_time = 1.0
            # feet_stumble = -5.0
            stand_still = -1.0
            base_height = -2.0


class xjqrRoughCfgPPO(LeggedRobotCfgPPO):
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'xjqr_rough'

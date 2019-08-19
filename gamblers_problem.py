#import numpy as np

class GP():
    def __init__(self, ph=0.4):

        def gen_transitions():
            
            transitions = []

            for state in range(self.nS):
                state_t = []
                for action in range(self.nA):
                    # (prob, next_state, reward, done)

                    if min(state, 100-state) < action or state == 0 or state == 100: # can't stake more than current capital
                        prob_w = prob_l = 0
                    else:
                        prob_w = ph
                        prob_l = 1 - ph

                    win_outcome   = (prob_w , state, action, state + action, 1 if state+action == 100 and state != 100 else 0  , state == 0 or state == 100)
                    loose_outcome = (prob_l , state, action, state - action, 0                                                 , state == 0 or state == 100)

                    outcomes = (win_outcome, loose_outcome)

                    state_t.append(outcomes)
                
                transitions.append(state_t)
            
            return transitions

        self.nS = 101 # state is gamblers capital
        self.nA = 99  # maximum stake amount is min(s, 100-s)

        self.P = gen_transitions()



if __name__ == "__main__":
    env = GP()

    #for a in range(env.nA):
    #    print(env.P[51][a])
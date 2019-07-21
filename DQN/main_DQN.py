from DQN import Agent, DeepQNetwork
import utils
import numpy as np

#need to create an environment



def train(epochs=1):
   eps_history=[]
   eps_history.append(brain.EPSILON)
   
   # the sumamries produced will be put against the ones constructed based on rouge, consine and the other function
   # optimized for rouge score of course 
   '''
    while not done:
        #agent picks an action of the numpy array
        action = brain.chooseAction(observation)


        #each of these variables need to be selected in order to continue
        observation_, reward, done, info = env.step(action)

        rouge_score += reward => from rouge metric
        brain.storeTransition(observation, action, reward, observation_, done)
        #env is set to next state
        observation = observation_

        dqn_agent.learn()


    #could append to a list of running scores for the document
    '''

if __name__ == '__main__':

    #create a DQN agent for learning
    #it will run the rouge score of each sentence

    # Agent creation
    dqn_agent = Agent()


    #need to record the agent history
    

    # Data Loading function
    # Need a training function
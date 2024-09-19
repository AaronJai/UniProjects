from agent import Agent
import random

# Important: Make sure you put your agents in the agents folder, so that the
# game runner code can find them.

class Student(Agent):        
    '''A sample implementation of a random agent in the game The Resistance'''

    def __init__(self, name='22884212'):
        '''
        Initialises the agent.
        '''
        self.name = name
        self.mission_history = []
        self.player_probabilities = {}  # Player index to spy probability

    def new_game(self, number_of_players, player_number, spy_list):
        '''
        initialises the game, informing the agent of the 
        number_of_players, the player_number (an id number for the agent in the game),
        and a list of agent indexes which are the spies, if the agent is a spy, or empty otherwise
        '''
        self.num_players = number_of_players
        self.player_number = player_number
        self.spies = set(spy_list)
        self.mission_history = []

        # Initialize probabilities for all players (except the current agent)
        self.player_probabilities = {player: 0.33 for player in range(number_of_players)}
        self.player_probabilities[self.player_number] = 0.0  # Self is never a spy

    def is_spy(self):
        '''
        returns True iff the agent is a spy
        '''
        return self.player_number in self.spies

    def propose_mission(self, team_size, betrayals_required=1):
        '''
        expects a team_size list of distinct agents with id between 0 (inclusive) and number_of_players (exclusive)
        to be returned. 
        betrayals_required are the number of betrayals required for the mission to fail.
        '''
        return random.sample(range(0, self.num_players), team_size)        

    def vote(self, mission, proposer, betrayals_required=1):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals_required are the number of betrayals required for the mission to fail.
        The function should return True if the vote is for the mission, and False if the vote is against the mission.
        '''
        spy_count = len(set(mission) & self.spies)
        
        if self.is_spy():
            # Spy-specific voting logic
            if spy_count >= betrayals_required:
                return True
            return False

        # Non-spy voting logic based on probabilities
        mission_spy_prob = sum([self.player_probabilities[player] for player in mission])
        
        # Threshold for rejecting a mission
        rejection_threshold = 1.0  # Adjust based on testing
        if mission_spy_prob > rejection_threshold:
            return False

        # If the agent is on the mission, slightly favor approval
        if self.player_number in mission:
            return random.random() < 0.7

        # Otherwise, approve based on lower probability
        return random.random() < 0.5

    def vote_outcome(self, mission, proposer, votes):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        votes is a dictionary mapping player indexes to Booleans (True if they voted for the mission, False otherwise).
        No return value is required or expected.
        '''
        #nothing to do here
        pass

    def betray(self, mission, proposer, betrayals_required=1):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players, and include this agent.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals_required are the number of betrayals required for the mission to fail.
        The method should return True if this agent chooses to betray the mission, and False otherwise. 
        Only spies are permitted to betray the mission.
        By default, spies will betray 30% of the time. 
        '''
        if not self.is_spy():
            return False

        spy_count = len(set(mission) & self.spies)

        if spy_count < betrayals_required:
            return False

        # Strategic decision to betray
        # Example: Only betray if it doesn't reveal the agent as a spy
        # Assume that betraying too often raises suspicion
        betrayal_threshold = 0.3  # Adjust based on testing
        return random.random() < betrayal_threshold

    def mission_outcome(self, mission, proposer, num_betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        num_betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It is not expected or required for this function to return anything.
        '''
        self.mission_history.append({
            'mission': mission,
            'proposer': proposer,
            'num_betrayals': num_betrayals,
            'mission_success': mission_success
        })
        self.update_probabilities()
    
    def update_probabilities(self):
        # Simple Bayesian update based on mission outcomes
        for player in range(self.num_players):
            if player == self.player_number:
                continue
            spy_evidence = 0
            for mission in self.mission_history:
                if player in mission['mission']:
                    if mission['mission_success']:
                        spy_evidence += 0  # Less likely to be a spy
                    else:
                        spy_evidence += 1  # More likely to be a spy
            # Update probability (this is a simplistic approach)
            self.player_probabilities[player] = min(1.0, self.player_probabilities[player] + 0.1 * spy_evidence)

    def round_outcome(self, rounds_complete, missions_failed):
        '''
        basic informative function, where the parameters indicate:
        rounds_complete, the number of rounds (0-5) that have been completed
        missions_failed, the numbe of missions (0-3) that have failed.
        '''
        #nothing to do here
        pass
    
    def game_outcome(self, spies_win, spies):
        '''
        basic informative function, where the parameters indicate:
        spies_win, True iff the spies caused 3+ missions to fail
        spies, a list of the player indexes for the spies.
        '''
        #nothing to do here
        pass

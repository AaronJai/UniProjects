from agent import Agent
import random
import math

class StudentAgent(Agent):
    '''Our implementation'''

    def __init__(self, name='Student'):
        '''
        Initialises the agent.
        And other variables
        '''
        self.name = name
        self.player_probabilities = {}      # Player index to spy probability
        self.mission_history = []           # Store mission outcomes
        self.vote_history = {}              # Store vote patterns
        self.spy_behavior = {}              # Tracks spy behavior for heuristics
        self.total_rounds = 5

    def new_game(self, number_of_players, player_number, spy_list):
        '''
        initialises the game, informing the agent of the 
        number_of_players, the player_number (an id number for the agent in the game),
        and a list of agent indexes which are the spies, if the agent is a spy, or empty otherwise.
        And sets up the variables for mission history, vote history, spy behavior, and player probabilities for our implementation.
        '''
        self.num_players = number_of_players
        self.player_number = player_number
        self.spies = set(spy_list)          # Converting to a set for lookup efficiency
        self.mission_history = []           # Reset mission history for the new game
        
        # Initialize vote history for all players
        self.vote_history = {}
        for player in range(number_of_players):
            self.vote_history[player] = []
        
        # Initialize spy behavior tracking for all players
        self.spy_behavior = {}
        for player in range(number_of_players):
            self.spy_behavior[player] = {'missions': 0, 'betrays': 0}


        # Initialize Bayesian probabilities for all players (except self)
        self.player_probabilities = {}
        for player in range(number_of_players):
            self.player_probabilities[player] = 0.33

        self.player_probabilities[self.player_number] = 0.0  # Self is never a spy

        self.successful_missions = 0
        self.failed_missions = 0
    
    def is_spy(self, player_num=None):
        '''
        returns True iff the given agent is a spy
        '''
        if player_num is not None:
            # If a player number is provided, check if that player is a spy
            return player_num in self.spies
        else:
            # If no player number is provided, check if the agent (self) is a spy
            return self.player_number in self.spies

    def propose_mission(self, team_size, betrayals_required=1):
        '''
        Returns a list of agents to propose for the mission. 
        If spy, it selects a mix of spies and non-spies to reduce suspicion. 
        If not a spy, it selects the players with the lowest spy probabilities.
        '''
        if self.is_spy():
            # Spy strategy: Choose a mixed team with some spies and non-spies to reduce suspicion.
            spy_team = random.sample(self.spies, min(team_size, len(self.spies)))
            non_spies = []
            for i in range(self.num_players):
                if i not in self.spies:
                    non_spies.append(i)

            return spy_team + random.sample(non_spies, team_size - len(spy_team))

        # Resistance strategy: Choose players with the lowest spy probability
        sorted_players = sorted(self.player_probabilities.items(), key=lambda x: x[1])
        team = []
        for player, probability in sorted_players[:team_size]:
            team.append(player)

        return team

    def vote(self, mission, proposer, betrayals_required=1):
        '''
        Determines whether the agent votes for or against the mission. 
        If spy, it votes to approve missions it can sabotage, or occasionally approves good missions to reduce suspicion. 
        If not a spy (resistance), it votes based on the calculated spy probability of the mission members and the proposer.
        If the mission's spy probability or the proposer's probability is too high, the mission is rejected.
        '''
        if self.is_spy():
            # Spies approve missions they can sabotage but also approve successful missions to avoid suspicion
            spy_count = len(set(mission) & self.spies)
            if spy_count >= betrayals_required:
                return True  # Spy-heavy mission, ensure failure

            # Sometimes approve a good mission to reduce suspicion
            return random.random() < 0.3

        # Resistance: Calculate total spy probability of mission members
        total_spy_prob = 0
        for player in mission:
            total_spy_prob += self.player_probabilities[player]

        mission_spy_prob = total_spy_prob / len(mission)

        # See if proposer is suspicious
        if mission_spy_prob > 0.6 or self.player_probabilities[proposer] > 0.6:
            return False  # Reject mission with high spy likelihood

        return self._simulate_future_vote_outcome(mission, proposer, betrayals_required)

    def vote_outcome(self, mission, proposer, votes):
        '''
        Records each player's vote in their voting history.
        '''
        for player, vote in enumerate(votes):
            self.vote_history[player].append(vote)

    def betray(self, mission, proposer, betrayals_required=1):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players, and include this agent.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals_required are the number of betrayals required for the mission to fail.
        The method should return True if this agent chooses to betray the mission, and False otherwise. 
        Only spies are permitted to betray the mission.

        Betrayal decision is based on various factors: if enough spies are present to ensure failure, 
        if the game state (e.g., 2 failed or 2 successful missions) makes a betrayal crucial, 
        or if the agent prefers to remain hidden by avoiding unnecessary betrayals.
        '''
        if not self.is_spy():
            return False

        # Spy betrayal: Only betray when necessary or strategically good
        spy_count = len(set(mission) & self.spies)

        if spy_count >= betrayals_required:
            # Ensure mission fails if enough spies are present
            return True

        # betray when tied (2-2)
        if self.failed_missions == 2 or self.successful_missions == 2:
            return True

        # Spy behavior: betray only if necessary or if staying hidden no longer matters
        if spy_count > 1 and betrayals_required == 1:
            return random.random() < 0.5  # Less predictable betrayal behavior

        # Keep betrayal probability low to avoid detection
        return random.random() < 0.3

    def mission_outcome(self, mission, proposer, num_betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        num_betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It is not expected or required for this function to return anything.
        
        Also updates the mission history with the outcome and applies Bayesian reasoning to update spy probabilities for players based on success or failure.
        Tracks spy-like behavior (number of missions and betrayals) for each player to identify patterns 
        and adjusts the probabilities after each mission based on vote patterns, allowing the agent to refine its predictions.
        '''
        self.mission_history.append({
            'mission': mission,
            'proposer': proposer,
            'num_betrayals': num_betrayals,
            'mission_success': mission_success
        })

        # Bayesian updates for spy probabilities based on mission success and betrayals
        for player in mission:
            self._bayesian_update(player, mission_success, num_betrayals)

        # Track spy-like behavior for heuristics
        if not mission_success:
            for player in mission:
                self.spy_behavior[player]['missions'] += 1
                self.spy_behavior[player]['betrays'] += num_betrayals

        # Adjust probabilities based on vote history after each mission
        for player in range(self.num_players):
            self._adjust_for_voting_patterns(player)

    def round_outcome(self, rounds_complete, missions_failed):
        '''
        basic informative function, where the parameters indicate:
        rounds_complete, the number of rounds (0-5) that have been completed
        missions_failed, the numbe of missions (0-3) that have failed.
        '''
        self.successful_missions = rounds_complete - missions_failed
        self.failed_missions = missions_failed
        pass

    def game_outcome(self, spies_win, spies):
        '''
        basic informative function, where the parameters indicate:
        spies_win, True iff the spies caused 3+ missions to fail
        spies, a list of the player indexes for the spies.
        '''
        #nothing to do here
        pass


    # Helper Methods #

    def _simulate_future_vote_outcome(self, mission, proposer, betrayals_required):
        '''Simulate future rounds to adjust voting decisions based on minimax-inspired logic.'''
        
        # Get current round number and remaining rounds in the game
        current_round = len(self.mission_history)
        remaining_rounds = self.total_rounds - current_round

        # Estimate likelihood that this mission has spies
        total_spy_prob = 0
        for player in mission:
            total_spy_prob += self.player_probabilities[player]
        future_spy_prob = total_spy_prob / len(mission)

        # Estimate likelihood that the proposer is a spy
        proposer_spy_prob = self.player_probabilities[proposer]

        if proposer_spy_prob > 0.5:
            return False  # Reject missions from highly suspicious proposers

        if future_spy_prob > 0.5 and remaining_rounds > 1:
            return False  # Too risky, reject to improve future rounds

        if future_spy_prob > 0.5 and betrayals_required == 1:
            return False  # High-risk missions should be rejected

        return True  # Accept if the probabilities are reasonable

    def _bayesian_update(self, player, mission_success, num_betrayals):
        '''Update player spy probabilities based on mission outcomes with Bayesian inference.'''
        
        # If the mission was successful, reduce the player's probability of being a spy.
        # The reduction is scaled by the inverse of the number of betrayals (fewer betrayals -> more reduction).
        if mission_success:
            # Decrease spy probability: The fewer betrayals, the larger the reduction.
            # Example: If no betrayals, the probability is reduced more significantly.
            self.player_probabilities[player] = max(0, self.player_probabilities[player] - 0.1 * (1 - num_betrayals))
        else:
            # If the mission failed, increase the player's probability of being a spy.
            # The increase is proportional to the number of betrayals (more betrayals -> more suspicion).
            # This reflects a higher likelihood that players on a failed mission are spies.
            self.player_probabilities[player] = min(1.0, self.player_probabilities[player] + 0.15 * num_betrayals)

    def _adjust_for_voting_patterns(self, player):
        '''Adjust spy probabilities based on voting behavior.'''
        
        # Only adjust the player's spy probability if we have sufficient vote history (more than 5 votes).
        if len(self.vote_history[player]) > 5:
            # Count how many times the player has voted against a mission.
            suspicious_votes = 0
            for vote in self.vote_history[player]:
                if vote == False:
                    suspicious_votes += 1

            # Calculate the ratio of suspicious (negative) votes to the total number of votes.
            vote_ratio = suspicious_votes / len(self.vote_history[player])
            
            # If more than 50% of the player's votes are suspicious (against missions),
            # this is typical spy behavior (sabotaging missions), so increase their spy probability.
            if vote_ratio > 0.5:
                self.player_probabilities[player] = min(1.0, self.player_probabilities[player] + 0.2)
            else:
                # If the player mostly votes in favor of missions, reduce their probability of being a spy.
                # This shows they're behaving like a Resistance member.
                self.player_probabilities[player] = max(0, self.player_probabilities[player] - 0.1)

import random
import numpy as np 
import string

alphabets=list(string.ascii_lowercase)+[" ", ",","'","."]
phrase= input("What is the word or phrase you would like the computer to predict: ")
phrase = phrase.lower()


def generate_list():
	phrase_list = []

	# Initialize the phrase list
	for i in range(200):
		word=""
		for j in range(len(phrase)):
			word = word + random.choice(alphabets)
		phrase_list.append(word)

	return phrase_list

# compute the fitness score for each phrase
def compute_fitness(phrase_list):
	fitness_list= []
	total_score = 0
	for pop_phrase in phrase_list:
		score = 0
		for i in range(len(phrase)):
			if pop_phrase[i] == phrase[i]:
				score+=1
		score = score*score
		total_score+=score

		fitness_list.append((pop_phrase, score))

	return fitness_list, total_score


# Create the selection process
def compute_selection(fitness_list, total_score):
	selection_pool = []
	
	# adds more phrases to the list based on the relative score
	for fit_phrase in fitness_list:
		total_copy = int((float(fit_phrase[1])/float(total_score))*len(fitness_list))
		for i in range(total_copy):
			selection_pool.append(fit_phrase[0])

	return selection_pool

# recombine from selction process with mutation and add to phrase list
def compute_recombination(selection_pool, phrase_list, fitness_list, mutation_factor = 0.01, dying_factor=0.01):
	
	# Chooses 100 members of the population to kill off and replace with the offspring
	indicies_to_replace = []

	for i in range(100):
		indicies_to_replace.append(random.randint(0,100))

	for i in indicies_to_replace:
		top_2 = []
		for j in range(2):
			if j==0:
				top_2.append(random.choice(selection_pool))
				sub_pool = [ele for ele in selection_pool if ele != top_2[0]]
			else:
				top_2.append(random.choice(sub_pool))

		# Random splitting of the index, better for variance
		split_index = random.choice([i for i in range(len(top_2[0]))])
		new_word = top_2[0][0:split_index] + top_2[1][split_index:]


		# incorperates the mutation rate to alter the combined word
		mutation_compound = int(mutation_factor*1000)
		mutation_list= [1]*mutation_compound + [0]*(1000-mutation_compound)
		determine_mutation = random.choice(mutation_list)
		if determine_mutation == 1:
			new_word = list(new_word)
			index_of_choice = random.choice([k for k in range(len(new_word))])
			new_word[index_of_choice] = random.choice(alphabets)
			word_to_be=""
			for letter in new_word:
				word_to_be+=letter
			new_word=word_to_be

		

		phrase_list[i] = new_word

	return phrase_list


def run_simulation():
	phrase_list = generate_list()
	count = 0
	while phrase not in phrase_list:
		fitness_list, total_score= compute_fitness(phrase_list)
		fitness_values = sorted(fitness_list, key=lambda phrase: phrase[1],reverse=True)
		top_value=fitness_values[0]
		print(top_value)
		print()
		selection_pool = compute_selection(fitness_list,total_score)
		phrase_list= compute_recombination(selection_pool, phrase_list, fitness_list)

		count +=1
	fitness_list, total_score= compute_fitness(phrase_list)
	fitness_values = sorted(fitness_list, key=lambda phrase: phrase[1],reverse=True)
	top_value=fitness_values[0]
	print(top_value)
	print("It took the genetic algorithm "+ str(count) + " tries to get the word you entered")

run_simulation()










	








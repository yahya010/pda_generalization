import random
import json
from collections import defaultdict

# Define lemmas, number markers, and inflection rules
class SyntheticLanguageGenerator:
    def __init__(self, lemma_freq=None, number_marker_freq=None):
        # Default vocabularies
        self.lemmas = ['to be', 'to have', 'to go', 'to eat']
        self.number_markers = ['he', 'she', 'it', 'they', 'we']
        self.inflection_rules = {
            ('to be', 'he'): 'is',
            ('to be', 'she'): 'is',
            ('to be', 'it'): 'is',
            ('to be', 'they'): 'are',
            ('to be', 'we'): 'are',
            ('to have', 'he'): 'has',
            ('to have', 'she'): 'has',
            ('to have', 'it'): 'has',
            ('to have', 'they'): 'have',
            ('to have', 'we'): 'have',
            ('to go', 'he'): 'goes',
            ('to go', 'she'): 'goes',
            ('to go', 'it'): 'goes',
            ('to go', 'they'): 'go',
            ('to go', 'we'): 'go',
            ('to eat', 'he'): 'eats',
            ('to eat', 'she'): 'eats',
            ('to eat', 'it'): 'eats',
            ('to eat', 'they'): 'eat',
            ('to eat', 'we'): 'eat',
        }

        # Frequencies (probabilities) for sampling
        # If frequencies are not provided, use uniform distribution
        self.lemma_freq = lemma_freq or {lemma: 1/len(self.lemmas) for lemma in self.lemmas}
        self.number_marker_freq = number_marker_freq or {nm: 1/len(self.number_markers) for nm in self.number_markers}

        # Normalize frequencies
        self._normalize_frequencies()

    def _normalize_frequencies(self):
        # Normalize lemma frequencies
        total = sum(self.lemma_freq.values())
        for lemma in self.lemma_freq:
            self.lemma_freq[lemma] /= total

        # Normalize number marker frequencies
        total = sum(self.number_marker_freq.values())
        for nm in self.number_marker_freq:
            self.number_marker_freq[nm] /= total

    def sample_lemma(self):
        lemmas = list(self.lemma_freq.keys())
        probabilities = [self.lemma_freq[lemma] for lemma in lemmas]
        return random.choices(lemmas, weights=probabilities, k=1)[0]

    def sample_number_marker(self):
        nms = list(self.number_marker_freq.keys())
        probabilities = [self.number_marker_freq[nm] for nm in nms]
        return random.choices(nms, weights=probabilities, k=1)[0]

    def get_inflected_form(self, lemma, number_marker):
        key = (lemma, number_marker)
        return self.inflection_rules.get(key, 'UNKNOWN')

    def generate_sentence(self):
        # Simulate PDA transitions
        # State q0: Output lemma
        lemma = self.sample_lemma()

        # State q1: Output number marker
        number_marker = self.sample_number_marker()

        # State q2: Output inflected form based on lemma and number marker
        inflected_form = self.get_inflected_form(lemma, number_marker)

        # Return the generated components
        return {
            'lemma': lemma,
            'number_marker': number_marker,
            'inflected_form': inflected_form
        }

    def generate_dataset(self, num_samples):
        dataset = []
        for _ in range(num_samples):
            sample = self.generate_sentence()
            dataset.append(sample)
        return dataset

    def save_dataset(self, dataset, filename):
        with open(filename, 'w') as f:
            json.dump(dataset, f, indent=2)

# Example
if __name__ == '__main__':
    # Define custom frequencies if needed
    lemma_freq = {
        'to be': 0.4,
        'to have': 0.3,
        'to go': 0.2,
        'to eat': 0.1
    }

    number_marker_freq = {
        'he': 0.25,
        'she': 0.25,
        'it': 0.1,
        'they': 0.3,
        'we': 0.1
    }

    generator = SyntheticLanguageGenerator(lemma_freq=lemma_freq, number_marker_freq=number_marker_freq)

    # Generate a dataset of 100 samples
    dataset = generator.generate_dataset(100)

    #save the dataset to a file
    generator.save_dataset(dataset, 'synthetic_dataset.json')
    
    for sample in dataset[:5]:
        print(f"Lemma: {sample['lemma']}, Number Marker: {sample['number_marker']}, Inflected Form: {sample['inflected_form']}")

import random
imagenet_labels = dict(enumerate(open('ilsvrc2012_wordnet_lemmas.txt')))

print(imagenet_labels[random.randint(0, 1000)])

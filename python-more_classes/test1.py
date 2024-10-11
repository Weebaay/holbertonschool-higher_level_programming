#!/usr/bin/python3
import gc
Rectangle = __import__('5-rectangle').Rectangle

# Créer des instances de Rectangle
r1 = Rectangle(3, 2)
r2 = Rectangle(5, 7)

print("Number of instances: {}".format(Rectangle.number_of_instances))

# Supprimer une instance
del r1

# Forcer la collecte des objets non utilisés
gc.collect()

print("Number of instances after deletion: {}".format(Rectangle.number_of_instances))

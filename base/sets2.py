mammals = {'tiger', 'camel', 'sheep', 'whale', 'walrus'}
aquatic_mammals = {'whale', 'walrus'}

# >>> aquatic_mammals < mammals
# True
# >>> mammals > aquatic_mammals
# True

reptiles = {'turtle', 'snake', 'lizard', 'crocodile'}

# >>> mammals.isdisjoint(reptiles)
# True
# >>> reptiles.isdisjoint(mammals)
# True

aquatic = {'octopus', 'crab', 'squid', 'whale', 'walrus'}

# >>> mammals | aquatic
# {'sheep', 'camel', 'whale', 'tiger', 'crab', 'walrus', 'octopus', 'squid'}

# >>> mammals & aquatic
# {'walrus', 'whale'}

# >>> mammals - aquatic
# {'sheep', 'camel', 'tiger'}

# >>> aquatic - mammals
# {'crab', 'octopus', 'squid'}

# >>> mammals ^ aquatic
# {'sheep', 'camel', 'tiger', 'crab', 'octopus', 'squid'}


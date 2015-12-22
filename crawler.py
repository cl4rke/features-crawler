import sys
import os


def import_features(directory):
    features = {}

    for filename in os.listdir(directory):
        features_file = open(os.path.join(directory, filename))
        for line in features_file:
            name = line.split(' ===== ')[0].strip()
            usages = line.split('============= ')[1].strip()

            features[name] = usages

    return features


if len(sys.argv) < 3:
    print 'Usage:   python main.py <dir> <features to find seperated by ==$==>'
    print 'Example: python main.py ~/Downloads/features/ some==$==features==$==hello'
else:
    features = import_features(sys.argv[1])
    features_to_find = sys.argv[2]

    for name in features_to_find:
        print name, features[name]


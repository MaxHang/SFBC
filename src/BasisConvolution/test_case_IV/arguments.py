import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e','--epochs', type=int, default=1)
parser.add_argument('-cmap','--coordinateMapping', type=str, default='cartesian')
parser.add_argument('-w','--windowFunction', type=str, default='None')
parser.add_argument('-b','--batch_size', type=int, default=4)
parser.add_argument('-o','--output', type = str, default = '../../trainingData/test_case_IV')
parser.add_argument('--cutlassBatchSize', type=int, default=128)
parser.add_argument('-initLR','--initialLR', type=float, default=1e-2)
parser.add_argument('-fLR','--finalLR', type=float, default=1e-4)
parser.add_argument('--lrStep', type=int, default=10)
parser.add_argument('--weight_decay', type=float, default=0)
parser.add_argument('-rx','--rbf_x', type=str, default='linear')
parser.add_argument('-ry','--rbf_y', type=str, default='linear')
parser.add_argument('-rz','--rbf_z', type=str, default='linear')
parser.add_argument('-nx','--nx', type=int, default=4)
parser.add_argument('-ny','--ny', type=int, default=4)
parser.add_argument('-nz','--nz', type=int, default=4)
parser.add_argument('--seed', type=int, default=42)
parser.add_argument('--networkseed', type=int, default=42)
parser.add_argument('--gpu', type=int, default=0)
parser.add_argument('--gpus', type=int, default=1)
parser.add_argument('-f','--forwardLoss', type=bool, default=False)
parser.add_argument('-v','--verbose', type=bool, default=False)
parser.add_argument('-l','--li', type=bool, default=False)
parser.add_argument('-a','--activation', type=str, default='relu')
parser.add_argument('-i','--input', type=str, default='../../datasets/test_case_IV/lowJitter.hdf5')
# parser.add_argument('-o','--output', type=str, default='../../trainingData')
# parser.add_argument('--arch', type=str, default='32 64 64 3')
parser.add_argument('--arch', type=str, default='1')
parser.add_argument('--iterations', type=int, default=5000)
parser.add_argument('-augj', '--augmentJitter', type=bool, default=True)
parser.add_argument('-j', '--jitterAmount', type=float, default=0.01)
parser.add_argument('-augr', '--augmentAngle', type=bool, default=True)
parser.add_argument('-adjust', '--adjustForFrameDistance', type = bool, default = True)
parser.add_argument('-netArch', '--network', type=str, default='default')
parser.add_argument('-norm', '--normalized', type=bool, default=False)

parser.add_argument('-target', '--target', type=str, default='rho')
parser.add_argument('-features', '--features', type=str, default='normalizedVolume')
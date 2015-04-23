#!/usr/bin/env python
# esempio: ./diffXML.py AlignmentResults/Iter0/xml/Conditions/TT/Alignment/Modules.xml AlignmentResults_sposto/Iter0/xml/Conditions/TT/Alignment/Modules.xml

##########################
###   Options parser   ###
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = '''read 2 xml files and give the differences 
    ./diffXML.py AlignmentResults/Iter0/xml/Conditions/TT/Alignment/Modules.xml AlignmentResults_sposto/Iter0/xml/Conditions/TT/Alignment/Modules.xml''')
    parser.add_argument('file1',help='First file')
    parser.add_argument('file2',help='Second file')
    args = parser.parse_args()
##########################
    
import xml.etree.ElementTree
import os


def readXML(inFile):
    '''
    Read XML file and return dictionary with {name: align_params}
    where align_params is a list [Tx, Ty, Tz, Rx, Ry, Rz]
    '''
    tree = xml.etree.ElementTree.parse(inFile)
    root = tree.getroot()
    alignParams = {}
    for alignable in root:
        name = alignable.attrib['name']
        for vec in alignable:
            if vec.attrib['name'] == 'dPosXYZ':
                [Tx, Ty, Tz] = [float(i) for i in vec.text.split()]
            elif vec.attrib['name'] == 'dRotXYZ':
                [Rx, Ry, Rz] = [float(i) for i in vec.text.split()] 

        alignParams[name] = [Tx, Ty, Tz, Rx, Ry, Rz]
    return alignParams


def getDictDifference(file1, file2):
    """
    Read two XML files and return dictionary with {name: diff}
    where diff is a list with the differences [dTx, dTy, dTz, dRx, dRy, dRz]
    """
    align1 = readXML(file1)
    align2 = readXML(file2)
    diff = {}
    for key in set(align1.keys() + align2.keys()):
        try:
            diff[key] = [i-j for i,j in zip(align1[key], align2[key])]
        except KeyError:
            pass
    return diff


def bigChanges(diff, list_max_diff):
    '''
    Return the dictionary of alignables which deviated more than they should have
    {alignable_dof : param_diff}
    '''
    bigs = {}
    dofs = ['Tx', 'Ty', 'Tz', 'Rx', 'Ry', 'Rz']
    for name, params in diff.items():
        for param, par_max, dof in zip(params, list_max_diff, dofs):
            if abs(param) > par_max:
                bigs['{name}_{dof}'.format(**locals())] = param
    return bigs


def get2Files(directory):
    return sorted(os.listdir(directory))[:2]


if __name__ == '__main__':
    list_max_diff = [0.0, 0.0, 0., 0.00, 0.00, 0.0]
    diff = getDictDifference(args.file1, args.file2)
    print diff
    print bigChanges(diff, list_max_diff)
    # print sorted(bigChanges(diff, list_max_diff).keys())

    print diff['TTaXLayerR1Module1T']

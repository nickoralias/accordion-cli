import json
import argparse

from typing import List

class PianoAccordion:
    def __init__(self, make, trebleKeys, bassKeys, trebleReeds, tuning, status, model):
        self._make = str(make)
        self._trebleKeys = int(trebleKeys)
        self._bassKeys = int(bassKeys)
        self._trebleReeds = int(trebleReeds)
        self._tuning = str(tuning)
        self._status = str(status)
        self._model = str(model)
    
    def get_make(self):
        return self._make
    
    def set_make(self, make):
        self._make = make

    def get_trebleKeys(self):
        return self._trebleKeys

    def set_trebleKeys(self, trebleKeys):
        self._trebleKeys = trebleKeys

    def get_bassKeys(self):
        return self._bassKeys

    def set_bassKeys(self, bassKeys):
        self._trebleKeys = bassKeys

    def get_trebleReeds(self):
        return self._trebleReeds

    def set_trebleReeds(self, trebleReeds):
        self._trebleKeys = trebleReeds

    def get_tuning(self):
        return self._tuning
    
    def set_tuning(self, tuning):
        self._tuning=tuning

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def __str__(self):
        return "PianoAccordion{" + "make=" + self._make + ", trebleKeys=" + self._trebleKeys + ", bassKeys=" + self._bassKeys + ", trebleReeds=" + self._trebleReeds + ", tuning=" + self._tuning + '}'

    def __repr__(self):
        return "PianoAccordion{" + "make=" + self._make + ", trebleKeys=" + str(self._trebleKeys) + ", bassKeys=" + str(self._bassKeys) + ", trebleReeds=" + str(self._trebleReeds) + ", tuning=" + self._tuning + '}'


def filterList(inputList: List[PianoAccordion], args) -> List[PianoAccordion]:
    resultList = []

    def arg_to_attribute(arg, obj: PianoAccordion):
        switch = {
            'make': obj.get_make()
        }
        return switch.get(arg, 'Nothing')

    if args:
        for k, v in args.items():
            for a in inputList:
                if str(arg_to_attribute(k, a)) == str(v):
                    resultList.append(a)
        return resultList
    else:
        return inputList

def main():
    filename = 'inventory.json'
    inputList = []

    # import inventory data
    with open(filename, 'r') as file:
        data = json.load(file)
        for a in data:
            try:
                tmp = PianoAccordion(
                    a.get('make'),
                    a.get('trebleKeys'),
                    a.get('bassKeys'),
                    a.get('trebleReeds'),
                    a.get('tuning'),
                    a.get('status'),
                    a.get('model')
                )
                inputList.append(tmp)
            except Exception as e:
                print(e)

    # filter the list
    parser = argparse.ArgumentParser(description = 'Filter the inventory list')
    parser.add_argument('--make', help='Make of accordion', required=False)
    parser.add_argument('--trebleKeys', help='Number of treble keys', required=False)
    args = vars(parser.parse_args())

    print(filterList(inputList, args))

if __name__ == '__main__':
    main()

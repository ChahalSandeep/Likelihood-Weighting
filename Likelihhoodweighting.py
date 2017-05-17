import random
import numpy as np

#CPT
probablity_w=0.3
probablity_c=0.8
probablity_i=0.5
probablity_ts=np.array([0.2,0.4,0.1,0.7])
probablity_o=np.array([0.2,0.5,0.3,0.6])
probablity_r=np.array([0.9,0.5,0.3,0.1])

sample_numbers=int(input("Enter a number of samples: "))


def check_probability_independent(value,probablity_element):
    if value<=probablity_element:
        return 1
    else:
        return 0


def check_probability_dependent(value,probablity_element,first_dependent_element,sec__dependent_element):
    if first_dependent_element==1 and sec__dependent_element==1:
        a = probablity_element[3]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==1 and sec__dependent_element==0:
        a = probablity_element[2]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==0 and sec__dependent_element==1:
        a = probablity_element[1]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==0 and sec__dependent_element==0:
        a = probablity_element[0]
        if value<=a:
            return 1
        else:
            return 0

def fixing_r(first_dependent_element,sec__dependent_element):    #value,probablity_element
    if first_dependent_element==1 and sec__dependent_element==1:
        return 1,0.1
    elif first_dependent_element==1 and sec__dependent_element==0:
        return 1,0.3

    elif first_dependent_element==0 and sec__dependent_element==1:
        return 1,0.5
    elif first_dependent_element==0 and sec__dependent_element==0:
        return 1,0.9

sample_store=[]
weight_vector=[]
for x in range (sample_numbers):
    #states=6
    states=5
    w=1
    sample_list=[]
    for y in range(states):
        if y==0:
            ran_number=random.uniform(0,0.5)
        elif y==1:
            ran_number=random.uniform(0,0.8)
        #elif y==5:
        #    ran_number=random.uniform(0,0.1)
        else:
            ran_number = random.uniform(0, 1)
        sample_list.append(ran_number)
    #print(len(sample_list))
    one_element=1
    w=w*probablity_i
    sec_element =1
    w=w*probablity_c
    thi_element = check_probability_independent(sample_list[2], probablity_w)
    fou_element = check_probability_dependent(sample_list[3], probablity_o,one_element,sec_element)
    fif_element = check_probability_dependent(sample_list[4], probablity_ts,sec_element,thi_element)
    six_element,prob_r = fixing_r(fou_element,fif_element)  #sample_list[5], probablity_r,
    sample_list.append(1)
    w=w*prob_r
    weight_vector.append(w)
    sample_result=np.array([one_element,sec_element,thi_element,fou_element,fif_element,six_element])
    sample_store.append(sample_result)

    print(sample_result)
print(type(weight_vector))
#print(len(sample_store))
favorable_weights=0
for x in range(len(sample_store)):
    if(sample_store[x][4]==1):
        favorable_weights=favorable_weights+weight_vector[x]


favorable_unfavourable_weights = sum(weight_vector)

print(favorable_weights/favorable_unfavourable_weights)

